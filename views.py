from django.shortcuts import render
from django.http import JsonResponse
from utils import SubjectPricing

# Create your views here.
subject=SubjectPricing()

def get_state_factor(request, state='lagos'):
    data=subject.get_state_factor(state)
    return  JsonResponse({data})

def get_all_states_with_vicinities(request):
    data=subject.get_all_states_with_vicinities()
    return  JsonResponse({data})

def get_state_vicinities(request, state='lagos'):
    data=subject.get_state_vicinities(state)
    return  JsonResponse({data})

def get_vicinity_factor(request, vicinity='lagos'):
    data=subject.get_vicinity_factor(vicinity)
    return JsonResponse({data})

def get_all_purposes_and_factors(request):
    data=subject.get_all_purposes_and_factors()
    return  JsonResponse({data})

def get_purpose_factor(request, purpose=[]):
    new_purpose = purpose.strip().\
                    replace('-', ' ').split(',')
    data=subject.get_purpose_factor(new_purpose)
    return  JsonResponse({data})
