import requests
import json
import time
import os

def obtener_detalles_pedido():
    url = input("Introduce el URL de la persona: ")
    seguidores = int(input("Introduce la cantidad de seguidores que quieres comprar: "))
    return url, seguidores

def realizar_pedido(url, seguidores):
    api_endpoint = "API DE TU PAGINA DE SEGUIDORES"  
    api_key = "TU API KEY (NO LA COMPARTAS CON NADIE)"  
    service_id = 0000 #NUMERO DEL SERVICIO QUE QUIERES UTILIZAR  

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "key": api_key,
        "action": "add",
        "service": service_id,
        "link": url,
        "quantity": seguidores
    }

    try:
        response = requests.post(api_endpoint, headers=headers, json=data)
        response.raise_for_status()  
        print("Pedido realizado con éxito!")
    except requests.exceptions.ConnectionError as e:
        print("Error de conexión: No se pudo resolver la dirección del servidor. Verifica tu conexión a Internet y la URL del API.")
        print(e)
    except requests.exceptions.HTTPError as e:
        print("Error HTTP: Hubo un problema con la solicitud.")
        print(e)
    except requests.exceptions.RequestException as e:
        print("Error durante la solicitud HTTP.")
        print(e)

def main():
    while True:
        url, seguidores = obtener_detalles_pedido()
        realizar_pedido(url, seguidores)
        time.sleep(5)
        os.system('cls')

if __name__ == "__main__":
    main()
