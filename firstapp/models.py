from django.db import models

class Carplan(models.Model):
    plan_name = models.CharField(max_length=50)
    year_of_warranty = models.PositiveIntegerField(default=1)
    finanace_plan = models.CharField(max_length=20,default='unavaible')

    def __str__(self):
        return self.plan_name


class Carspecs(models.Model):
    car_plan = models.ForeignKey(Carplan,on_delete=models.SET_NULL,null=True)
    car_brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=50)
    production_year = models.CharField(max_length=10)
    car_body = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=20)
    car_img = models.ImageField(upload_to='Images/',max_length=255,null=True,blank=True)

    def __str__(self):
        return self.car_brand