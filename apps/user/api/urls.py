from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.user.api.v1.urls'))
]
