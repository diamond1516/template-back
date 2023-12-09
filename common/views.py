import smtplib
import ssl
from email.message import EmailMessage

from django.shortcuts import render
from django.template.loader import render_to_string

from . import models


# Create your views here.


def home(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        subject = data.get('subject')
        msg = data.get('message')
        name = data.get('name')
        send_code_email(email, subject, msg, name)
    portfolios = []
    for portfolio in models.Portfolio.objects.all():
        data = {'obj': portfolio}
        string = ''
        for i in portfolio.status.all():
            string += i.status + ' '
        data['status'] = string
        string = ''
        portfolios.append(data)
    contex = {
        'works': models.Workflow.objects.all()[:3],
        'about': models.About.objects.first(),
        'teams': models.Team.objects.all()[:4],
        'portfolios': portfolios
    }
    return render(request, template_name='index.html', context=contex)


def send_code_email(email, subject, msg, name):
    body = render_to_string('email.html', {'msg': msg, 'name': name})
    em = EmailMessage()
    em['From'] = 'ahmadboyabdurahimov589@gmail.com'
    em['To'] = email
    em['Subject'] = subject
    em.set_content(body, subtype='html')
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login('ahmadboyabdurahimov589@gmail.com', 'dmhslgpsuasutxcn')
        smtp.sendmail('ahmadboyabdurahimov589@gmail.com', email, em.as_string())
