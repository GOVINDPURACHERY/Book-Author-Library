
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, ListView
from .models import *
from django.contrib import auth, messages
from django.urls import reverse_lazy
# Create your views here.


def AddAuthorView(request):
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        insertqry = Authors.objects.create(author_name = author_name,user_name=user_name,email=email,phone=phone,status = "True")
        insertqry.save()
        return redirect('authorlist')
    return render(request,'addauthorform.html')


'''for project purpose only - 
    superuser - username = admin
    superuser - password = admin
'''

def LoginPageView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request,user)
            return redirect('authorlist')
        else:
            messages.error(request,"invalid user")
            return redirect('login')
    return render(request,"login.html")



# def AuthorListView(request):
#     author_list = Authors.objects.all()
#     total_books = Books.objects.count()
#     total_authors = Authors.objects.count()
#     return render(request,'authors.html',{"author_data":author_list,"total_books":total_books,"total_authors":total_authors})
class AuthorListViewClass(ListView):
    model = Authors
    fields = '__all__'
    template_name = 'authors.html'
    context_object_name = 'author_data'
    # paginate_by = 3
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_books"] = Books.objects.count()
        context["total_authors"] = Authors.objects.count() 
        return context
    

def BookListView(request):
    book_list = Books.objects.all()
    print(book_list)
    total_books = Books.objects.count() 
    total_authors = Authors.objects.count()
    return render(request,'books.html',{"book_data":book_list,"total_books":total_books,"total_authors":total_authors})

class  AuthorUpdateView(UpdateView):
    model = Authors
    fields = '__all__'
    template_name = 'addauthorform.html'
    success_url = reverse_lazy('authorlist')
    context_object_name = 'data'

def DetailView(request, pk):
    detail_data = Authors.objects.get(id=pk)
    book_data = Books.objects.filter(author_id=pk)
    return render(request,'singleauthor.html',{"detail_data":detail_data,"book_data":book_data})


def AddBookView(request):
    authors_list = Authors.objects.all()
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        author_name = request.POST.get('author_name_select')
        author_data = Authors.objects.get(author_name=author_name)
        insertqry = Books.objects.create(book_name = book_name,author_id = author_data, status = True)
        insertqry.save()
        return redirect('booklist')
    return render(request,'addbookform.html',{"authors_list":authors_list})



def BookUpdateView(request,pk):
    authors_list = Authors.objects.all()
    old_book_data = Books.objects.get(id=pk)
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        author_name = request.POST.get('author_name_select')
        author_data = Authors.objects.get(author_name=author_name)
        updateqry = Books.objects.get(id=pk)
        updateqry.book_name = book_name
        updateqry.author_id = author_data
        updateqry.save()
        return redirect('booklist')
    return render(request,'addbookform.html',{"authors_list":authors_list,"old_book_data":old_book_data})


def logout(request):
    auth.logout(request)
    return redirect('login')

# def AuthorSearch(request):
#     if request.method == 'POST':
#         author_name = request.POST.get('search')
#         author = Authors.objects.get(author_name=author_name)
#         if author:
#             return redirect('authorlist')
#         else:
#             messages.error(request,"no data exist")
#     return render(request,'authors.html',{"author_search_data":author})