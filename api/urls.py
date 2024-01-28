from django.urls import path
from .views import AuthorsList, BooksList
urlpatterns = [
    path('authorslist/', AuthorsList.as_view(),name="authorslist"),
    path('bookslist/',BooksList.as_view(), name='bookslist'),
]
