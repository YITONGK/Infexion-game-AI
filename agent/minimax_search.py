from referee.game import Board, PlayerColor, SpreadAction, SpawnAction, HexPos, HexDir, Action
from referee.game.board import CellState

from .utils import apply_action


def minimax(action_list: list[Action], curr_board: Board):
    return

# assign utility value to each action in the list and return as a dict
def assign_utility(curr_board: Board, action_list: list[Action], color: PlayerColor) -> dict[Action, int]:
    action_dict = {}
    for action in action_list:
        utility = calculate_utility(curr_board, action, color)
        action_dict[action] = utility
    return action_dict

# initially use power difference before and after an action applies to the current board as utility value
def calculate_utility(curr_board: Board, action: Action, color: PlayerColor) -> int:
    initial_power_difference = calculate_power_difference(curr_board._state, color)
    temp_state = curr_board._state.copy()
    # temp_board.apply_action(action)
    apply_action(temp_state, action, color)
    final_power_difference = calculate_power_difference(temp_state, color)
    return final_power_difference - initial_power_difference

def calculate_power_difference(state: dict[HexPos, CellState], color: PlayerColor):
    my_power = 0
    oppo_power = 0
    for key in state:
        cellstate = state[key]
        if cellstate.player == color:
            my_power += cellstate.power
        else:
            oppo_power += cellstate.power
    return my_power - oppo_power





