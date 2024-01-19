from django.shortcuts import render
from .models import ConfessionModel
from django.http import HttpResponse

def load(request):
    confession_list = []
    for i in ConfessionModel.objects.all():
        confession_list.append(
            {
                'from': i.from_name,
                'to': i.to_name,
                'confession': i.confession
            }
        )
    return render(request, 'home.html', context={'confession_list': confession_list})

def confess(request):
    if request.method == "GET":
        return render(request, 'confess.html')
    if request.method == "POST":
        from_name = request.POST['from']
        to_name = request.POST['to']
        data = request.POST['confession']
        confession = ConfessionModel(from_name=from_name, to_name=to_name, confession=data)
        confession.save()
        return HttpResponse("Confession saved")
        
        