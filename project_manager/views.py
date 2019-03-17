from django.shortcuts import render
from django import forms

from .models import Architect, Client, Project, Phase

architects = Architect.objects.all()
print(architects)
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
    architect_username = forms.ChoiceField(
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
    


# >>> CHOICES = (('1', 'First',), ('2', 'Second',))
# >>> choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
# >>> choice_field.choices
# [('1', 'First'), ('2', 'Second')]
# >>> choice_field.widget.choices
# [('1', 'First'), ('2', 'Second')]
# >>> choice_field.widget.choices = ()
# >>> choice_field.choices = (('1', 'First and only',),)
# >>> choice_field.widget.choices
# [('1', 'First and only')]


# BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
# FAVORITE_COLORS_CHOICES = (
#     ('blue', 'Blue'),
#     ('green', 'Green'),
#     ('black', 'Black'),
# )


# class SimpleForm(forms.Form):
#     birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
#     favorite_colors = forms.MultipleChoiceField(
#         required=False,
#         widget=forms.CheckboxSelectMultiple,
#         choices=FAVORITE_COLORS_CHOICES,
#     )

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
            Project.objects.create(
                architect_username = form.cleaned_data['architect_username'],
                client = form.cleaned_data['client'],
                name_proj = form.cleaned_data['name_proj'],
                address = form.cleaned_data['address'],
                start_date = form.cleaned_data['start_date'],
                end_date = form.cleaned_data['end_date'],
            )
            messages.warning(request, "New Project Created")
            return redirect('/hey/')
    else:
        form = ProjectForm()
    
    context = {
        'form': form,
    }
    # TODO: create html file create-project.html
    return render(request, 'pages/create-project.html', context)


def update_project(request):
    pass

def create_phase(request):
    pass

def update_phase(request):
    pass