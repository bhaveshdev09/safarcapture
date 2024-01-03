from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout

def dashboardlogin(request):
    if request.method=="GET":
      return render(request,"dashboard-login.html")
    if request.method=="POST":
        useremail=request.POST['email']
        userpassword=request.POST['password']
        myuser=authenticate(username=useremail,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            print("login success!")
            return redirect('dashboardmain')         
        else:
            return HttpResponse("<h3>login fail!</h3>")

    return render(request,"dashboard-login.html")  

        
def dashboardmain(request):
    return render(request,"dashboard-main.html") 

def handlelogout(request):
    logout(request)
    print("user logout success!")
    return redirect('dashboardlogin')