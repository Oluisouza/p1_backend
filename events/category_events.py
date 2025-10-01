from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any

@dataclass(frozen=True)
class CategoryCreated:
    category_id: str
    name: str
    description: str
    is_active: bool
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass(frozen=True)
class CategoryUpdated:
    category_id: str
    updated_fields: Dict[str, Any]
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass(frozen=True)
class CategoryActivated:
    category_id: str
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass(frozen=True)
class CategoryDeactivated:
    category_id: str
    timestamp: datetime = field(default_factory=datetime.now)