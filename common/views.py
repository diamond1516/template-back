from django.shortcuts import render
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
