from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('portfolio.urls')),
    path('admin/', admin.site.urls),
    path('autos/',  include('automotive.urls')),
    path('residential/',  include('residential.urls')),
    path('expense_tracking/',  include('expense_tracking.urls')),
]
