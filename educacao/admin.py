from django.contrib import admin
from .models import Aluno, Curso, Disciplina, Matricula, Atividade, Desempenho

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Atividade)
admin.site.register(Desempenho)