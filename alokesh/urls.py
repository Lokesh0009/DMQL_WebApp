from django.urls import path
from .views import table_names_view, table_data_view

urlpatterns = [
   
    path('', table_names_view, name='table_names'),
    path('<str:table_name>/', table_data_view, name='table_data'),
    
]