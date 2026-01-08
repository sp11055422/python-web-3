from django.shortcuts import render, redirect
from studentapp.models import Student

# Create your views here.

def listone(request):
    oneperson=None
    error=None
    try:
        oneperson=Student.objects.get(cName='李佩玲')
    except:
        error='查無此人' 
    return render(request, 'listone.html', locals())

def listall(request):
    students=Student.objects.all().order_by('id')
    return render(request, 'listall.html', locals())

def insert(request):
    if request.method=='POST':
        cName=request.POST['name']
        cSex=request.POST['sex']
        cBirthday=request.POST['birthday']
        cEmail=request.POST['email']
        cPhone=request.POST['phone']
        cAddr=request.POST['address']
        unit=Student.objects.create(cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail, cPhone=cPhone, cAddr=cAddr)
        unit.save()
        students=Student.objects.all().order_by('-id')
        return render(request, 'listall.html',locals())
    else:
        return render(request, 'insert.html',locals())

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/listall/')