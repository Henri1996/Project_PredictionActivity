## c'est l'accès qui est permis grae aux endpoints

## definition des endpoints 

from . import views
from django.urls import path

urlpatterns = [
    # path(route, la view to be triggered)
    path('', views.index, name='index'),
    path('petittest/', views.petittest, name = 'petittest'),
    path('predict/', views.predict, name = 'predict')

]