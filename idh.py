import pandas as pd
'''
esta función obtiene el crecimiento más reciente del índice de desarrollo humana (IDH) de un país en.wikipedia.org
args:
    pais: nombre del país
returns:
    crecimiento_idh: crecimiento más reciente del índice de desarrollo humana (IDH)
    None: si no se encuentra información sobre el crecimiento del índice de desarrollo humana (IDH)
'''
def obtener_crecimiento_idh(pais):
    # URL de la página web
    url = "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_%C3%ADndice_de_desarrollo_humano"

    # Leer las tablas de la página
    tablas = pd.read_html(url)

    # Buscar el país en la primera columna de la primera tabla
    for tabla in tablas:
        if "País" in tabla.columns:
            for fila in tabla.itertuples(index=False):
                for elemento in fila:
                    if str(pais).lower() in str(elemento).lower():
                        ultimo_idh = fila[-1].strip()
                        return ultimo_idh

    # Si no se encontró información sobre el país, devolver None
    return None

# Pedir al usuario que ingrese el nombre del país
nombre_pais = input("Ingresa el nombre del país para obtener su crecimiento IDH más reciente: ")

# Obtener el crecimiento del IDH del país ingresado por el usuario
crecimiento_idh = obtener_crecimiento_idh(nombre_pais)

if crecimiento_idh:
    print(f"El crecimiento del IDH más reciente de {nombre_pais.capitalize()} es: {crecimiento_idh}")
else:
    print(f"No se encontró información sobre el crecimiento del IDH de {nombre_pais}")
