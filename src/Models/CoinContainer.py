from API.Coin import Coin
import flet as ft


class CoinContainer(ft.Container):
    def __init__(self,coin:Coin):
        self.coin = coin
        
        super().__init__(
            bgcolor = coin.color,
            content=ft.Row(controls=[
                ft.Text(value=self.coin.name)
            ]),
            border_radius= ft.BorderRadius(5,5,5,5),
        )