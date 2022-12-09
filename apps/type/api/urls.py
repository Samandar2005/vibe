from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.type.api.v1.urls'))
]
