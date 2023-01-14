from argparse import ArgumentParser

from rpsgame.cli import CLI
from rpsgame.game import Game
from rpsgame.players import CPUPlayer, HumanPlayer


def main() -> None:
    cli = CLI(ArgumentParser())

    player1 = HumanPlayer(cli.read_player_name(), cli.pick_player_entity)
    player2 = CPUPlayer()

    game = Game(cli, player1, player2, cli.read_rounds())
    try:
        game.play()
    except KeyboardInterrupt:
        cli.display_interrupt()


if __name__ == '__main__':
    main()
