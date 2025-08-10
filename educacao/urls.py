from django.urls import path
from .views import (
    AlunoListCreateAPIView, AlunoDetailAPIView,
    CursoListCreateAPIView, CursoDetailAPIView,
    DisciplinaListCreateAPIView, DisciplinaDetailAPIView,
    MatriculaListCreateAPIView, MatriculaDetailAPIView,
    AtividadeListCreateAPIView, AtividadeDetailAPIView, AtividadesPorAlunoAPIView,
    DesempenhoListCreateAPIView, DesempenhoDetailAPIView,
)

urlpatterns = [
    path('alunos/', AlunoListCreateAPIView.as_view()),
    path('alunos/<int:pk>/', AlunoDetailAPIView.as_view()),

    path('cursos/', CursoListCreateAPIView.as_view()),
    path('cursos/<int:pk>/', CursoDetailAPIView.as_view()),

    path('disciplinas/', DisciplinaListCreateAPIView.as_view()),
    path('disciplinas/<int:pk>/', DisciplinaDetailAPIView.as_view()),

    path('matriculas/', MatriculaListCreateAPIView.as_view()),
    path('matriculas/<int:pk>/', MatriculaDetailAPIView.as_view()),

    path('atividades/', AtividadeListCreateAPIView.as_view()),
    path('atividades/<int:pk>/', AtividadeDetailAPIView.as_view()),
    path('alunos/<int:aluno_id>/atividades/', AtividadesPorAlunoAPIView.as_view()),

    path('desempenhos/', DesempenhoListCreateAPIView.as_view()),
    path('desempenhos/<int:pk>/', DesempenhoDetailAPIView.as_view()),
]
