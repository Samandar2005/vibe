from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.customer.api.v1.urls'))
]
