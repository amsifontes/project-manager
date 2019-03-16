from django.shortcuts import render

from .models import Project, Phase
# Create your views here.
# def retrieve_project_id():


def hello(request):
    # users = User.objects.all()
    # print(Project.objects.all()[1])
    # print(Phase.objects.all()[1])
    # print(request)
    

    # output = {}
    # p_id = retrieve_project_id(request.)

    # context = {
    #     'first_project': {
    #         'name': name_proj,
    #         'proj_id': proj_id,
    #         'start_date': start_date,
    #         'end_date': end_date,
    #         'phases': [
    #                 'phase 1': {
    #                     'name': phase_name,
    #                     'start': start,
    #                     'end': end,
    #                 },
    #                 'phase 2',
    #                 'phase 3',
    #         ]
    #         }

    # }
    projects = Project.objects.all()
    
    phases = Phase.objects.all()
    project_list = []
    for project in projects:
        proj_dict = dict()
        proj_dict["project_name"] = project.name_proj
        proj_dict["address"] = project.address
        proj_dict["start_date"] = project.start_date
        proj_dict["end_date"] = project.end_date
        proj_dict["phases"] = [phase for phase in phases]
        project_list.append(proj_dict)

        context = {
            'projects_list': project_list
        }
    


        # print('project:', project)
        # print('all phases:' project.phases.all())
    print('projects list:', project_list)
        # context["project_name"] = project.name
        # context["address"] = project.address
        



    # for item in first_project.phases
    #     for whatevs in item.level2.level3.level4
    #     <p>item.name</p>

    # print(Project.objects.count())
    # for project in projects:
    #     print(project.id)
    #

    context = {
        # 'projects': projects,
        # 'phases': phases,
    }
    return render(request, 'pages/hello.html', context)
