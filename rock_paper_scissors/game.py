import random
from dataclasses import dataclass, field

from entity import Entity
from rules import get_winner
from ui import UI


def cpu_chooses() -> Entity:
    return random.choice(list(Entity))


@dataclass
class Game:
    ui: UI
    user_name: str
    cpu_name: str = field(default="CPU", init=False)

    def turn(self) -> None:
        user_entity = self.ui.pick_user_entity()
        cpu_entity = cpu_chooses()

        self.ui.display_current_round(
            self.user_name, user_entity, self.cpu_name, cpu_entity
        )

        winner, msg = get_winner(user_entity, cpu_entity)

        if not winner:
            self.ui.display_tie()
        else:
            players_choices = {
                user_entity: self.user_name,
                cpu_entity: self.cpu_name
            }
            self.ui.display_round_winner(players_choices[winner], winner, msg)

    def play(self):
        self.ui.display_welcome()
        while True:
            self.turn()
            self.ui.clear_display()
            if not self.ui.user_wants_to_continue():
                break
