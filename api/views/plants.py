from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from ..serializers.plant import PlantSerializer
from ..models.plant import Plant
from django.core.exceptions import PermissionDenied

class PlantsView(APIView):
    def post(self, request):
        request.data['owner'] = request.user.id
        plant = PlantSerializer(data=request.data)
        if plant.is_valid():
            plant.save()
            return Response(plant.data, status=status.HTTP_201_CREATED)
        else:
            return Response(plant.errors, status=status.HTTP_404_BAD_REQUEST)
    
    def get(self, request):
        plants = Plant.objects.filter(owner=request.user.id)
        data = Plant(plants, many=True).data
        return Response(data)
