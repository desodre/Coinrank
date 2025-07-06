import flet as ft
from dotenv import load_dotenv
from API.CoinRequisition import CoinRequisition
from API.Coin import Coin
from Models.CoinContainer import CoinContainer
load_dotenv()

def main(page: ft.Page):
    coinReq = CoinRequisition()
    top5Coins:list[Coin] = coinReq.get_coins(limit=5)

    for coin in top5Coins:
        page.add(CoinContainer(coin=coin))


ft.app(main)
