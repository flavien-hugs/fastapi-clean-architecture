from typing import List
from datetime import date
from uuid import UUID, uuid4
from dataclasses import dataclass, field

from src.domain.enitites.bid import Bid
from src.domain.enitites.item import Item
from src.domain.value_objects.price import Price


@dataclass
class Auction:
    item: Item
    seller_id: UUID
    start_date: date
    end_date: date
    start_price: Price
    bids: List[Bid] = field(default_factory=list)
    id: UUID = field(default_factory=uuid4)

    @property
    def is_active(self) -> bool:
        return self.start_date <= date.today() <= self.end_date

    @property
    def minimal_bid_price(self) -> Price:
        return max(
            [bid.price for bid in self.bids] + [self.start_price], key=lambda x: x.value
        )
