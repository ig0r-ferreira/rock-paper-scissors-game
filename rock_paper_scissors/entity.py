from enum import Enum


class Entity(Enum):
    ROCK = "Rock"
    PAPER = "Paper"
    SCISSORS = "Scissors"

    def __str__(self):
        return self.value
