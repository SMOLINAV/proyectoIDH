import pandas as pd
import requests
from bs4 import BeautifulSoup

def obtener_crecimiento_idh(pais):
    # URL de la página web
    url = "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_%C3%ADndice_de_desarrollo_humano"

    # Realizamos la solicitud HTTP a la página web
    response = requests.get(url)

    # Verificamos si la solicitud fue exitosa
    if response.status_code == 200:
        # Parseamos el contenido HTML de la página web
        soup = BeautifulSoup(response.content, 'html.parser')

        # Buscamos la tabla que contiene los datos del IDH
        tables = pd.read_html(url)

        # Convertimos la columna "País" a minúsculas fuera del ciclo for
        for table in tables:
            if "País" in table.columns:
                # Encontramos la tabla correcta
                df = table
                df["País"] = df["País"].apply(lambda x: x.lower())
                break
        else:
            # No se encontró la tabla
            print("No se encontró la tabla.")
            return None

        # Buscamos el país en la tabla
        fila_pais = df[df["País"] == pais.lower()]
        
        # Verificamos si se encontró el país en la tabla
        if not fila_pais.empty:
            # Obtenemos el último valor de IDH del país
            ultimo_idh = fila_pais.iloc[0, -1]
            return ultimo_idh
        else:
            # No se encontró información sobre el país
            print(f"No se encontró información sobre el crecimiento del IDH de {pais}")
            return None
    else:
        # La solicitud no fue exitosa
        print("No se pudo acceder a la página web.")
        return None

# Solicitamos al usuario el nombre del país
nombre_pais = input("Ingresa el nombre del país para obtener su crecimiento IDH más reciente: ")

# Obtenemos el crecimiento del IDH del país ingresado
crecimiento_idh = obtener_crecimiento_idh(nombre_pais)

# Imprimimos el resultado
if crecimiento_idh is not None:
    print(f"El crecimiento del IDH más reciente de {nombre_pais.capitalize()} es: {crecimiento_idh}")
