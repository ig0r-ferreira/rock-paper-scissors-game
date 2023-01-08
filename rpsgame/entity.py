from enum import Enum

ROCK = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

PAPER = r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

"""

SCISSORS = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""


class Entity(Enum):
    ROCK = ROCK
    PAPER = PAPER
    SCISSORS = SCISSORS

    def __str__(self):
        return self.value
