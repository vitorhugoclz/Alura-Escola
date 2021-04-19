from django.contrib import admin
from escola.models import Aluno, Curso

# Register your models here.

class Alunos(admin.ModelAdmin):
  list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
  list_display_link = ('id', 'nome')
  search_fields = ('nome',)
  list_per_page = 20

class Cursos(admin.ModelAdmin):
  list_display = ('id', 'codigo_curso', 'descricao')
  list_display_link = ('id', 'codigo_curso')
  search_fields = ('codigo_curso',)
  list_per_page = 20

admin.site.register(Aluno, Alunos)
admin.site.register(Curso, Cursos)