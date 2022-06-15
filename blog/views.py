from unicodedata import name
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View
from .models import Article, Contacto
from django.views.generic import ListView
from .forms import FormContacto
# Create your views here.
# DATABASE= {
#    'detail-article':"Primer articulo es de ranas"
# }
def blog(request):
    if request.method == 'GET':
        return render(request, 'blog/blog.html',{})

class Home(ListView):
    def get(self, request):
        # <view logic>
        articles= Article.objects.all()
        return render(request, 'blog-plantilla\index.html',{'articles': articles})

class ArticleVista(View):
    def get(self, request, slug):
        article= Article.objects.get(slug=slug)
        article= get_object_or_404(Article, slug= slug)
        return render(request, 'blog-plantilla\post.html', {'article': article} )

class ContactoVista(View):
    def get(self,request):
        return render(request, 'blog-plantilla\contact.html', {} )

    def post(self,request):
        if request.method == "POST":
            data= request.POST
            form =FormContacto(data)

            if form.is_valid():
                name = form.cleaned_data.get('name')
                email = form.cleaned_data.get('email')
                phone_number = form.cleaned_data.get('phone_number')
                message = form.cleaned_data.get('message')

                Contacto.objects.create(
                name = name,
                email = email,
                phone_number = phone_number,
                message = message,)

                print('Guardamos los datos del usuario')
                
            else:
                print(form.errors)
                errors= form.errors
                return render(request, 'blog-plantilla\contact.html', {'errors':errors} )



        return render(request, 'blog-plantilla\contact.html', {} )