import smtplib
import ssl
import uuid
from email.message import EmailMessage

from django.shortcuts import render
from django.template.loader import render_to_string

from . import models


# Create your views here.


def home(request):
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


def homepost(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, template_name='index.html')


def send_code_email(email, code):
    subject = "Soff.uz"
    body = render_to_string('email.html', {'code': code})
    em = EmailMessage()
    em['Message-ID'] = str(uuid.uuid4())
    em['From'] = 'EMAIL'
    em['To'] = email
    em['Subject'] = subject
    em.set_content(body, subtype='html')
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('server2.ahost.cloud', 465, context=context) as smtp:
        smtp.login('EMAIL', 'EMAIL_PASSWORD')
        smtp.sendmail('EMAIL', email, em.as_string())
