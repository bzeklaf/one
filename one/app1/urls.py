from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('', views.home, name='one-home'),
path('about/', views.about, name='one-about'),
path('my_program/', views.my_program, name='one-my_program'),
path('upload/', views.upload, name='one-upload'),
path('books/upload/', views.upload_book, name='one-upload_book'),
path('books/', views.book_list, name='one-book_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)