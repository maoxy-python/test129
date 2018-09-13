from django.shortcuts import render

# Create your views here.


def index(request):
    print('sss')
    return render(request, 'admin_app/index.html')


def addParentCate(request):

    pass
    return render(request, 'admin_app/main/zjsp.html')


def addBook(request):

    pass
    return render(request, 'admin_app/main/add.html')