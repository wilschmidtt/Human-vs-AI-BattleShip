from typing import List
import random
from BattleShip.src import move, game_config
from BattleShip.src.player import Player
from BattleShip.src.players.ai_player import AIPlayer
from collections import deque


class SearchDestroyAI(AIPlayer):
    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__(player_num, config, other_players)
        self.coords_list = []
        self.previous_move = []
        self.opponents = other_players[:]

        for row_index in range(self.board.num_rows):
            for col_index in range(self.board.num_cols):
                coords_tup = (row_index, col_index)
                self.coords_list.append(coords_tup)

    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
        self.name = f"Search Destroy AI {player_num}"

    def get_move(self) -> move.Move:
        if len(self.previous_move) > 0:
            prev_row, prev_col = self.previous_move[0].split(',')

        while len(self.previous_move) > 0 and self.opponents[0].board.contents[int(prev_row)][int(prev_col)].contains_ship():
            if (int(prev_row), int(prev_col) - 1) not in self.coords_list and (
            int(prev_row) - 1, int(prev_col)) not in self.coords_list and (
            int(prev_row), int(prev_col) + 1) not in self.coords_list and (
            int(prev_row) + 1, int(prev_col)) not in self.coords_list:
                del self.previous_move[0]
                prev_row, prev_col = self.previous_move[0].split(',')

            if (int(prev_row), int(prev_col)-1) in self.coords_list:
                firing_location = (int(prev_row), int(prev_col)-1)
                self.coords_list.remove(firing_location)
                row = str(firing_location[0])
                col = str(firing_location[1])
                str_coords = row + ',' + col
                firing_location = move.Move.from_str(self, str_coords)
                if self.opponents[0].board.contents[int(row)][int(col)].content != "*" and self.opponents[0].board.contents[int(row)][int(col)].content != "O":
                    self.previous_move.append(str_coords)
                if (int(prev_row), int(prev_col)-1) not in self.coords_list and (int(prev_row) -1, int(prev_col)) not in self.coords_list and (int(prev_row), int(prev_col) + 1) not in self.coords_list and (int(prev_row) + 1, int(prev_col)) not in self.coords_list:
                    del self.previous_move[0]
                return firing_location

            elif (int(prev_row) -1, int(prev_col)) in self.coords_list:
                firing_location = (int(prev_row) -1, int(prev_col))
                self.coords_list.remove(firing_location)
                row = str(firing_location[0])
                col = str(firing_location[1])
                str_coords = row + ',' + col
                firing_location = move.Move.from_str(self, str_coords)
                if self.opponents[0].board.contents[int(row)][int(col)].content != "*" and self.opponents[0].board.contents[int(row)][int(col)].content != "O":
                    self.previous_move.append(str_coords)
                if (int(prev_row), int(prev_col)-1) not in self.coords_list and (int(prev_row) -1, int(prev_col)) not in self.coords_list and (int(prev_row), int(prev_col) + 1) not in self.coords_list and (int(prev_row) + 1, int(prev_col)) not in self.coords_list:
                    del self.previous_move[0]
                return firing_location

            elif (int(prev_row), int(prev_col) + 1) in self.coords_list:
                firing_location = (int(prev_row), int(prev_col) + 1)
                self.coords_list.remove(firing_location)
                row = str(firing_location[0])
                col = str(firing_location[1])
                str_coords = row + ',' + col
                firing_location = move.Move.from_str(self, str_coords)
                if self.opponents[0].board.contents[int(row)][int(col)].content != "*" and self.opponents[0].board.contents[int(row)][int(col)].content != "O":
                    self.previous_move.append(str_coords)
                if (int(prev_row), int(prev_col)-1) not in self.coords_list and (int(prev_row) -1, int(prev_col)) not in self.coords_list and (int(prev_row), int(prev_col) + 1) not in self.coords_list and (int(prev_row) + 1, int(prev_col)) not in self.coords_list:
                    del self.previous_move[0]
                return firing_location

            elif (int(prev_row) + 1, int(prev_col)) in self.coords_list:
                firing_location = (int(prev_row) + 1, int(prev_col))
                self.coords_list.remove(firing_location)
                row = str(firing_location[0])
                col = str(firing_location[1])
                str_coords = row + ',' + col
                firing_location = move.Move.from_str(self, str_coords)
                if self.opponents[0].board.contents[int(row)][int(col)].content != "*" and self.opponents[0].board.contents[int(row)][int(col)].content != "O":
                    self.previous_move.append(str_coords)
                if (int(prev_row), int(prev_col)-1) not in self.coords_list and (int(prev_row) -1, int(prev_col)) not in self.coords_list and (int(prev_row), int(prev_col) + 1) not in self.coords_list and (int(prev_row) + 1, int(prev_col)) not in self.coords_list:
                    del self.previous_move[0]
                return firing_location

        firing_location = random.choice(self.coords_list)
        self.coords_list.remove(firing_location)
        row = str(firing_location[0])
        col = str(firing_location[1])
        str_coords = row + ',' + col
        firing_location = move.Move.from_str(self, str_coords)
        if len(self.previous_move) > 0:
            del self.previous_move[0]
        self.previous_move.append(str_coords)
        return firing_location

    def hit_is_scored(self, row, col) -> bool:
        opponent = self.opponents[0]
        if not opponent.board.has_been_fired_at(row, col):
            if opponent.board.contents[row][col].content != '*':
                return True
        else:
            return False
