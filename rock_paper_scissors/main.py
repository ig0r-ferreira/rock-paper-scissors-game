from cli import CLI
from game import Game

if __name__ == "__main__":
    cli = CLI()
    player_name = cli.read_user_name()
    game = Game(cli, player_name)
    game.play()
