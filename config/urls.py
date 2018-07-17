"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('state-factor/<slug:state>/', 
            views.get_state_factor, name='get_state_factor'),
    path('all-states-with-vicinities/', 
            views.get_all_states_with_vicinities, 
            name='get_all_states_with_vicinities'),
    path('state-with-vicinity/<slug:state>/', 
            views.get_state_vicinities, 
            name='get_state_vicinities'),
    path('vicinity-factor/<slug:vicinity>/', 
            views.get_vicinity_factor, 
            name='get_vicinity_factor'),
    path('all-purposes-factors/', 
            views.get_all_purposes_and_factors, 
            name='get_all_purposes_and_factors'),
]
