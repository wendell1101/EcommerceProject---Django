from django.shortcuts import render

def admin(request):
    return render(request,'admin_panel/dashboard.html')
