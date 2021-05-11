from rest_framework.views import APIView
from .serializers import CarsSerializer
from cars.models import Cars
from rest_framework.response import Response

class CarsAPIView(APIView):
    serializer_class=CarsSerializer

    def get_queryset(self):
        cars=Cars.objects.all()
        return cars

    def get(self,request,*args,**kwargs):
        cars = self.get_queryset()
        serializer = CarsSerializer(cars,many=True)

        return Response(serializer.data)