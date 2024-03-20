from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.models import User
from lespays.views import Classeviewset,Eleveviewset
from rest_framework import routers
from lespays.models import Classe,Eleve

router = routers.DefaultRouter()
router.register('Classe', Classeviewset)
router.register('Eleve', Eleveviewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lespays.urls')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]
