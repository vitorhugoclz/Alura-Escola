from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaAlunoSerializer
from escola.serializer import ListaAlunosMatriculadosCursoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class AlunosViewSet(viewsets.ModelViewSet):
  """Exibindo todos os alunos"""
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
  """Exibindo todos os cursos"""
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]


class MatriculaViewSet(viewsets.ModelViewSet):
  """Listando todas as matrículas"""

  queryset = Matricula.objects.all()
  serializer_class = MatriculaSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
  """Listando as matrículas de um aluno"""
  
  def get_queryset(self):
    queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListaMatriculaAlunoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]


class ListaAlunosMatriculados(generics.ListAPIView):
  """Listando alunos matriculados em um curso"""
  def get_queryset(self):
    queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListaAlunosMatriculadosCursoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
