from django.contrib import admin
from django.urls import path, include
from monitor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),  # Includes login/logout/password views
    path('add-credential/', views.add_credential, name='add_credential'),
    path('check/', views.check_credential, name='check_credential'),
    path('delete/<int:pk>/', views.delete_credential, name='delete_credential'),
]
