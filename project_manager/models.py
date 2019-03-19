from django.db import models
from django.contrib.auth.models import User


# TODO: add `created` and `updated` fields to models

# USER MODELS

class Architect(models.Model):
    # id(pk)
    username = models.CharField(
        max_length=100,
        # unique=True,
    )
    # first_name
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
    architects = models.ManyToManyField(
        User,
        related_name="architects",
    )
    clients = models.ManyToManyField(
        User,
        related_name="clients",
    )
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
    #     return self.name_proj


class Phase(models.Model):
    # id(pk)
    project = models.ForeignKey(
        Project,
        related_name='phases',
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
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )
    phase = models.ForeignKey(
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
