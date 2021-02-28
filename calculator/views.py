from django.shortcuts import render, redirect
from django.http import HttpResponse
from quality_points.models import *
from .models import *

# Create your views here.


def caculate(request):
    if request.method == "POST":
        ch_1 = request.POST.get('ch_1')
        num_1 = request.POST.get('num_1')
    # for other subjects
        ch_2 = request.POST.get('ch_2')
        num_2 = request.POST.get('num_2')
    # for other subjects
        ch_3 = request.POST.get('ch_3')
        num_3 = request.POST.get('num_3')
    # for other subjects
        ch_4 = request.POST.get('ch_4')
        num_4 = request.POST.get('num_4')
    # for other subjects
        ch_5 = request.POST.get('ch_5')
        num_5 = request.POST.get('num_5')
    # for other subjects
        ch_6 = request.POST.get('ch_6')
        num_6 = request.POST.get('num_6')


    # for subject number 1
    highest_mark = HighestNumber.objects.get(belongs_to=ch_1)
    if int(num_1) > highest_mark.highest:
        num_1 = highest_mark.highest
    numbers_1 = Number.objects.get(credit_hour=ch_1, number=num_1)
    points_1 = Point.objects.get(numbers=numbers_1)

    # for subject number 2
    highest_mark = HighestNumber.objects.get(belongs_to=ch_2)
    if int(num_2) > highest_mark.highest:
        num_2 = highest_mark.highest
    numbers_2 = Number.objects.get(credit_hour=ch_2, number=num_2)
    points_2 = Point.objects.get(numbers=numbers_2)


    # for subject number 3
    highest_mark = HighestNumber.objects.get(belongs_to=ch_3)
    if int(num_3) > highest_mark.highest:
        num_3 = highest_mark.highest
    numbers_3 = Number.objects.get(credit_hour=ch_3, number=num_3)
    points_3 = Point.objects.get(numbers=numbers_3)


    # for subject number 4
    highest_mark = HighestNumber.objects.get(belongs_to=ch_4)
    if int(num_4) > highest_mark.highest:
        num_4 = highest_mark.highest
    numbers_4 = Number.objects.get(credit_hour=ch_4, number=num_4)
    points_4 = Point.objects.get(numbers=numbers_4)


    # for subject number 5
    highest_mark = HighestNumber.objects.get(belongs_to=ch_5)
    if int(num_5) > highest_mark.highest:
        num_5 = highest_mark.highest
    numbers_5 = Number.objects.get(credit_hour=ch_5, number=num_5)
    points_5 = Point.objects.get(numbers=numbers_5)
    
    # for subject number 6
    highest_mark = HighestNumber.objects.get(belongs_to=ch_6)
    if int(num_6) > highest_mark.highest:
        num_6 = highest_mark.highest
    numbers_6 = Number.objects.get(credit_hour=ch_6, number=num_6)
    points_6 = Point.objects.get(numbers=numbers_6)





    total_credit_hours = int(ch_1) + int(ch_2) + int(ch_3) + int(ch_4) + int(ch_5) + int(ch_6)
    total_quality_points = points_1.points + points_2.points + points_3.points + points_4.points + points_5.points + points_6.points
    Gpa = total_quality_points / total_credit_hours



    return render(request, 'success.html', {'gpa': Gpa})

def success_msg(request):
    return HttpResponse("success")

