from rich.align import Align
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.prompt import IntPrompt
from rich.text import Text

from rpsgame.entity import Entity
from rpsgame.players import Player

console = Console()
layout = Layout()

VS = r"""
__      _______
\ \    / / ____|
 \ \  / / (___
  \ \/ / \___ \
   \  /  ____) |
    \/  |_____/

"""


def _entities_as_enum_dict() -> dict[int, Entity]:
    return dict(enumerate(Entity, start=1))


def _options_as_str(options: dict[int, Entity]) -> str:
    return ', '.join(
        f'{index} for {entity.name}' for index, entity in options.items()
    )


def horizontally_mirror(ascii_art: str) -> str:
    rows = ascii_art.splitlines()
    max_len = max(map(len, rows))

    def rotate_row(row: str) -> str:
        return row[::-1].translate(str.maketrans('()', ')(')).rjust(max_len)

    return '\n'.join(map(rotate_row, rows))


class CLI:
    def display_welcome(self) -> None:
        console.print(
            '\nWelcome to the Rock, Paper, Scissors game!\n',
            justify='center',
        )

    def display_error(self, msg: str) -> None:
        console.print(f'Error: {msg}', style='red')

    def read_player_name(self) -> str:
        return console.input('Please enter your name: ').strip() or 'You'

    def pick_player_entity(self) -> Entity:
        options = _entities_as_enum_dict()

        choice = IntPrompt.ask(
            f'\nWhen ready, type {_options_as_str(options)}',
            choices=list(map(str, options.keys())),
            show_choices=False,
        )
        return options[choice]

    def display_current_round(self, round_number: int) -> None:
        console.rule(f'\nRound {round_number}')

    def display_choices(self, player1: Player, player2: Player) -> None:
        layout.unsplit()
        layout.split_row(
            Layout(
                Panel(
                    Align.center(Text(str(player1))),
                    title=player1.name,
                )
            ),
            Layout(Panel(Align.center(Text(VS)), style='gold3')),
            Layout(
                Panel(
                    Align.center(Text(horizontally_mirror(str(player2)))),
                    title=player2.name,
                )
            ),
        )

        console.print(layout, height=10, new_line_start=True)

    def display_tie(self) -> None:
        console.print("\nIt's a tie!\n", style='yellow3', justify='center')

    def display_round_winner(self, player: Player, msg: str) -> None:
        console.print(
            f'\n{msg} - {player.name} won!\n',
            style='green',
            justify='center',
        )

    def display_game_over(self) -> None:
        console.print('Game Over. Thanks for playing!\n', justify='center')
