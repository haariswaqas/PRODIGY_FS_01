from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from api import views

urlpatterns = [
    path("token/", views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", views.RegisterView.as_view(), name='register'),
    path("profile/", views.ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),
    path("notes/", views.note_list, name="note_list"),
    path("notes/<int:pk>/", views.note_detail, name="note_detail")
]
