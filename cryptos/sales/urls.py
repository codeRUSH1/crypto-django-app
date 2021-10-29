from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from django.contrib import admin
from django.urls import path
from app import views_orders
from app import views
from sales import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/orders/', views_orders.orders),
    path('api/orders/<int:order_id>/', views_orders.order),
    path('landing', views.landing),
    path('convert', views.convert),
    path('', views.index),
    path('register', views.register),
    path('login', views.login_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
