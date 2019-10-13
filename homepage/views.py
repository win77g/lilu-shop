from django.shortcuts import render
from products.models import Product
from django.db.models import Q
# Create your views here.
# вывод главной страницы
def index(request):
   slider = Product.objects.filter(slider=True)
   slider_new = Product.objects.filter(new_product=True)
   slider_top = Product.objects.filter(new_product=True)

   return render(request,'index.html',locals())

def error_404_view(request, exception):
    # data = {"name": "ThePythonDjango.com"}
    return render(request,'404.html', )

def search(request):
    q = request.POST['q']
    product = Product.objects.filter(Q(name = q)|Q(description = q)|Q(description_short = q)
                                     |Q(brend__name = q))
    prod=list(product)
    count = len(prod)

    return render(request,'search.html',locals())
