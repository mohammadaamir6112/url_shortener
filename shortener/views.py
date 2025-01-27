from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import URLMapping
import string, random

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def home(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        existing = URLMapping.objects.filter(original_url=original_url).first()
        if existing:
            short_code = existing.short_code
        else:
            short_code = generate_short_code()
            URLMapping.objects.create(original_url=original_url, short_code=short_code)
        short_url = request.build_absolute_uri('/') + short_code
        return render(request, 'shortener/home.html', {'short_url': short_url})
    return render(request, 'shortener/home.html')

def redirect_url(request, short_code):
    mapping = URLMapping.objects.filter(short_code=short_code).first()
    if mapping:
        return redirect(mapping.original_url)
    return HttpResponse("Invalid URL", status=404)
