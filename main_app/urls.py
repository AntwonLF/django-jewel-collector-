from django.urls import path
# import Home view from the views file
from .views import Home, JewelsList, JewelsDetial



urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('Jewels/', JewelsList.as_view(), name='Jewels-list'),
  path('Jewels/<int:id>/', JewelsDetial.as_view(), name='Jewels-detail'),
]