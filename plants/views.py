from rest_framework import viewsets
from .serializers import PlantSerializer
from .models import Plant
from rest_framework.permissions import IsAuthenticated   ##from simplejwt we have added this so that authentication is required for all views
from rest_framework.response import Response
from rest_framework import status


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated]   ##Ensure that only authenticated users can access the views

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
