
from django.urls import path
from .views import AdminView, UploadProfile, UserView, UpdateUserDetail

urlpatterns = [
    path('user_admin/', AdminView.as_view(), name='Admin_access'),
    path('user_admin/<int:pk>', AdminView.as_view(), name='Admin_access'),
    path('user_detail/', UserView.as_view(), name='User_access'),
    path('update_user_detail/', UpdateUserDetail.as_view(), name='update_user_details'),
    path('upload_profile/', UploadProfile.as_view(), name='upload_user_profile')

]
