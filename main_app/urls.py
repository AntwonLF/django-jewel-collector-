from django.urls import path
# import Home view from the views file
from django.urls import path
from .views import Home, JewelsList, JewelsDetail, CleaningListCreate, CleaningDetailUpdateDelete, CleaningsOnDateListView



urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('Jewels/', JewelsList.as_view(), name='Jewels-list'),
  path('Jewels/<int:id>/', JewelsDetail.as_view(), name='Jewels-detail'),

  # CRUD
 path('jewels/<int:jewel_id>/cleanings/new', CleaningListCreate.as_view(), name='cleaning-create'),  # For creating a new Cleaning
 path('jewels/<int:jewel_id>/cleanings', CleaningListCreate.as_view(), name='cleaning-list'),  # For listing all Cleanings of a Jewel
 path('jewels/<int:jewel_id>/cleanings/<int:pk>', CleaningDetailUpdateDelete.as_view(), name='cleaning-detail'),  # For viewing a specific Cleaning
 path('jewels/<int:jewel_id>/cleanings/<int:pk>/update', CleaningDetailUpdateDelete.as_view(), name='cleaning-update'),  # For updating a specific Cleaning
path('jewels/<int:jewel_id>/cleanings/<int:pk>/delete', CleaningDetailUpdateDelete.as_view(), name='cleaning-delete'),  
path('cleanings/on_date/', CleaningsOnDateListView.as_view(), name='cleanings-on-date'),

]