from random import sample

from django.shortcuts import render
from django.http import HttpResponse

# def show_index(request):
#     fruits = [
#         'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
#         'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
#     ]
#     return render(request, 'index.html', {'fruits': sample(fruits, 3.虚拟DOM的两种创建方式)})

def show_index(request):
        fruits = [
           'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
           'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
        ]
        selected_fruits = sample(fruits, 3)
        return render(request, 'index.html', {'fruits': selected_fruits})