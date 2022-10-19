from typing import Protocol

from entity import Entity


class UI(Protocol):

    def display_welcome(self) -> None:
        raise NotImplementedError()

    def display_error(self, msg: str) -> None:
        raise NotImplementedError()

    def read_user_name(self) -> str:
        raise NotImplementedError()

    def pick_user_entity(self) -> Entity:
        raise NotImplementedError()

    def display_current_round(
        self,
        user_name: str, user_entity: Entity,
        cpu_name: str, cpu_entity: Entity
    ) -> None:
        raise NotImplementedError()

    def display_tie(self) -> None:
        raise NotImplementedError()

    def display_round_winner(
        self, winner_name: str, winner_entity, msg: str
    ) -> None:
        raise NotImplementedError()

    def clear_display(self) -> None:
        raise NotImplementedError()

    def user_wants_to_continue(self) -> bool:
        raise NotImplementedError()
