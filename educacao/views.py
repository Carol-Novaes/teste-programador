from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Aluno, Curso, Disciplina, Matricula
from .serializers import AlunoSerializer, CursoSerializer, DisciplinaSerializer, MatriculaSerializer

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
