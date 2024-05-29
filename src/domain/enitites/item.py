"""
src/domain/enitites/item.py
Define enitites Item
"""

try:
    from uuid import UUID, uuid4
    from dataclasses import dataclass, field
except ImportError as err:
    raise ImportError(str(err))


@dataclass
class Item:
    name: str
    description: str
    id: UUID = field(default_factory=uuid4)
