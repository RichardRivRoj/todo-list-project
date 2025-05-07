from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# Vista para Listar y Crear Tareas
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated] # Solo usuarios autenticados
    
    def get_queryset(self):
        # Filtrar las tareas del usuario actual
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Asign automaticamente el usuario al crear la tarea
        serializer.save(user=self.request.user)
        
# Vista de Detalle, Actualizar y Eliminar Tarea
class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Solo permite acceso a las tareas del usuario
        return Task.objects.filter(user=self.request.user)