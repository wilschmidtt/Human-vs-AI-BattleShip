from typing import List
from BattleShip.src import move, ship, orientation, game_config, ship_placement
from BattleShip.src.player import Player
import random
import abc


class AIPlayer(Player):

    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__(player_num, config, other_players)

    @abc.abstractmethod
    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
        ...

    def place_ship(self, ship_: ship.Ship) -> None:
        while True:
            placement = self.get_ship_placement(ship_)
            try:
                self.board.place_ship(placement)
            except ValueError as e:
                pass
            else:
                return

    def get_ship_placement(self, ship_: ship.Ship):
        while True:
            try:
                orientation_ = self.get_orientation(ship_)
                start_row, start_col = self.get_start_coords(ship_, orientation_)
            except ValueError as e:
                print(e)
            else:
                return ship_placement.ShipPlacement(ship_, orientation_, start_row, start_col)

    def get_orientation(self, ship_: ship.Ship) -> orientation.Orientation:
        return random.choice([orientation.Orientation.HORIZONTAL, orientation.Orientation.VERTICAL])

    def get_start_coords(self, ship_: ship.Ship, orientation_: orientation.Orientation):
        if orientation_ == orientation.Orientation.HORIZONTAL:
            row = random.randint(0, self.board.num_rows - 1)
            col = random.randint(0, self.board.num_cols - ship_.length)
        else:
            row = random.randint(0, self.board.num_rows - ship_.length)
            col = random.randint(0, self.board.num_cols - 1)
        return row, col

    @abc.abstractmethod
    def get_move(self) -> move.Move:
        ...

