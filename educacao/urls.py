from django.urls import path
from .views import (
    AlunoListCreateAPIView, AlunoDetailAPIView,
    CursoListCreateAPIView, CursoDetailAPIView,
    DisciplinaListCreateAPIView, DisciplinaDetailAPIView,
    MatriculaListCreateAPIView, MatriculaDetailAPIView,
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
]
