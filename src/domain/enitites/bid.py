"""
src/domain/enitites/bid.py
Define enitites Bid
"""

try:
    from datetime import datetime
    from uuid import UUID, uuid4
    from dataclasses import dataclass, field

    from src.domain.value_objects.price import Price
except ImportError as err:
    raise ImportError(str(err))


@dataclass
class Bid:
    price: Price
    bidder_id: UUID
    auction_id: UUID
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=datetime.now())

