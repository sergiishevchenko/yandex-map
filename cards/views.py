from django.shortcuts import render

def show_card(request):
    return render(request, 'index.html')