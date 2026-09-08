from django.contrib import admin
from .models import Proyecto, Tarea

class TareaInline(admin.TabularInline):
    model = Tarea
    extra = 0

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "usuario", "fecha_creacion")
    search_fields = ("nombre", "usuario__username")
    inlines = [TareaInline]

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "proyecto", "estado", "fecha_creacion")
    list_filter = ("estado",)
    search_fields = ("titulo", "proyecto__nombre")