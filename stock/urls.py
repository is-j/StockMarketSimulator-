from django.conf import settings
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import main_page

app_name = 'stock'

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('stocks/', views.stock_list, name='stock_list'),
    path('stocks/import/', views.stock_detail, name='stock_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='stock/registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='stock/templates/registration/password_change_form.html'), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('accounts/profile/', main_page, name='main_page'),

   # path('login/', )
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
