from django.urls import include, path
from rest_framework import routers
from .views import MarcaView, VehiculoView
router = routers.DefaultRouter()
router.register(r'vehiculos', VehiculoView)
router.register(r'marcas', MarcaView)

urlpatterns = [
    path('', include(router.urls)),

]

urlpatterns += router.urls