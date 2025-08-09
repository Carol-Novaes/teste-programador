from django.forms import ValidationError
from rest_framework import serializers
from .models import Aluno, Curso, Disciplina, Matricula, Atividade, Desempenho
from .validators import validar_nota_maxima

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    curso_nome = serializers.CharField(source='curso.nome', read_only=True)
    class Meta:
        model = Disciplina
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = '__all__'

class DesempenhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desempenho
        fields = '__all__'   

    def validate(self, data):
        try:
            validar_nota_maxima(data.get('atividade'), data.get('nota'))
        except ValidationError as e:
            raise serializers.ValidationError({'nota':str(e)})    
        return data                 
