from django.shortcuts import render  

# Create your views here. 

def jinja_print(request):
    d={'name':'ravi','age':20} 
    return render(request, 'jinja_print.html', context=d)
