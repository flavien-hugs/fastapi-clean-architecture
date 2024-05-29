"""
src/domain/value_objects/price.py
Define object Price
"""

from dataclasses import dataclass
from enum import StrEnum


class CurrencyOption(StrEnum):
    euro = "EUR"
    xof = "XOF"
    xaf = "XAF"


@dataclass(frozen=True)
class Price:
    value: float
    currency: CurrencyOption
