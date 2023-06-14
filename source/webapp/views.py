# from unittest import result

from django.shortcuts import render
import math


def calculator(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        value_add = None
        value_sub = None
        value_mul = None
        value_div = None
        if request.POST.get('operation') == 'add':
            value_add = int(request.POST.get('fn')) + int(request.POST.get('sn'))
        elif request.POST.get('operation') == 'sub':
            value_sub = int(request.POST.get('fn')) - int(request.POST.get('sn'))
        elif request.POST.get('operation') == 'mul':
            value_mul = int(request.POST.get('fn')) * int(request.POST.get('sn'))
        elif request.POST.get('operation') == 'div':
            value_div = int(request.POST.get('fn')) // int(request.POST.get('sn'))
        context = {
            'first_num': request.POST.get('fn'),
            'second_num': request.POST.get('sn'),
            'value_add': value_add,
            'value_sub': value_sub,
            'value_mul': value_mul,
            'value_div': value_div
        }
        return render(request, 'index.html', context)