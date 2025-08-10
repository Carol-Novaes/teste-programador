from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Aluno, Curso, Disciplina, Matricula, Atividade, Desempenho
from .serializers import AlunoSerializer, CursoSerializer, DisciplinaSerializer, MatriculaSerializer, AtividadeSerializer, DesempenhoSerializer

# ----------- ALUNO ----------------
class AlunoListCreateAPIView(APIView):
    def get(self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlunoDetailAPIView(APIView):
    def get(self, request, pk):
        aluno = get_object_or_404(Aluno, pk=pk)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)

    def put(self, request, pk):
        aluno = get_object_or_404(Aluno, pk=pk)
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        aluno = get_object_or_404(Aluno, pk=pk)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------- CURSO ----------------
class CursoListCreateAPIView(APIView):
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CursoDetailAPIView(APIView):
    def get(self, request, pk):
        curso = get_object_or_404(Curso, pk=pk)
        serializer = CursoSerializer(curso)
        return Response(serializer.data)

    def put(self, request, pk):
        curso = get_object_or_404(Curso, pk=pk)
        serializer = CursoSerializer(curso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        curso = get_object_or_404(Curso, pk=pk)
        curso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------- DISCIPLINA ----------------
class DisciplinaListCreateAPIView(APIView):
    def get(self, request):
        disciplinas = Disciplina.objects.all()
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DisciplinaDetailAPIView(APIView):
    def get(self, request, pk):
        disciplina = get_object_or_404(Disciplina, pk=pk)
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data)

    def put(self, request, pk):
        disciplina = get_object_or_404(Disciplina, pk=pk)
        serializer = DisciplinaSerializer(disciplina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        disciplina = get_object_or_404(Disciplina, pk=pk)
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------- MATRICULA ----------------
class MatriculaListCreateAPIView(APIView):
    def get(self, request):
        matriculas = Matricula.objects.all()
        serializer = MatriculaSerializer(matriculas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MatriculaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MatriculaDetailAPIView(APIView):
    def get(self, request, pk):
        matricula = get_object_or_404(Matricula, pk=pk)
        serializer = MatriculaSerializer(matricula)
        return Response(serializer.data)

    def put(self, request, pk):
        matricula = get_object_or_404(Matricula, pk=pk)
        serializer = MatriculaSerializer(matricula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        matricula = get_object_or_404(Matricula, pk=pk)
        matricula.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# ----------- ATIVIDADE ----------------    
class AtividadeListCreateAPIView(APIView):
    def get(self, request):
        atividades = Atividade.objects.all()
        serializer = AtividadeSerializer(atividades, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AtividadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AtividadeDetailAPIView(APIView):
    def get(self, request, pk):
        atividade = get_object_or_404(Atividade, pk=pk)
        serializer = AtividadeSerializer(atividade)
        return Response(serializer.data)

    def put(self, request, pk):
        atividade = get_object_or_404(Atividade, pk=pk)
        serializer = AtividadeSerializer(atividade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        atividade = get_object_or_404(Atividade, pk=pk)
        atividade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AtividadesPorAlunoAPIView(APIView):
    def get(self, request, aluno_id):
        try:
            aluno = get_object_or_404(Aluno, pk=aluno_id)            
            matriculas = Matricula.objects.filter(codigo_aluno=aluno)
            disciplinas_ids = [m.codigo_disciplina_id for m in matriculas]            
            atividades = Atividade.objects.filter(disciplina_id__in=disciplinas_ids)            
            serializer = AtividadeSerializer(atividades, many=True)            
            return Response(serializer.data)            
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_400_BAD_REQUEST)    

# ----------- DESEMPENHO ----------------
class DesempenhoListCreateAPIView(APIView):
    def get(self, request):
        desempenhos = Desempenho.objects.all()
        serializer = DesempenhoSerializer(desempenhos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DesempenhoSerializer(data=request.data)
        if serializer.is_valid():
            aluno = serializer.validated_data['aluno']
            atividade = serializer.validated_data['atividade']

            if Desempenho.objects.filter(aluno=aluno, atividade=atividade).exists():
                return Response({'error': 'Já existe uma nota registrada para este aluno(a) nesta atividade!'}, status=status.HTTP_400_BAD_REQUEST)
            
            if not Matricula.objects.filter(codigo_aluno=aluno, codigo_disciplina=atividade.disciplina).exists():
                return Response({'error': 'O aluno não está matriculado na disciplina desta atividade!'}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DesempenhoDetailAPIView(APIView):
    def get(self, request, pk):
        desempenho = get_object_or_404(Desempenho, pk=pk)
        serializer = DesempenhoSerializer(desempenho)
        return Response(serializer.data)

    def put(self, request, pk):
        desempenho = get_object_or_404(Desempenho, pk=pk)
        serializer = DesempenhoSerializer(desempenho, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        desempenho = get_object_or_404(Desempenho, pk=pk)
        desempenho.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)