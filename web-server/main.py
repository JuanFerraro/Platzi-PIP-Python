import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/') #A esto se le llama decorador
def get_list():
    return [1,2,3]

@app.get('/contact', response_class = HTMLResponse) 
def contact():
    return """
        <h1>Hola, acá aprendiendo python</h1>
        <p>Parrafo parrafo parrafo</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()