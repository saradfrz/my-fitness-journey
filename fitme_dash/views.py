from django.shortcuts import render


# Create your views here.
def home(request):
    # recipes = Recipe.objects.filter(is_published=True).order_by('id')
    return render(request, 'home.html')
