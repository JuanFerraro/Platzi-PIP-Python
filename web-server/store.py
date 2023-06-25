import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text)) #Llega como str
    categories = r.json() # La misma libreria lo transforma
    for category in categories:
        print(category['name'])