
from django.urls import path
from .views import AdminView

urlpatterns = [
    path('', AdminView.as_view(), name='Admin_access'),
    path('<int:pk>', AdminView.as_view(), name='Admin_access')

]
