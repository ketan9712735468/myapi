from django.urls import path,include
from .views import firstfunction,CarspecsViewset
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


router=DefaultRouter()
router.register('car-specs',CarspecsViewset, basename='car-specs')

urlpatterns = [
    path('first/',firstfunction),
    path('',include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)