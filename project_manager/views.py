from django.shortcuts import render

from .models import Project, Phase
# Create your views here.
def hello(request):
    # users = User.objects.all()
    projects = Project.objects.all()
    phases = Phase.objects.all()

    context = {
        'projects': projects,
        'phases': phases,
    }
    return render(request, 'pages/hello.html', context)
