from django.contrib import admin

from app.models import Options, Vacancy, VacancyLink


@admin.register(Options)
class OptionsAdmin(admin.ModelAdmin):
    list_display = ["country", "position", "status"]


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ["employer", "title", "description", "date_publication", "link"]


@admin.register(VacancyLink)
class VacancyLinkAdmin(admin.ModelAdmin):
    list_display = ["name", "link", "status"]
