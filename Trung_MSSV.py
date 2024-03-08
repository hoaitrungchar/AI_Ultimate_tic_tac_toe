import numpy as np
import copy
from state import State, State_2,UltimateTTT_Move


def evaluationFunction(curState):
    miniwin=0
    for i in range (0,9):
        x= curState.game_result(curState.blocks[i].reshape(3,3))
        if not(x is None):
            if(x==0 or x==2 or x==6 or x==8):
                x=1.25
            elif(x==4):
                x=1.5            
            miniwin=miniwin+x
    y=curState.game_result(curState.global_cells.reshape(3,3))
    if(y is None):
        y=0
    return 9999*y +miniwin

def generateSuc(curState,valid_moves):
    newCurState = copy.deepcopy(curState)
    newCurState.act_move(valid_moves)
    return  newCurState

def a_b_min_max(curState,depth,alpha,beta):
    if curState.game_over or depth<=0:
        return (evaluationFunction(curState),  (-1,-1,-1,-1))
    moves=curState.get_valid_moves
    if(len(moves)<1):
        return (evaluationFunction(curState),  (-1,-1,-1,-1))
    elif len(moves)>=28 and depth>2:
         depth=depth-1
    x=(-1,-1,-1,-1)
    if curState.player_to_move == 1:
        ans = (-99999, (-1,-1,-1,-1))
        for action in moves:
            evaluate_action=a_b_min_max(generateSuc(curState,action), depth - 1, alpha, beta)[0]
            # print(ans[0])
            # print(evaluate_action)
            if(ans[0]<=evaluate_action):
                x=(copy.deepcopy(action.index_local_board),copy.deepcopy(action.x),copy.deepcopy(action.y),copy.deepcopy(action.value))
                ans=(evaluate_action,x)
            if(ans[0]>alpha[0]):
                alpha=ans
            if alpha[0] >= beta[0]:
                break;
        # if x[0]==-1:
        #     print(2)
        # print("alpha", alpha)
        return alpha
    else:
        ans = (99999, (-1,-1,-1,-1))
        for action in moves:
            evaluate_action=a_b_min_max(generateSuc(curState,action), depth - 1, alpha, beta)[0]
            if(ans[0]>=evaluate_action):
                x=(copy.deepcopy(action.index_local_board),copy.deepcopy(action.x),copy.deepcopy(action.y),copy.deepcopy(action.value))
                ans=(evaluate_action,x)
            if(ans[0]<beta[0]):
               beta=ans
            if alpha[0] >= beta[0]:
                break
        # print("beta",beta)
        return beta


def select_move(cur_state, remain_time):
    if(cur_state.previous_move is None):
        return UltimateTTT_Move(4,1,1,1)
    valid_moves = cur_state.get_valid_moves
    depth=3
    alpha = (-9999, (-1,-1,-1,-1))
    beta = (+9999,  (-1,-1,-1,-1))
    action = a_b_min_max(cur_state, 2*depth, alpha, beta)[1]
    # print(action)
    if action[0]!=-1:
        return UltimateTTT_Move(action[0],action[1],action[2],action[3])
    else:
        if len(valid_moves) != 0:
            return np.random.choice(valid_moves)
        return None
    return None

