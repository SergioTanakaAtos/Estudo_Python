from django.shortcuts import render

# Create your views here.
def metodo(request):
    return render(request,'produtos/index.html')