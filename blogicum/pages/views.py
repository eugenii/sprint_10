from django.shortcuts import render


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
