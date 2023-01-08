import random
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Callable

from rpsgame.entity import Entity


@dataclass
class Player(ABC):
    name: str
    _choice: Entity | None = field(default=None, init=False, repr=False)

    @property
    def choice(self):
        return self._choice

    @abstractmethod
    def choice_entity(self) -> None:
        ...

    def __str__(self) -> str:
        return f'{self.choice}'


@dataclass
class HumanPlayer(Player):
    ui_choice_func: Callable[..., Entity]

    def choice_entity(self) -> None:
        self._choice = self.ui_choice_func()


@dataclass
class CPUPlayer(Player):
    name: str = 'CPU'

    def choice_entity(self) -> None:
        self._choice = random.choice(list(Entity))
