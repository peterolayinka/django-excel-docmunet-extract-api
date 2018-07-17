from django.shortcuts import render
from django.http import JsonResponse
from utils import SubjectPricing

# Create your views here.
subject_pricing=SubjectPricing()

def get_state_factor(request, state='lagos'):
    data=subject_pricing.get_state_factor(state)
    return  JsonResponse({'data':data})

def get_all_states_with_vicinities(request):
    data=subject_pricing.get_all_states_with_vicinities()
    return  JsonResponse({'data':data})

def get_state_vicinities(request, state='lagos'):
    data=subject_pricing.get_state_vicinities(state)
    return  JsonResponse({'data':data})

def get_vicinity_factor(request, vicinity='lagos'):
    data=subject_pricing.get_vicinity_factor(vicinity)
    return JsonResponse({'data':data})

def get_all_purposes_and_factors(request):
    data=subject_pricing.get_all_purposes_and_factors()
    return  JsonResponse({'data':data})

def get_purpose_factor(request, purpose):
    new_purpose = purpose.strip().\
                    replace('-', ' ').split(',')
    data=subject_pricing.get_purpose_factor(new_purpose)
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

def get_curriculum_factor(request, curriculum):
    new_curriculum = curriculum.strip().\
                    replace('-', ' ').split(',')
    data=subject_pricing.get_curriculum_factor(new_curriculum)
    return  JsonResponse({'data':data})

def get_all_hours_and_factors(request):
    data=subject_pricing.get_all_hours_and_factors()
    return  JsonResponse({'data':data})
