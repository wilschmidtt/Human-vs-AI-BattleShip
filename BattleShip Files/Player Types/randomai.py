from typing import List
import random
from BattleShip.src import move, game_config
from BattleShip.src.player import Player
from BattleShip.src.players.ai_player import AIPlayer


class RandomAI(AIPlayer):
    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__(player_num, config, other_players)
        self.coords_list = []
        for row_index in range(self.board.num_rows):
            for col_index in range(self.board.num_cols):
                coords_tup = (row_index, col_index)
                self.coords_list.append(coords_tup)

    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
        self.name = f"Random Ai {player_num}"

    def get_move(self) -> move.Move:
        firing_location = random.choice(self.coords_list)
        self.coords_list.remove(firing_location)
        row = str(firing_location[0])
        col = str(firing_location[1])
        str_coords = row + ',' + col
        firing_location = move.Move.from_str(self, str_coords)
        return firing_location
