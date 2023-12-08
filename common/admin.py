from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position')
    list_display_links = ('id', 'full_name')

    def has_add_permission(self, request):
        if models.Workflow.objects.all().count() >= 4:
            return False
        return True


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

    def has_add_permission(self, request):
        if models.About.objects.all().exists():
            return False
        return True


@admin.register(models.Workflow)
class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'icon')
    list_display_links = ('id', 'title')

    def has_add_permission(self, request):
        if models.Workflow.objects.all().count() >= 3:
            return False
        return True


@admin.register(models.Status)
class salom(admin.ModelAdmin):

    def has_add_permission(self, request): return False

    def has_delete_permission(self, request, obj=None): return False

    def has_change_permission(self, request, obj=None): return False
