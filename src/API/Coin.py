from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Coin:
    uuid: str
    symbol: str
    name: str
    rank: int
    price: Optional[float]
    marketCap: Optional[float]
    change: Optional[float]
    iconUrl: str
    coinrankingUrl: str
    volume24h: Optional[float]
    color: Optional[str] = None
    sparkline: List[Optional[float]] = field(default_factory=list)

    @classmethod
    def from_json(cls, json_data: dict):
        """Cria uma instância de Coin a partir de um dicionário JSON."""
        def safe_float(value):
            return float(value) if value is not None else None

        return cls(
            uuid=json_data.get('uuid'),
            symbol=json_data.get('symbol'),
            name=json_data.get('name'),
            rank=int(json_data.get('rank')),
            price=safe_float(json_data.get('price')),
            marketCap=safe_float(json_data.get('marketCap')),
            change=safe_float(json_data.get('change')),
            iconUrl=json_data.get('iconUrl'),
            coinrankingUrl=json_data.get('coinrankingUrl'),
            volume24h=safe_float(json_data.get('24hVolume')),
            color=json_data.get('color'),
            sparkline=[safe_float(p) for p in json_data.get('sparkline', [])]
        )