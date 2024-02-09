from django.shortcuts import render

# Create your views


def example_view(request):
    return render(request, 'myapp/example.html')
