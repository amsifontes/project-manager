from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.models import User
from django import forms

from .models import Architect, Client, Project, Phase

architects = Architect.objects.all()
# print(architects)
architect_choices_list = []
for architect in architects:
    architect_option = (architect, architect.username)
    architect_choices_list.append(architect_option)
architect_choices_tuple = tuple(architect_choices_list)

clients = Client.objects.all()
client_choices_list = []
for client in clients:
    client_option = (client, client.username)
    client_choices_list.append(client_option)
client_choices_tuple = tuple(client_choices_list)

# (
#     ('1', 'Architect option 1'),
#     ('2', 'Architect option 2'),
# )

#forms as classes
class ProjectForm(forms.Form):
    architect = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect, 
        choices=architect_choices_tuple,
        )
    client  = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect, 
        choices=client_choices_tuple,
        )
    name_proj  = forms.CharField(max_length=100)
    address  = forms.CharField(max_length=100)
    start_date  = forms.DateField(widget=forms.SelectDateWidget)
    end_date  = forms.DateField(widget=forms.SelectDateWidget)

# Create your views here.
# def retrieve_project_id():


# main project view - render all projects and related phases
def hello(request):
    projects = Project.objects.all()
    project_list = []
    for project in projects:
        proj_dict = dict()
        proj_dict["project_name"] = project.name_proj
        proj_dict["address"] = project.address
        proj_dict["start_date"] = project.start_date
        proj_dict["end_date"] = project.end_date
        proj_dict["phases"] = project.phases.all()
        project_list.append(proj_dict)
        # print('project:', project, '   phases:',proj_dict["phases"])
    context = {
        'projects_list': project_list
    }
    # print('projects list:', project_list)
    return render(request, 'pages/hello.html', context)

def create_project(request):
    # process form data if POST request
    if request.method == 'POST':
        # create form instance
        form = ProjectForm(request.POST)
        # confirm form values are valid

        # TODO: validate address with LOB API HERE


        if form.is_valid():
            print("form.cleaned_data['architect']: ", form.cleaned_data['architect'])
            Project.objects.create(
                # architect_username = form.cleaned_data['architect_username'],
                # architect = form.cleaned_data['architect'],
                architect = Architect.objects.get(username=form.cleaned_data['architect']),

                # client = form.cleaned_data['client'],
                client = Client.objects.get(username=form.cleaned_data['client']),
                name_proj = form.cleaned_data['name_proj'],
                address = form.cleaned_data['address'],
                start_date = form.cleaned_data['start_date'],
                end_date = form.cleaned_data['end_date'],
            )
            # messages.info(request, "New Project Created")
            return redirect('/hey/')

    else:
        form = ProjectForm()
    
    context = {
        'form': form,
        # 'mesages': messages,
    }
    # TODO: create html file create-project.html
    return render(request, 'pages/create-project.html', context)


def update_project(request, project_id):
    project = Project.objects.get(id=project_id)

    form = ProjectForm(
          initial={
              'architect': project.architect,
              'client': project.client, 
              'name_proj': project.name_proj,
              'address': project.address,
              'start_date': project.start_date,
              'end_date': project.end_date,
          }
     )
    # read (CRUD)
    print('120:',request.POST)
    # not certain of the purpose of this if statement
    if 'project' in request.POST:
        print('123:',request.POST)
        # update (CRUD)
        # should these be changed to = form.cleaned_data['architect'] ?
        project.architect = request.POST['architect']
        project.client = request.POST['client']
        project.name_proj = request.POST['name_proj']
        project.address = request.POST['address']
        project.start_date = request.POST['start_date']
        project.end_date = request.POST['end_date']


        # project.architect = Architect.objects.get(username=form.cleaned_data['architect'])
        # project.client = Client.objects.get(username=form.cleaned_data['client'])
        # project.name_proj = form.cleaned_data['name_proj']
        # project.address = form.cleaned_data['address']
        # project.start_date = form.cleaned_data['start_date']
        # project.end_date = form.cleaned_data['end_date']

        



        project.save()
        return redirect('/hey/')

    context = {
        'project': project,
        'form': form
    }
    return render(request, 'pages/update-project.html', context)

    pass

def create_phase(request):
    pass

def update_phase(request):
    pass