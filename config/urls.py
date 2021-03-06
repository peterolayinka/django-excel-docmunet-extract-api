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
            views.get_state_factor, 
            name='get_state_factor'),
    path('all-state-with-vicinity/', 
            views.get_all_states_with_vicinities, 
            name='all_state_with_vicinity'),
    path('state-with-vicinity/<slug:state>/', 
            views.get_state_vicinities, 
            name='state_with_vicinities'),
    path('vicinity-factor/<slug:vicinity>/', 
            views.get_vicinity_factor, 
            name='vicinity_factor'),
    path('all-purpose-factor/', 
            views.get_all_purposes_and_factors, 
            name='all_purpose_and_factor'),
    path('purpose-factor/<purpose>/', 
            views.get_purpose_factor, 
            name='purpose_and_factor'),
    path('purpose-factor/', 
            views.get_purpose_factor, 
            name='default_purpose_and_factor'),
    path('all-subject-price/', 
            views.get_all_subjects_and_their_prices, 
            name='all_subject_price'),
    path('subject-price/<subject>/', 
            views.get_subject_price, 
            name='subject_price'),
    path('all-curriculum-factor/', 
            views.get_all_curriculums_and_factors, 
            name='all_curriculum_factor'),
    path('curriculum-factor/<curriculum>/', 
            views.get_curriculum_factor, 
            name='curriculum_factor'),
    path('curriculum-factor/', 
            views.get_curriculum_factor, 
            name='default_curriculum_factor'),
    path('all-hour-factor/', 
            views.get_all_hours_and_factors, 
            name='all_hour_factor'),
    path('hour-factor/<hour>/', 
            views.get_hour_factor, 
            name='hour_factor'),
    path('hour-factor/', 
            views.get_hour_factor, 
            name='default_hour_factor'),
    path('purpose-curriculum-relation/<curriculum>/', 
            views.get_purpose_curriculum_relation, 
            name='purpose_curriculum_relation'),
    path('marketing-channel/', 
            views.get_marketing_channels, 
            name='marketing_channel'),
    path('hourly-price/', 
            views.get_hourly_price_and_transport, 
            name='hourly_price'),
]
