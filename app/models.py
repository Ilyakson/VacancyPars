from django.db import models


class Options(models.Model):
    country = models.CharField(max_length=255)
    position = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=25, default='New')


class VacancyLink(models.Model):
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=250, unique=True)
    status = models.CharField(max_length=25, default='New')


class Vacancy(models.Model):
    employer = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_publication = models.CharField(max_length=255)
    link = models.CharField(max_length=250, unique=True)
