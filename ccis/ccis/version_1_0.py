from django.urls import path, include

urlpatterns = [
    path('index/', include('user.urls')),
]
