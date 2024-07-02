import requests

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_location(ip):
    geo_api_url = f'https://ipapi.co/{ip}/json/'
    response = requests.get(geo_api_url)
    return response.json()

def get_temperature(city):
    weather_api_key = 'bf12a4c39ad553044b01fa3896b83239'
    weather_api_url = f'https:/api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric'
    response = requests.get(weather_api_url)
    return response.json()