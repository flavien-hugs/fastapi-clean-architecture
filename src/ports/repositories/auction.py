from abc import ABC, abstractmethod
from typing import Any

from src.domain.enitites.auction import Auction
from src.domain.enitites.bid import Bid


class AuctionRepository(ABC):
    @abstractmethod
    async def get(self, **filters: Any) -> Auction | None:
        pass

    @abstractmethod
    async def add_bid(self, bid: Bid) -> bool:
        pass
