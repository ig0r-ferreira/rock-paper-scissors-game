from entity import Entity
from players import Player

COLORS_CODES = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'reset': '\033[m',
}


def _entities_as_enum_dict() -> dict:
    return dict(enumerate(Entity, start=1))


def _entities_str() -> str:
    return ', '.join(
        f'{index} for {entity}'
        for index, entity in _entities_as_enum_dict().items()
    )


class CLI:
    def display_welcome(self) -> None:
        print('\nWelcome to the Rock, Paper, Scissors GAME\n')

    def display_error(self, msg: str) -> None:
        print('{red}Error: {msg}{reset}'.format(**COLORS_CODES, msg=msg))

    def read_player_name(self) -> str:
        name = None
        while not name:
            name = input('Please enter your name: ').strip()

        return name

    def pick_player_entity(self) -> Entity:
        options = _entities_as_enum_dict()
        while True:
            try:
                choice = int(input(f'Type {_entities_str()}: ').strip())
            except ValueError:
                self.display_error(
                    'You entered something that is not a valid number. '
                    'Try again!'
                )
            else:
                if choice in options:
                    return options[choice]

                self.display_error(
                    'Choose one of the available options. ' 'Try again!'
                )

    def display_current_round(
        self, round_number: int, player1: Player, player2: Player
    ) -> None:
        print(f'\n*** Round {round_number} ***: {player1} x {player2}')

    def display_tie(self) -> None:
        print("{yellow}It's a tie!{reset}".format(**COLORS_CODES))

    def display_round_winner(self, player: Player, msg: str) -> None:
        print(
            '{msg} - {green}{player} won!{reset}'.format(
                msg=msg, player=player, **COLORS_CODES
            )
        )
