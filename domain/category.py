import uuid
from dataclasses import dataclass, field, asdict
from typing import Optional, Dict, Any,  Type

from events.category_events import (
    CategoryCreated,
    CategoryUpdated,
    CategoryActivated,
    CategoryDeactivated,
)

MAX_NAME =  255

@dataclass
class Category:
    name: str
    description: str = ""
    is_active: bool = True
    id: Optional[str] = field(default=None)

    events: list = field(default_factory=list, repr=False)

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())

        self.name = self._validate_name(self.name)
        self.description = self.description or ""
        self.is_active = bool(self.is_active)

        self.events.append(CategoryCreated(
            category_id=self.id,
            name=self.name,
            description=self.description,
            is_active=self.is_active
        ))

    @staticmethod
    def _validate_name(name: str) -> str:
        if not isinstance(name, str):
            raise ValueError("name deve ser string")
        n = name.strip()
        if not n:
            raise ValueError("name é obrigatório")
        if len(n) > MAX_NAME:
            raise ValueError(f"name deve ter no máximo {MAX_NAME} caracteres")
        return n
    
    def update(self, *, name: Optional[str] = None, description: Optional[str] = None) -> None:
        updated_fields: Dict[str, Any] = {}

        if name is not None and self.name != name:
            self.name = self._validate_name(name)
            updated_fields["name"] = self.name

        if description is not None and self.description != description:
            self.description = description
            updated_fields["description"] = self.description

        if updated_fields:
            self.events.append(CategoryUpdated(
                category_id=self.id,
                updated_fields=updated_fields
            ))

    def activate(self) -> None:
        if not self.is_active:
            self.is_active = True
            self.events.append(CategoryActivated(category_id=self.id))

    def deactivate(self) -> None:
        if self.is_active:
            self.is_active = False
            self.events.append(CategoryDeactivated(category_id=self.id))

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data.pop('events', None)
        data['class_name'] = self.__class__.__name__
        return data
    
    @classmethod
    def from_dict(cls: Type['Category'], data: Dict[str, Any]) -> 'Category':
        data.pop('class_name', None)
        return cls(**data)
    
    def __str__(self) -> str:
        return f"{self.name} | {self.description} ({'Ativa' if self.is_active else 'Inativa'})"
    
    def __repr__(self) -> str:
        return f"<Category {self.name} ({self.id})>"