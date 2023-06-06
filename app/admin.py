from django.contrib import admin

from app.models import Settings, Info


@admin.register(Settings)
class SettingAdmin(admin.ModelAdmin):
    list_display = ["country", "position"]


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ["company_name", "vacancy_name", "position", "date_publication"]
