from django.shortcuts import render, redirect
from django.http import HttpResponse
from quality_points.models import *


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
    points_1 = Point.objects.get(cre_hr=ch_1, numbers=num_1)




    # for subject number 2
    highest_mark = HighestNumber.objects.get(belongs_to=ch_2)
    if int(num_2) > highest_mark.highest:
        num_2 = highest_mark.highest
    points_2 = Point.objects.get(cre_hr=ch_2, numbers=num_2)


    # for subject number 3
    highest_mark = HighestNumber.objects.get(belongs_to=ch_3)
    if int(num_3) > highest_mark.highest:
        num_3 = highest_mark.highest
    points_3 = Point.objects.get(cre_hr=ch_3, numbers=num_3)


    # for subject number 4
    highest_mark = HighestNumber.objects.get(belongs_to=ch_4)
    if int(num_4) > highest_mark.highest:
        num_4 = highest_mark.highest
    points_4 = Point.objects.get(cre_hr=ch_4, numbers=num_4)


    # for subject number 5
    highest_mark = HighestNumber.objects.get(belongs_to=ch_5)
    if int(num_5) > highest_mark.highest:
        num_5 = highest_mark.highest
    points_5 = Point.objects.get(cre_hr=ch_5 ,numbers=num_5)
    
    # for subject number 6
    highest_mark = HighestNumber.objects.get(belongs_to=ch_6)
    if int(num_6) > highest_mark.highest:
        num_6 = highest_mark.highest
    points_6 = Point.objects.get(cre_hr=ch_6, numbers=num_6)





    total_credit_hours = int(ch_1) + int(ch_2) + int(ch_3) + int(ch_4) + int(ch_5) + int(ch_6)
    total_quality_points = points_1.points + points_2.points + points_3.points + points_4.points + points_5.points + points_6.points
    Gpa = total_quality_points / total_credit_hours




    return render(request, 'success.html', {'gpa': Gpa})


