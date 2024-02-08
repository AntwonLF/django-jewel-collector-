from django.urls import path
from .views import (
    Home, 
    JewelsList, 
    JewelsDetail, 
    CleaningListCreate, 
    CleaningDetailUpdateDelete, 
    CleaningsOnDateListView,
    CreateUserView,  # Import CreateUserView
    LoginView,       # Import LoginView
    VerifyUserView   # Import VerifyUserView
)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('jewels/', JewelsList.as_view(), name='jewels-list'),
    path('jewels/<int:id>/', JewelsDetail.as_view(), name='jewels-detail'),
    path('jewels/<int:jewel_id>/cleanings/new', CleaningListCreate.as_view(), name='cleaning-create'),
    path('jewels/<int:jewel_id>/cleanings', CleaningListCreate.as_view(), name='cleaning-list'),
    path('jewels/<int:jewel_id>/cleanings/<int:pk>', CleaningDetailUpdateDelete.as_view(), name='cleaning-detail'),
    path('jewels/<int:jewel_id>/cleanings/<int:pk>/update', CleaningDetailUpdateDelete.as_view(), name='cleaning-update'),
    path('jewels/<int:jewel_id>/cleanings/<int:pk>/delete', CleaningDetailUpdateDelete.as_view(), name='cleaning-delete'),
    path('cleanings/on_date/', CleaningsOnDateListView.as_view(), name='cleanings-on-date'),
    
    # New routes for user management
    path('create_user/', CreateUserView.as_view(), name='create-user'),  # Route for creating a new user
    path('login/', LoginView.as_view(), name='login'),  # Route for logging in a user
    path('verify_user/', VerifyUserView.as_view(), name='verify-user'),  # Route for verifying a user's credentials
]
