import requests
import os
from typing import List
from API.Coin import Coin

class CoinRequisition:
    def __init__(self):
        self.baseURL = 'https://api.coinranking.com/v2'
        self.__api_key = os.getenv('KEY')
        if not self.__api_key:
            raise ValueError("A chave da API não foi encontrada. Verifique seu arquivo .env e a variável 'KEY'.")

    def get_coins(self, limit=10) -> List[Coin]:
        """
        Busca uma lista de moedas na API CoinRanking.
        Retorna uma lista de objetos Coin.
        """
        endpoint = '/coins'
        url = self.baseURL + endpoint

        headers = {
            'x-access-token': self.__api_key
        }
        params = {
            'limit': limit
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Lança um erro para respostas com status 4xx/5xx
            data = response.json()
            coin_list_json = data.get('data', {}).get('coins', [])
            return [Coin.from_json(coin_json) for coin_json in coin_list_json]
        except requests.exceptions.RequestException as e:
            print(f"Ocorreu um erro ao fazer a requisição: {e}")
            return []
        except (KeyError, TypeError, ValueError) as e:
            print(f"Ocorreu um erro ao processar os dados da API: {e}")
            return []