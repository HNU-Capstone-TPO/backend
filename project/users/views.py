from django.shortcuts import render
from .models import User
from django.db.models import Q
from rest_framework import generics
from .serializer import UserSerializer
from django.http.response import HttpResponse
from django.db.models import F
from django.http import JsonResponse  # json형식으로 반환


def home(request):
    return render(request, 'folder/index.html')


def home1(request):
    return render(request, 'folder/base.html')


gen = ["남자", "여자", "공용", "남성", "여성"]
part = ["상의", "하의", "신발", "모자", "아우터"]
season = []
color = ["빨강", "파랑", "노랑", "청색", "흰색", "검은색"]
price = int
brand = []


def createform(request):
    query = request.POST.getlist('query[]')

    input1 = None
    input2 = None
    input3 = None
    input4 = []

    for q in query:
        if q in gen:
            input1 = q
        elif q in part:
            input2 = q
        elif q in color:
            input3 = q
        else:
            input4.append(q)

    input4 = list(set(input4))

    filters = Q()
    if input1:
        filters &= Q(gender__icontains=input1)
    if input2:
        filters &= Q(part__icontains=input2)
    if input3:
        filters &= Q(color__icontains=input3)
    if input4:
        for q in input4:
            users = User.objects.filter(tag__icontains=q)
            users.update(score=F('score') + 1)

        filters |= Q(tag__icontains=input4)

    users = User.objects.filter(filters).order_by('-score')
    serializer = UserSerializer(users, many=True)
    data = serializer.data

    users.update(score=0)

    # return JsonResponse({'users': data})
    return render(request, 'folder/search.html', {'users': data})


def search_view(request):
    users = User.objects.all()
    return render(request, 'folder/search.html', {'users': UserSerializer(users, many=True)})


class UserListsCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
