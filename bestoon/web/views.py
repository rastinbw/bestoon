from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import JSONEncoder
from web.models import User, Token, Expense, Income
from datetime import datetime

# Create your views here.
@csrf_exempt
def submit_expense(request):
    """ User submits an expense"""
    #TODO: validate data, token might be fake ...

    print(request.POST) #prints it in the console

    current_token = request.POST['token']
    current_user = User.objects.filter(token__token = current_token).get()

    if('date' not in request.POST):
        date = datetime.now()
    else:
        date = request.POST['date']
        
    Expense.objects.create(
        user = current_user, 
        amount = request.POST['amount'], 
        description = request.POST['description'],
        date = date) 

    return JsonResponse({
        'status':'ok'
    },encoder=JSONEncoder)