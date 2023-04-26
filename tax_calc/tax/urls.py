from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:var>', views.taxcalc ,name ="taxcalc"),
    path('taxrate',views.taxrate , name='taxrate')
]