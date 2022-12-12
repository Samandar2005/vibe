from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.worker.api.v1.urls'))
]
