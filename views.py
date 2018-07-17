from django.shortcuts import render
from django.http import JsonResponse
from utils import SubjectPricing

# Create your views here.
subject=SubjectPricing()

def get_state_factor(request, state='lagos'):
    data=subject.get_state_factor(state)
    return  JsonResponse({'fator':data})

def get_all_states_with_vicinities(request):
    data=subject.get_all_states_with_vicinities()
    return  JsonResponse({'data':data})

def get_state_vicinities(request, state='lagos'):
    data=subject.get_state_vicinities(state)
    return  JsonResponse({'data':data})

def get_vicinity_factor(request, vicinity='lagos'):
    data=subject.get_vicinity_factor(vicinity)
    return JsonResponse({"vicinity":data})

def get_all_purposes_and_factors(request):
    data=subject.get_all_purposes_and_factors()
    return  JsonResponse({'data':data})
