from rest_framework import serializers
from .models import Aluno, Curso, Disciplina, Matricula, Atividade, Desempenho

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
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
        atividade = data.get('atividade')
        nota = data.get('nota')
        
        if nota and atividade:
            if nota > atividade.valor:
                raise serializers.ValidationError(
                    {'nota': f'A nota máxima permitida para esta atividade é {atividade.valor}'}
                )
        return data                 
