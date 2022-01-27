from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from ..serializers.plant import PlantSerializer
from ..models.plant import Plant
from django.core.exceptions import PermissionDenied

class PlantsView(APIView):
    def post(self, request):
        plant = PlantSerializer(data=request.data)
        if plant.is_valid():
            plant.save()
            return Response(plant.data, status=status.HTTP_201_CREATED)
        else:
            return Response(plant.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self):
        plants = Plant.objects.all()
        data = PlantSerializer(plants, many=True).data
        return Response(data)
