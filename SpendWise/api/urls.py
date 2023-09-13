from django.urls import path
from .views import *

urlpatterns = [
    path("", UserListView.as_view(), name="user-list"),
    path('current-account', CurrentAccountView.as_view(), name='current-account'),
    path('register', UserRegistrationAPIView.as_view(), name='user-registration'),

    path('categories', CatListsView.as_view(), name='categories'),
    path('categories/create', create_category, name='categories-create'),

    path('wallets', user_wallets, name='wallets'),
    path('wallets/<id>', wallet_details, name='wallets-details'),
    path('wallets/<id>/entries', entries_view, name='wallets-entries'),

]