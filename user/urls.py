
from django.urls import path
from .views import AdminView, UploadProfile

urlpatterns = [
    path('', AdminView.as_view(), name='Admin_access'),
    path('<int:pk>', AdminView.as_view(), name='Admin_access'),
    path('upload_profile/', UploadProfile.as_view(), name='upload_user_profile')

]
