from django.shortcuts import render ,redirect
from django.http import HttpResponse
# from django.contrib.auth import logout
def dashboard(request):
    return render(request,'myapp/dashboard.html')

def teamleader(request):
    return render(request,'myapp/Admin.html')

def management(request):
    return render(request,'myapp/Management.html')

def approval(request):
    return render(request,'myapp/approval.html')

def portal(request):
    return render(request,'myapp/portal.html')

# def signin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # Check if the provided username and password match the specific credentials
#         if username == 'TwilightSoftwares' and password == 'twilight':
#             # Redirect to the main page after successful sign-in
#             return redirect('portal/')
#         if username == 'TeamLeader' and password == 'twilight':
#             return redirect('portal/')
#         if username == 'Management' and password == 'twilight':
#             return redirect('portal/')
#         else:
#             # Authentication failed, render the sign-in page again with an error message
#             return render(request, 'myapp/signin.html', {'error_message': 'Invalid username or password'})
#     else:
#         return render(request, 'myapp/signin.html')
    
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = None
       
        if username == 'employee' and password == 'twilight':
            role = 'employee'
        elif username == 'teamleader' and password == 'twilight':
            role = 'team_leader'
        elif username == 'management' and password == 'twilight':
            role = 'management'         
        if role:
            return render(request, 'myapp/portal.html', {'role': role})  
        else:
            return render(request, 'myapp/signin.html', {'error_message':'Invalid username or password'})
    else:
        return render(request, 'myapp/signin.html')
def profile(request):
    return render(request,'myapp/profile.html')


 