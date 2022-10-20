from cli import CLI
from game import Game
from players import CPUPlayer, HumanPlayer


if __name__ == "__main__":
    cli = CLI()

    player1 = HumanPlayer(
        cli.read_player_name(), cli.pick_player_entity
    )
    player2 = CPUPlayer()

    game = Game(cli, player1, player2, rounds=3)
    game.play()
