from abc import ABC
from typing import List

from BattleShip.src import move, game_config, cell
from BattleShip.src.player import Player
from BattleShip.src.players.ai_player import AIPlayer


class CheatingAI(AIPlayer, ABC):
    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__(player_num, config, other_players)

    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
        self.name = f"Cheating Ai {player_num}"

    def get_move(self) -> move.Move:
        opponent = self.opponents[0]
        for row_index in range(self.board.num_rows):
            for col_index in range(self.board.num_cols):
                if opponent.board.has_been_fired_at(row_index, col_index):
                    continue
                elif opponent.board.contents[row_index][col_index].content == "*":
                    continue
                else:
                    row = str(row_index)
                    col = str(col_index)
                    str_coords = row + ',' + col
                    firing_location = move.Move.from_str(self, str_coords)
                    return firing_location
                    continue



