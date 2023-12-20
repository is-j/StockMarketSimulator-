from django.contrib import admin
from django.urls import path, include
from stock.views import CustomLoginView, main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stock.urls')),  # Assuming your app's URLs are configured in stock/urls.py
    path('accounts/login/', CustomLoginView.as_view(template_name='stock/registration/login.html'), name='login'),
    path('accounts/profile/', main_page, name='main_page'),
]
