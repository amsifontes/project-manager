from django.db import models

# USER MODELS

class Architect(models.Model):
    # id(pk)
    username = models.CharField(
        max_length=100,
        # unique=True,
    )
    # fist_name
    # last_name
    email = models.EmailField(
        max_length=100,
    )

    def __str__(self):
        return self.username

class Client(models.Model):
    # id(pk)
    username = models.CharField(
        max_length=100,
        # unique=True,
    )
    email = models.EmailField(
        max_length=100,
        # unique=True,
    )

    def __str__(self):
        return self.username

# PROJECT MODELS


class Project(models.Model):
    # id(pk)
    architect_username = models.ForeignKey(
        Architect,
        on_delete=models.CASCADE,
        # default="unassigned"
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE) # consider SET_NULL, requires field be nullable, to keep Project is Client is deleted
    name_proj = models.CharField( # consider SlugField for use in shareable URL
        max_length=100,
        default="Unnamed Project"
    )
    address = models.CharField(
        max_length=200,
    )
    start_date = models.DateField()
    end_date = models.DateField()

    # def __str__(self):
    #     return self.name


class Phase(models.Model):
    # id(pk)
    project_id = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )
    name_phase = models.CharField(
        max_length=100,
        default="Unnamed Phase"
    )
    start_date = models.DateField()
    end_date = models.DateField()

    # def __str__(self):
    #     return self.name

class Task(models.Model):
    # id(pk)
    project_id = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )
    phase_id = models.ForeignKey(
        Phase,
        on_delete=models.CASCADE,
    )
    name_task = models.CharField(
        max_length=100,
        default="Unnamed Task",
    )
    start_date = models.DateField()
    end_date = models.DateField()

    # def __str__(self):
    #     return self.name
