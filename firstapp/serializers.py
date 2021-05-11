from rest_framework import serializers
from .models import Carspecs

class CarspecsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carspecs
        fields=['id','car_brand','car_model','production_year','car_body','engine_type','car_img']
        # depth = 1