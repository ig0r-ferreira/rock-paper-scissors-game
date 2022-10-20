from typing import Protocol

from entity import Entity
from players import Player


class UI(Protocol):

    def display_welcome(self) -> None:
        raise NotImplementedError()

    def display_error(self, msg: str) -> None:
        raise NotImplementedError()

    def read_player_name(self) -> str:
        raise NotImplementedError()

    def pick_player_entity(self) -> Entity:
        raise NotImplementedError()

    def display_current_round(
            self, round_number: int, player1: Player, player2: Player
    ) -> None:
        raise NotImplementedError()

    def display_tie(self) -> None:
        raise NotImplementedError()

    def display_round_winner(self, player: Player, msg: str) -> None:
        raise NotImplementedError()

    def clear_display(self) -> None:
        raise NotImplementedError()
