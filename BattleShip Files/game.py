import itertools
from . import game_config
from .players import humanplayer, cheatingai, searchdestroyai, randomai
from . import player


class Game(object):

    def __init__(self, game_config_file: str, num_players: int = 2) -> None:
        super().__init__()
        self.game_config = game_config.GameConfig(game_config_file)
        self.players = []
        self.player_turn = 0
        self.setup_players(num_players)

    def setup_players(self, num_players: int) -> None:
        for player_num in range(1, num_players + 1):
            while True:
                player_type = input(
                    f"Enter one of ['Human', 'CheatingAi', 'SearchDestroyAi', 'RandomAi'] for Player {player_num}'s type: ")
                player_type = player_type.lower().strip()
                if 'Human'.lower().startswith(player_type):
                    self.players.append(humanplayer.HumanPlayer(player_num, self.game_config, self.players))
                    break

                elif 'CheatingAi'.lower().startswith(player_type):
                    self.players.append(cheatingai.CheatingAI(player_num, self.game_config, self.players))
                    break

                elif 'SearchDestroyAi'.lower().startswith(player_type):
                    self.players.append(searchdestroyai.SearchDestroyAI(player_num, self.game_config, self.players))
                    break

                elif 'RandomAi'.lower().startswith(player_type):
                    self.players.append(randomai.RandomAI(player_num, self.game_config, self.players))
                    break
                else:
                    print("Please enter a valid player type")
                    continue

    def play(self) -> None:
        active_player = self.players[0]
        for active_player in itertools.cycle(self.players):
            self.do_current_players_turn(active_player)
            if self.game_is_over():
                break
        print(f'{active_player} won the game!')

    def do_current_players_turn(self, cur_player: player.Player) -> None:
        self.display_gamestate(cur_player)
        while True:
            move = cur_player.get_move()
            move.make()
            if move.ends_turn():
                break

    @property
    def num_players(self) -> int:
        return len(self.players)

    def get_active_player(self) -> player.Player:
        return self.players[self.player_turn]

    def game_is_over(self) -> bool:
        return any(player_.all_ships_sunk() for player_ in self.players)

    def display_gamestate(self, cur_player: player.Player) -> None:
        cur_player.display_scanning_boards()
        cur_player.display_firing_board()
