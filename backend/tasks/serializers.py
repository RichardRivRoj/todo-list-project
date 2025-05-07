from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    # Campo personalizado
    user_email = serializers.EmailField(source="user.email", read_only=True)
    
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "completed",
            "created_at",
            "user",
            "user_email" # Campo personalizado
        ]
        read_only_fields = [
            'id',
            'created_at',
            'user'
        ] # No se modifican Via API
        
        def validate_title(self, value):
            if len(value.strip()) < 5:
                raise serializers.ValidationError("El titulo debe al menos tener 5 caracteres.")
            return value