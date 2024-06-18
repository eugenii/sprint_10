from django.shortcuts import render
from django.views.generic import TemplateView

'''
def about(request):
    template_name = 'pages/about.html'
    context = {
        'title': 'О проекте',
    }
    return render(request, template_name, context)


def rules(request):
    template_name = 'pages/rules.html'
    context = {
        'title': 'Наши правила',
    }
    return render(request, template_name, context)
'''
    

class About(TemplateView):
    template_name = 'pages/about.html'


class Rules(TemplateView):
    template_name = 'pages/rules.html'


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def custom_error_500(request):
    return render(request, 'pages/500.html', status=500)

