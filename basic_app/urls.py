from django.urls import path
from . import views
 # TEMPLATE TAGGING

app_name = 'basic_app'

urlpatterns = [
    path('',views.index, name= 'home'),
    path('home/',views.index, name= 'index'),
    path('other/', views.other, name='others-page'),
    path('relative/', views.relative, name='relative-path-page')
]
