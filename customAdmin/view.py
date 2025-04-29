from django.shortcuts import render, redirect
from django.contrib.auth.models import User,AnonymousUser
from django.contrib.auth import authenticate,login,logout
from app.models import *
from customAdmin.models import *
from datetime import date
today = date.today()
def admin(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_superuser :
                login(request, user)
                return redirect('adminIndex')
        else:
            return render( request,'login.html')
        
    return render(request,'adminLogin.html')

def adminLogout(request):
      
      if request.user.is_anonymous:
            return redirect('login')
      
      logout(request)
      return redirect('login')

def adminIndex(request):
    borrowed = Borrowed.objects.all().filter(approved=False)
    return render(request,'sec.html',{'borrowed' : borrowed})

def addBook(request):
     
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        author = request.POST.get('author')
        quantity = request.POST.get('quantity')

        addBook = Books(name=name,subject=subject,author=author,quantity=quantity,isBorrowed=False)
        addBook.save()

    return redirect('adminIndex')

def adminUpdate(request,id):
    
    book = Borrowed.objects.get(id=id)
    book.approved = True
    book.date = today.strftime("%Y-%m-%d")
    collection = Books.objects.get(name=book.name)
    collection.quantity = collection.quantity - book.quantity
    if (collection.quantity - book.quantity) < 0:
        return redirect('adminIndex')
    

    book.save()
    collection.save()
    return redirect('adminIndex')

def adminReject(request,id):

    temp = Borrowed.objects.get(id=id)
    temp.delete()
    return redirect('adminIndex')