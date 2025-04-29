from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User,AnonymousUser
from django.contrib.auth import authenticate,login,logout
from app.models import *
from customAdmin.models import *
from datetime import date

today = date.today()

def index(request):

    books = Books.objects.all()
    context = {'books' : books}

    borrowed = Borrowed.objects.all().filter(user=request.user)
    context2 = {'borrowed' : borrowed}

    approved = Borrowed.objects.all().filter(approved=True)
    amount=0
    for x in approved:
        d = today > x.date
        if d:
            amount=amount+100
        
    penalty = Penalty(user=request.user,amount=amount)
    
    return render(request,'index.html',{'books' : books,'borrowed' : borrowed,'approved' : approved,'penalty' : penalty} )

def loginUser(request):
    
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render( request,'login.html')
        
    return render(request,'login.html')

def signupUser(request):
    
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')   

        if(pass1 != pass2):
            return redirect('signup')

        Myuser = User.objects.create_user(username, email, pass1)
        Myuser.save()

        return redirect('login')

    return render(request,'signup.html')

def logoutUser(request):
      if request.user.is_anonymous:
            return redirect('login')
      
      logout(request)
      return redirect('login')

def borrowAsk(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        user = request.user
        quantity = request.POST.get('quantity')
        # if quantity > 5:
        #     return render('index')

        date = today.strftime("%Y-%m-%d")

        check = Books.objects.all().filter(name__icontains = name)
        if check :
            borrow = Borrowed(user=user,name=name,quantity=quantity,approved=False,date=date)
            borrow.save()

    return redirect('index')