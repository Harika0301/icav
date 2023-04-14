from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


from django.views import View
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import BooksDetails
import os
import csv
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists.")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request,'User created.')
                return redirect('login_api')

        else:
            messages.info(request,"PASSWORD NOT MATCHING")
            return redirect('register')

        return redirect('/')
    else:

        return render(request,'register.html')

class LoginAPIView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('csv_import')
            
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

def csv_import(request):
    
    csv_file = os.path.join('static','books.csv')
    with open(csv_file,'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row['title']
            author = row['author']
            authors = row['authors']
            isbn13 = int(row['isbn13'])
            isbn10 = row['isbn10']
            try:
                price = float(row['price'].replace('$',''))
                
            except:
                price = None
                
            publisher = row['publisher']
            pubyear = row['pubyear']
            subjects = row['subjects']
            
            try:
               
                pages = int(row['pages'])
            except ValueError:
                
                pages = None

            dimensions = row['dimensions'],
            x, books = BooksDetails.objects.get_or_create(title=title,author=author,authors=authors,isbn13=isbn13,
                                                            isbn10=isbn10,price=price,pages=pages,
                                                            publisher=publisher,pubyear=pubyear,subjects=subjects,
                                                            dimensions=dimensions)
    books_list = BooksDetails.objects.get_queryset().order_by('id')
    
    flag = request.POST.get('flag_value')
    
    if flag == '1':
        try:
            rows = int(request.POST.get('row',''))
            if rows is not None:
                books_list = books_list[:rows]
            else:
                books_list = books_list
        except ValueError:
            books_list = books_list
    else:
        books_list = books_list
    paginator = Paginator(books_list, 30)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    context = {'items': items}
    return render(request, 'books.html', context)

def logout(request):
    request.session.flush()
    return redirect('login_api')

