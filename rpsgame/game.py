from dataclasses import dataclass

from rpsgame.players import Player
from rpsgame.rules import get_winner
from rpsgame.ui import UI


@dataclass
class Game:
    ui: UI
    player1: Player
    player2: Player
    rounds: int

    def turn(self, round_number: int) -> None:
        self.player1.choice_entity()
        self.player2.choice_entity()

        self.ui.display_current_round(round_number, self.player1, self.player2)

        winning_entity, msg = get_winner(
            self.player1.choice, self.player2.choice
        )

        if not winning_entity:
            self.ui.display_tie()
        else:
            entities_by_players = {
                player.choice: player
                for player in (self.player1, self.player2)
            }

            winner = entities_by_players[winning_entity]

            self.ui.display_round_winner(winner, msg)

    def game_over(self):
        print('Game Over', 'Thanks for playing!', sep='\n')

    def play(self):
        self.ui.display_welcome()

        for round_number in range(1, self.rounds + 1):
            self.turn(round_number)

        self.game_over()
