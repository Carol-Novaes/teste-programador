from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
from django.db import models

from .validators import validar_nota_maxima

class Aluno(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    codigo = models.AutoField(primary_key=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='disciplinas')
    nome = models.CharField(max_length=255)
    carga_horaria = models.IntegerField()
    ano = models.IntegerField()
    professor = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')
    codigo_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='matriculas')
    data_matricula = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo_aluno.nome} - {self.codigo_disciplina.nome}"
    
class Atividade(models.Model):
    id = models.AutoField(primary_key=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='atividades')
    nome = models.CharField(max_length=255)    
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    data_atividade = models.DateField()
     
    def __str__(self):
        return f"{self.nome} - {self.disciplina.nome}"   

class Desempenho(models.Model):
    codigo = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='desempenhos')
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, related_name='desempenhos')
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    def clean(self):
        super().clean()
        validar_nota_maxima(self.atividade, self.nota) 

    def __str__(self):
        return f"{self.aluno.nome} - {self.atividade.nome} ; {self.nota}" 