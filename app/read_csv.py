import csv

#Nombre funcion (ubicacion_archivo)
def read_csv(path):
    with open(path, 'r') as csvfile: # abrir archivo con open
        reader = csv.reader(csvfile, delimiter = ',') # Lector del archivo
        # reader es un iterable, sabemos primer fila es nombre de columnas.
        header = next(reader) # array con 'llaves'
        data = []
        for row in reader:
            iterable = zip(header, row) # Daría un array de tuplas
            # Generar diccionario a partir de iterable:
            country_dict = {key: value for key, value in iterable}
            #Añadir a lista cada diccionario
            data.append(country_dict)
        return data

# Cada una de las filas tiene la información separada en listas.
# Transformarlo en diccionario para leerlo mas cómodo.


if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    print(data)