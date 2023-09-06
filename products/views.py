from django.shortcuts import render
from .models import Student,Teacher
from django.db import connection
from django.db.models import Q

# Create your views here.
def index(request):
    posts = Student.objects.all()
    print(posts.query)
    print(connection.queries)
    return render(request,'index.html',{'posts':posts})




def index(request):
    posts = Student.objects.filter(Q(surname__startswith='y') | Q (surname__startswith='jack'))
    print(posts.query)
    print(connection.queries)
    return render(request,'index.html',{'posts':posts})


def index(request):
    posts = Student.objects.filter(classroom=12) & Student.objects.filter(age=20)
    print(posts.query)
    print(connection.queries)
    return render(request,'index.html',{'posts':posts})


def index(request):
    posts = Student.objects.filter(Q(surname__startswith='y')&Q(firstname__startswith='al'))
    print(posts.query)
    print(connection.queries)
    return render(request,'index.html',{'posts':posts})

def index(request):
    posts = Student.objects.all().values_list("firstname").union(Teacher.objects.all().values_list)
    