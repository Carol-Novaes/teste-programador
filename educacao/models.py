from django.db import models

# Create your models here.
from django.db import models

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
    
