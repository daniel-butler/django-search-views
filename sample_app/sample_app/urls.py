from django.urls import path
from django.contrib import admin
from actors.views import ActorsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ActorsView.as_view(), name="actors"),
]
