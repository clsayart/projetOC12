"""OC12EPIC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.views import UserListView, UserRetrieveView
from epic_events.views import CustomerViewSet, ContractViewSet, EventViewSet

customer_router = routers.SimpleRouter()
customer_router.register('customers', CustomerViewSet, basename='customer')

contract_router = routers.SimpleRouter()
contract_router.register('contracts', ContractViewSet, basename='contract')

event_router = routers.SimpleRouter()
event_router.register('events', EventViewSet, basename='event')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/', include(customer_router.urls)),
    path('api/', include(contract_router.urls)),
    path('api/', include(event_router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/refresh/', TokenRefreshView.as_view(), name='refresh'),
]
