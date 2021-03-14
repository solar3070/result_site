from django.shortcuts import render, redirect
from .models import Result
from .forms import ResultForm

# Create your views here.

def home(request):
  form = ResultForm()
  return render(request, 'home.html', {'form':form})

def pass_fail(request):
  form = ResultForm(request.POST)
  if form.is_valid():
    obj = Result.objects.filter(name=form.data['name'], phone=form.data['phone'])
    if obj.exists(): #지원한 사람
      if obj[0].pf:  #합격한 사람
        return render(request, 'pass.html', {'obj':obj[0]})
      else: #탈락한 사람
        return render(request, 'fail.html', {'obj':obj[0]})
    else:
      error = True;    
      clearForm = ResultForm()
      return render(request, 'home.html', {'error':error, 'form':clearForm}) #지원하지 않았거나 틀린 정보 입력
  else:
    return render(request, 'home.html', {'form':form})