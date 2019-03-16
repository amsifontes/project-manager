from django.shortcuts import render

from .models import Project, Phase
# Create your views here.
# def retrieve_project_id():


def hello(request):

    projects = Project.objects.all()
    
    phases = Phase.objects.all()
    project_list = []
    for project in projects:
        proj_dict = dict()
        proj_dict["project_name"] = project.name_proj
        proj_dict["address"] = project.address
        proj_dict["start_date"] = project.start_date
        proj_dict["end_date"] = project.end_date
        proj_dict["phases"] = project.phases.all()
        project_list.append(proj_dict)
        print('project:', project, '   phases:',proj_dict["phases"])

    context = {
        'projects_list': project_list
    }




    print('projects list:', project_list)
    return render(request, 'pages/hello.html', context)
