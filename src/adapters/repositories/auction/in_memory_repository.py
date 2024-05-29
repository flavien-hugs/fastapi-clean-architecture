from typing import Any, List

from src.domain.enitites.auction import Auction
from src.domain.enitites.bid import Bid
from src.ports.repositories.auction import AuctionRepository


class InMemoryAuctionRepository(AuctionRepository):
    auctions: List[Auction] = []

    async def get(self, **filters: Any) -> Auction | None:
        for auction in self.auctions:
            if (f := filters.get("id")) and f == auction.id:
                return auction
        return None

    async def add_bid(self, bid: Bid) -> bool:
        for auction in self.auctions:
            if auction.id == bid.auction_id:
                auction.bids.append(bid)
                return True
        return False
