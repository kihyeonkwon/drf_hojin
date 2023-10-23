from django.urls import path
# from . import views
from .views import UserView, FollowView, UserDetailView


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', UserView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('follow/<int:user_id>/', FollowView.as_view(), name='follow'),
    path('profile/<int:user_id>/', UserDetailView.as_view(), name='profile')
]

