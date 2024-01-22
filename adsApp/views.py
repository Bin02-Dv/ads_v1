from django.shortcuts import render
from django.http import JsonResponse

def ad_template(request):
    # Initial ad content (can be fetched from a database or other source)
    ad_content = '<h2>Special Offer!</h2><p>Get 20% off on our products. Limited time offer!</p>'
    return render(request, 'ad_app/ad_.html', {'ad_content': ad_content})

def refresh_ad(request):
    # Simulate fetching new ad content from the server
    new_ad_content = '<h2>New Offer!</h2><p>Buy one, get one free! Exclusive deal!</p>'
    return JsonResponse({'ad_content': new_ad_content})