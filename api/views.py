from django.shortcuts import render
from django.http import JsonResponse
from api.models.first_problem import FirstProblem
from api.models.second_problem import SecondProblem

# Create your views here.
def first_problem(request):
    # Get the url query
    user_input = request.GET.get('input', '')
    # Create a new object to work
    first_problem = FirstProblem(user_input)
    # Get the answer of the problem
    result = first_problem.get_answer()
    # Create a JsonResponse object for return it
    response = JsonResponse({'result': result})

    return response

def second_problem(request):
    # Get the url query
    user_input = request.GET.get('input', '')
    # Create a new object to work
    second_problem = SecondProblem(user_input)
    # Get the answer of the problem
    result = second_problem.get_answer()
    # Create a JsonResponse object for return it
    response = JsonResponse({'result': result})

    return response