from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.video.api.v1.urls'))
]
