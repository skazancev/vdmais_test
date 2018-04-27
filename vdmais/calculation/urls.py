from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from . import viewsets


router = DefaultRouter()
router.register('calculate', viewsets.CalcViewSet, base_name='calc')


api_v1_urlpatterns = ([
    path('', include(router.urls))
], 'calculation')


app_name = 'calculation'
urlpatterns = [
    path('', TemplateView.as_view(template_name='calculation/form.html'), name='calc_form'),
]
