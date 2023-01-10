"""LIBRERIAS"""
import pandas as pd


"""FUNCIONES"""


def listar_archivos(_dictarchidatos:dict):
    """
    Funcion para listar archivos existentes
    Args:
        _dictrafico (dict): diccionario de directorios de acceso a los archivos de datos.
    """
    assert type(_dictarchidatos)==dict, "Tipo de dato incorrecto"
    for clase, directorio in _dictarchidatos.items():
        print('Clase:',clase)
        for archivo in range(len(directorio)):
            print("%s" % str(archivo+1))



def etiquetar_unirdatosdeclase(_dictarchidatos:dict, caracteristica:str, dir_guardar:str):
    assert type(_dictarchidatos)==dict, "Tipo de dato incorrecto"
    assert type(caracteristica)==str, "Tipo de dato incorrecto"
    assert type(dir_guardar)==str,"Tipo de dato incorrecto"
    """Funcion para unir archivos de datos de la misma clase y etiquetarlos segun el tipo.
    Args:
        _dictrafico (dict): diccionario de directorios de acceso a los archivos de datos.
        caracteristica (str): nombre del atributo o columna a etiquetar. La etiqueta es asignada segun el nombre de la carpeta que contiene todos los archivos de datos de esa clase.
        dir_guardar (str): carpeta donde se guardan todos los archivos generados que resultan del etiquetado y unificacion por clase.
    """
    dataframes = []
    for clase, directorio in _dictarchidatos.items():
        print("En proceso de clase %s..." % (clase))
        for archivo in range(len(directorio)):
            archivo_exdata = str(_dictarchidatos[clase][archivo])
            df = pd.read_csv(archivo_exdata, low_memory=False)
            df[caracteristica]=clase
            dataframes.append(df)

        ttotal_data = pd.concat(dataframes)
        ttotal_data.to_csv(dir_guardar+str(clase)+'.csv', index=False)
        print("Proceso completado.... \n Total de archivos unidos: %s" % str(len(dataframes)))
        dataframes.clear()