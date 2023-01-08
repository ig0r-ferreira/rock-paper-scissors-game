from dataclasses import dataclass, field

ROCK_ART = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

PAPER_ART = r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

"""

SCISSORS_ART = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""


@dataclass(frozen=True)
class Entity:
    name: str
    color: str
    art: str = field(repr=False)

    def __str__(self) -> str:
        return self.art


ROCK = Entity('ROCK', '#A05D19', ROCK_ART)
PAPER = Entity('PAPER', '#CCCCCC', PAPER_ART)
SCISSORS = Entity('SCISSORS', '#FF0000', SCISSORS_ART)

ENTITIES = [ROCK, PAPER, SCISSORS]
