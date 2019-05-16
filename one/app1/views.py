from django.shortcuts import render
import docx2txt
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book



posts = [ {
        'author': 'Jacek',
        'title': 'Mr',
        'content': 'This is the first awesome post',
        'date_posted': '22.04.2019'
},
        {
        'author': 'Buba',
        'title': 'Ms',
        'content': 'This is the second awesome post',
        'date_posted': '24.04.2019'
}]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'app1/home.html', context)

def about(request):
    return render(request, 'app1/about.html', {'title':'About'})

def my_program(request):
    text = docx2txt.process('one/C1.docx')
    word1 = 'sillyBilly'
    word2 = "relevant"
    return render(request, 'app1/my_program.html', {"text":text, "word1":word1, "word2":word2})

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'app1/upload.html', context)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'app1/book_list.html', {
        'books': books
    })

def upload_book(request):
   if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'app1/book_list.html')
   else:
        form = BookForm()
        return render(request, 'app1/upload_book.html', {
        'form': form
    })

