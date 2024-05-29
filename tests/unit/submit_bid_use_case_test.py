import uuid
import pytest

from datetime import date, timedelta

from src.adapters.repositories.auction.in_memory_repository import (
    InMemoryAuctionRepository,
)
from src.ports.repositories.auction import AuctionRepository

from tests.utils import create_bid, create_auction
from src.use_cases.exceptions import (
    AuctionNotFoundError,
    AuctionNotActiveError,
    LowBidError,
)
from src.use_cases.submit_bid import SubmitBidUseCase


@pytest.fixture
def auction_repository() -> AuctionRepository:
    return InMemoryAuctionRepository()


@pytest.fixture
def submit_bid_use_case(auction_repository: AuctionRepository) -> SubmitBidUseCase:
    return SubmitBidUseCase(auction_repository)


@pytest.mark.asyncio
async def test_auction_not_found(submit_bid_use_case: SubmitBidUseCase):
    bid = create_bid(auction_id=uuid.uuid4())
    with pytest.raises(AuctionNotFoundError):
        await submit_bid_use_case(bid)


@pytest.mark.asyncio
async def test_auction_not_active(
    auction_repository: InMemoryAuctionRepository,
    submit_bid_use_case: SubmitBidUseCase,
):
    auction = create_auction(
        end_date=date.today() - timedelta(days=1),
    )
    auction_repository.auctions.append(auction)
    bid = create_bid(auction_id=auction.id)
    with pytest.raises(AuctionNotActiveError):
        await submit_bid_use_case(bid)


@pytest.mark.asyncio
async def test_bid_price_lower_than_start_price(
    auction_repository: InMemoryAuctionRepository,
    submit_bid_use_case: SubmitBidUseCase,
):
    auction = create_auction(start_price_value=10)
    auction_repository.auctions.append(auction)
    bid = create_bid(auction_id=auction.id, price_value=9)
    with pytest.raises(LowBidError):
        await submit_bid_use_case(bid)


@pytest.mark.asyncio
async def test_bid_price_lower_than_higtest_price(
    auction_repository: InMemoryAuctionRepository,
    submit_bid_use_case: SubmitBidUseCase,
):
    auction = create_auction(bids=[create_bid(price_value=20)])
    auction_repository.auctions.append(auction)
    bid = create_bid(auction_id=auction.id, price_value=19)
    with pytest.raises(LowBidError):
        await submit_bid_use_case(bid)


@pytest.mark.asyncio
async def test_bid_successfully_added(
    auction_repository: InMemoryAuctionRepository, submit_bid_use_case: SubmitBidUseCase
):
    auction = create_auction()
    auction_repository.auctions.append(auction)
    bid = create_bid(auction_id=auction.id)
    await submit_bid_use_case(bid)
    result = await auction_repository.get(id=auction.id)

    assert result is not None and bid in result.bids
    assert isinstance(result.id, uuid.UUID) is True
