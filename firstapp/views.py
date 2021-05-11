from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets
from .models import Carspecs
from .serializers import CarspecsSerializer


@api_view()
@permission_classes([AllowAny])
def firstfunction(request):
    print(request.query_params)
    print(request.query_params['id'])
    print(request.query_params['key'])
    name1=request.query_params['id']
    name= int(name1) * 2
    return Response({"mesaage":'how are you'})

class CarspecsViewset(viewsets.ModelViewSet):
    queryset= Carspecs.objects.all()
    serializer_class=CarspecsSerializer

    # def retrieve(self,request,*args,**kwargs):
    #       =kwargs
    #     print(params['pk'])
    #     params_list=params['pk'].split('-')
    #     cars = Carspecs.objects.filter(car_brand=params_list[0],car_model=params_list[1])
    #     serializer=CarspecsSerializer(cars,many=True)
    #     return Response(serializer.data)

    def create(self,request,*args,**kwargs):
        car_data=request.data

        new_car=Carspecs.objects.create(car_brand=car_data['car_brand'],car_model=car_data['car_model'],
                    production_year=car_data['production_year'],car_body=car_data['car_body'],
                    engine_type=car_data['engine_type'],car_img=car_data['car_img'])

        new_car=Carspecs.objects.create(car_plan=Carplan.objects.get(id=car_data['car_plan']),car_brand=car_data['car_brand'],car_model=car_data['car_model'],
                    production_year=car_data['production_year'],car_body=car_data['car_body'],
                    engine_type=car_data['engine_type'],car_img=car_data['car_img'])

        new_car.save()
        serializer = CarspecsSerializer(new_car)
        return Response(serializer.data)

    # def destroy(self,request,*args,**kwargs):
    #     logedin_user = request.user
    #     if(logedin_user == 'admin'):
    #         car=self.get_object()
    #         car.delete()
    #         response_message={'message':'Item has been deleted'}
    #     else:
    #         response_message={'message':'Not Allow'}
    #     return Response(response_message)

