from django.shortcuts import render

def post_list(request):
    return render(request, '../templates/post_list.html', {})

def post_dash(request):
    return render(request, '../templates/post_dash.html', {})

def dashboard(request):
    return render(request, '../templates/dashboard.html', {})

def department(request):
    return render(request, '../templates/department.html', {})

def selfpage(request):
    return render(request, '../templates/selfpage.html', {})