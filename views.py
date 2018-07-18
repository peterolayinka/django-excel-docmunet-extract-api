import json 

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils import SubjectPricing

# Create your views here.
subject_pricing=SubjectPricing()

def get_state_factor(request, state='lagos'):
    new_state = state.strip().\
                    replace('-', ' ')
    data=subject_pricing.get_state_factor(new_state)
    return  JsonResponse({'data':data})

def get_all_states_with_vicinities(request):
    data=subject_pricing.get_all_states_with_vicinities()
    return  JsonResponse({'data':data})

def get_state_vicinities(request, state='lagos'):
    new_state = state.strip().\
                    replace('-', ' ')
    data=subject_pricing.get_state_vicinities(new_state)
    return  JsonResponse({'data':data})

def get_vicinity_factor(request, vicinity='lagos'):
    new_vicinity = vicinity.strip().\
                    replace('-', ' ')
    data=subject_pricing.get_vicinity_factor(vicinity)
    return JsonResponse({'data':data})

def get_all_purposes_and_factors(request):
    data=subject_pricing.get_all_purposes_and_factors()
    return  JsonResponse({'data':data})

def get_purpose_factor(request, purpose=None):
    if purpose:
        purpose = purpose.strip().\
                    replace('-', ' ').split(',')
    data=subject_pricing.get_purpose_factor(purpose)
    return  JsonResponse({'data':data})

def get_all_subjects_and_their_prices(request):
    data=subject_pricing.get_all_subjects_and_their_prices()
    return  JsonResponse({'data':data})

def get_subject_price(request, subject):
    new_subject = subject.strip().replace('-', ' ')
    data=subject_pricing.get_subject_price(new_subject)
    return  JsonResponse({'data':data})

def get_all_curriculums_and_factors(request):
    data=subject_pricing.get_all_curriculums_and_factors()
    return  JsonResponse({'data':data})

def get_curriculum_factor(request, curriculum="Not Sure"):
    new_curriculum = curriculum.strip().\
                        replace('-', ' ').split(',')
    data=subject_pricing.get_curriculum_factor(new_curriculum)
    return  JsonResponse({'data':data})

def get_all_hours_and_factors(request):
    data=subject_pricing.get_all_hours_and_factors()
    return  JsonResponse({'data':data})

def get_hour_factor(request, hour=1):
    data=subject_pricing.get_hour_factor(hour)
    return  JsonResponse({'data':data})

def get_purpose_curriculum_relation(request):
    data=subject_pricing.get_purpose_curriculum_relation()
    return  JsonResponse({'data':data})

def get_marketing_channels(request):
    data=subject_pricing.get_marketing_channels()
    return  JsonResponse({'data':data})

@csrf_exempt
def get_hourly_price_and_transport(request):
    json_data = json.loads(request.body)
    try:
        data=subject_pricing.get_hourly_price_and_transport(
            students=json_data.get('students'), state=json_data.get('state', 'Lagos'), 
            vicinity=json_data.get('vicinity'), curriculums=json_data.get('curriculums'),
            no_of_hours=json_data.get('no_of_hours', 1),
            subject=json_data.get('subject', "home tutoring")
        )
    except:
        data=None
    return  JsonResponse({'data':data})

