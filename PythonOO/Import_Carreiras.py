import requests
import json
from typing import List, Dict


def enviar_lista_para_endpoint(url: str, lista_dados: List[Dict]) -> None:
    """
    Envia uma lista de dicionários para um endpoint via POST.
    
    :param url: Endpoint da API
    :param lista_dados: Lista contendo os dados a serem enviados
    """
    
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            data=json.dumps(lista_dados),
            timeout=10
        )

        print(f"Status Code: {response.status_code}")

        if response.status_code in (200, 201):
            print("✅ Envio realizado com sucesso!")
            print("Resposta:", response.json())
        else:
            print("⚠️ Erro ao enviar dados")
            print("Resposta:", response.text)

    except requests.exceptions.RequestException as e:
        print("❌ Erro na requisição:", e)


if __name__ == "__main__":

    # Exemplo de lista
    lista_exemplo = [
        {"id": 1, "nome": "João", "nota": 8.5},
        {"id": 2, "nome": "Maria", "nota": 9.2},
        {"id": 3, "nome": "Carlos", "nota": 7.8}
    ]

    endpoint = "https://httpbin.org/post"  # Endpoint de teste

    enviar_lista_para_endpoint(endpoint, lista_exemplo)