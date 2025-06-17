from django.contrib import admin
from app03.models import Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega

# Inline para Inscripción (Estudiante <-> Curso)
class InscripcionInline(admin.TabularInline):
    model = Inscripcion
    extra = 1
    verbose_name = "Inscripción"
    verbose_name_plural = "Inscripciones"

class EntregaInline(admin.TabularInline):
    model = Entrega
    extra = 1
    verbose_name = "Entrega"
    verbose_name_plural = "Entregas"

class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso', 'fecha_entrega')
    list_filter = ('curso',)
    search_fields = ('titulo',)
    inlines = (EntregaInline,)


class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'departamento', 'instructor')
    list_filter = ('departamento', 'instructor')
    search_fields = ('titulo',)
    inlines = (InscripcionInline,)

admin.site.register(Departamento)
admin.site.register(Instructor)
admin.site.register(Curso, CursoAdmin) 
admin.site.register(Estudiante)
admin.site.register(Inscripcion)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(Entrega)
