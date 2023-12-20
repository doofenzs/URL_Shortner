from django.shortcuts import render 
import requests 

BITLY_ACCESS_TOKEN = 'Bearer 1824405919cf129f0cd7ced8d30dd2d3f23429ad'
BITLY_API_URL = 'https://api-ssl.bitly.com/v4/shorten'

def index(request): 
    return render(request, 'index.html') 

def index_form(request): 
    if request.method == "POST": 
        long_url = request.POST.get('long_url') 
        new_url = shorten_url(long_url) 
        return render(request, "new_url.html", context={'url': new_url}) 
    return render(request, 'index.html') 

def shorten_url(url): 
    headers = {'Authorization': BITLY_ACCESS_TOKEN, 'Content-Type': 'application/json'} 
    payload = {'long_url': url, 'domain': 'bit.ly'} 

    try:
        response = requests.post(BITLY_API_URL, headers=headers, json=payload) 
        response.raise_for_status() 
        short_url = response.json().get('link', 'Error: No link in response')
    except requests.RequestException as e:
        short_url = f'Error: {str(e)}'

    return short_url
