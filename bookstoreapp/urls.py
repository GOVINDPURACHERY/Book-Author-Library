from django.urls import path
 
from bookstoreapp.views import BookListView, AuthorListView, AddAuthorView, LoginPageView, AuthorUpdateView, DetailView, AddBookView, BookUpdateView, logout

urlpatterns = [
    path('',LoginPageView,name='login'),
    path('login/',LoginPageView,name='login'),
    path('logout/',logout,name='logout'),
    path('booklist/',BookListView, name='booklist'),
    path('authorlist/',AuthorListView, name='authorlist'),
    path('addauthorform/',AddAuthorView, name='addauthorform'),
    path('authorupdate/<int:pk>/',AuthorUpdateView.as_view(), name='authorupdate'),
    path('detailview/<int:pk>/',DetailView,name='detail_view'),
    path('addbook/',AddBookView,name='addbook'),
    path('bookupdate/<int:pk>/',BookUpdateView, name='updatebook'),
    
    
]
