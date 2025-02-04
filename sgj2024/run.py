import arcade
import argparse

from sgj2024.gamewindow import GameWindow
from sgj2024.config import *


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    if args.debug:
        print("Launching Game in Debug Mode")
    game = GameWindow(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, debug=args.debug)
    game.setup()
    arcade.run()
    game.cleanup()