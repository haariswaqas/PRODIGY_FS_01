from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from api import views

urlpatterns = [
    path("token/", views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", views.RegisterView.as_view(), name='register'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("profile/", views.ProfileView.as_view(), name='profile'),
    path("profile_info/", views.profile_info, name='profile_info'),
    path("create_profile/", views.create_profile, name='create_profile'),
    path('profile/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('lecturer/', views.lecturer_list, name='lecturer_list'),
    path('lecturer/<int:pk>/', views.lecturer_detail, name='lecturer_detail'),
    path('course/', views.course_list, name='course_list'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path("notes/", views.note_list, name="note_list"),
    path("notes/<int:pk>/", views.note_detail, name="note_detail")
]
