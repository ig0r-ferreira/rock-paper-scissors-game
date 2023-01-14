from typing import Protocol

from rpsgame.entity import Entity
from rpsgame.players import Player


class UI(Protocol):
    def display_welcome(self) -> None:
        raise NotImplementedError()

    def display_error(self, msg: str) -> None:
        raise NotImplementedError()

    def display_interrupt(self) -> None:
        raise NotImplementedError()

    def read_player_name(self) -> str:
        raise NotImplementedError()

    def read_rounds(self) -> int:
        raise NotImplementedError()

    def pick_player_entity(self) -> Entity:
        raise NotImplementedError()

    def display_current_round(self, round_number: int) -> None:
        raise NotImplementedError()

    def display_choices(self, player1: Player, player2: Player) -> None:
        raise NotImplementedError()

    def display_tie(self) -> None:
        raise NotImplementedError()

    def display_round_winner(self, player: Player, msg: str) -> None:
        raise NotImplementedError()

    def display_game_over(self) -> None:
        raise NotImplementedError()
