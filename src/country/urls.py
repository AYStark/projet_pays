from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.models import User
from lespays.views import Continentviewset,Paysviewset
from rest_framework import routers
from lespays.models import Continent,Pays

router = routers.DefaultRouter()
router.register('Continent', Continentviewset)
router.register('Pays', Paysviewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lespays.urls')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]
