from django.urls import path, include

from .views import DeviceLogin
from .views import DeviceMappingsView
from .views import DeviceActivityView

urlpatterns = [
    path('DeviceLogin/<device_auth>/', DeviceLogin.as_view(), name='device_login'),
    path('DeviceIdMappings/', DeviceMappingsView.as_view(), name='get_device_id_mapping_data'),
    path('DeviceActivity/', DeviceActivityView.as_view(), name='get_devuce_activity'),
]
