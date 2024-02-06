from django.urls import path
# import Home view from the views file
from .views import Home, JewelsList, JewelsDetial



urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('cats/', JewelsList.as_view(), name='cat-list'),
  path('cats/<int:id>/', JewelsDetial.as_view(), name='cat-detail'),
]