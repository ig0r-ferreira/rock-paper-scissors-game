import random

from entity import Entity


COLORS_CODES = {
    "red": "\033[1;31m",
    "yellow": "\033[1;33m",
    "reset": "\033[m"
}


def _entities_as_enum_dict() -> dict:
    return dict(enumerate(Entity, start=1))


def _entities_str() -> str:
    return ", ".join(
        f"{index} for {entity}"
        for index, entity in _entities_as_enum_dict().items()
    )


class CLI:

    def display_welcome(self) -> None:
        print("\nWelcome to the Rock, Paper, Scissors game.\n")

    def display_error(self, msg: str) -> None:
        print("{red}Error: {msg}{reset}".format(**COLORS_CODES, msg=msg))

    def read_user_name(self) -> str:
        return input("Please enter your name: ").strip()

    def pick_user_entity(self) -> Entity:
        options = _entities_as_enum_dict()
        while True:
            try:
                choice = int(input(
                    "What do you choose? "
                    f"Type {_entities_str()}.\n=> "
                ).strip())
            except ValueError:
                self.display_error(
                    "You entered something that is not a valid number. "
                    "Try again!"
                )
            else:
                if choice in options:
                    return options[choice]

                self.display_error("Choose one of the available options. "
                                   "Try again!")

    def display_current_round(
        self,
        user_name: str, user_entity: Entity,
        cpu_name: str, cpu_entity: Entity
    ) -> None:
        print(f"{user_name} ({user_entity}) x {cpu_name} ({cpu_entity})")

    def display_tie(self) -> None:
        print("{yellow}It's a tie!{reset}".format(**COLORS_CODES))

    def display_round_winner(
        self, winner_name: str, winner_entity, msg: str
    ) -> None:
        print(f"{msg}. {winner_name} ({winner_entity}) won!")

    def clear_display(self) -> None:
        print("\033[H\033[J", end="")

    def user_wants_to_continue(self) -> bool:
        print()
        continue_game = None
        while continue_game not in ("y", "n"):
            continue_game = input(
                "Do you want to play again? [y/n]: "
            ).strip().lower()

        return continue_game == 'y'
