from math import inf 
from collections import Counter
from state import UltimateTTT_Move
import copy
from timeit import default_timer as timer
import random

global turns 
turns = 1 

global evaluate_score1
evaluate_score1=[-1.87528548e+00,-1.49153326e+00,-1.06928951e+00,-1.83471616e+00,-1.52843050e+00,-1.14519467e+00,-1.67075826e+00,1.02961282e-01,4.75369405e-03,-1.64258786e+00,2.94065672e-02,-5.24613843e-02,-1.72804517e+00,1.87700434e-01,-1.37226404e-02,-1.68969029e+00,-5.88584151e-02,-1.70561899e-01,-1.67582253e+00,-3.08464184e-02,-4.66468293e-02,-1.79476605e+00,-1.82863604e-02,-4.23998768e-02,-3.80836229e-01,1.41988562e-01,9.40871464e-02,-3.69173390e-01,4.06886720e-02,3.32163685e-02,-5.03398254e-01,7.92580909e-02,-4.98126309e-02,-2.97675889e-01,1.18295200e-01,4.22296534e-02,-4.06526256e-01,1.81525350e-01,3.93268068e-02,-4.07652459e-01,2.84423263e-02,4.95359965e-02,-2.90705047e-01,1.64217960e-01,7.90727938e-02,-3.83718350e-01,9.10107626e-02,-4.36790488e-02,-3.62826079e-01,1.30903851e-01,1.22706683e-01,-3.35036161e-01,1.93116971e-01,4.00056720e-02,-3.36915660e-01,5.50884698e-02,2.20019563e-02,-4.02311484e-01,5.47065227e-02,-7.98014960e-02,-2.54896499e-01,6.76662285e-02,1.19976905e-01,-4.38448875e-01,1.40439987e-01,9.61817015e-02,-4.10316953e-01,4.83820094e-02,-1.16602945e-02,-3.48992624e-01,3.47562278e-02,-3.53320706e-02,-2.33576660e-01,9.15948420e-02,8.15461960e-02,-4.27970023e-01,9.52833375e-02,6.24648201e-03,-3.24134279e-01,1.04882351e-01,5.20543739e-02,-3.12587427e-01,6.49229314e-02,-2.53694613e-02,-3.57751524e-01,1.59754745e-01,7.28049853e-02,-3.26393090e-01,1.05255083e-01,4.52856201e-02,-2.87244448e-01,1.49411620e-01,3.23904085e-02,-3.11249912e-01,-7.83172897e-03,-4.30549695e-02,-2.89257347e-01,7.74931803e-02,-2.35538460e-02,-3.80042312e-01,1.04594392e-01,6.25971312e-02,-5.23842261e-01,5.73010321e-02,-2.24893709e-03,-3.62679461e-01,1.13888516e-01,5.59250882e-02,-3.93168406e-01,3.17514455e-02,1.11845944e-01,-3.18919432e-01,3.77707901e-02,5.80558724e-03,-4.44857222e-01,7.00179116e-02,-2.62999755e-02,-3.59888041e-01,9.04588458e-02,8.53025085e-03,-3.85355975e-01,-4.15171905e-02,2.83729184e-02,-3.59681744e-01,6.68607400e-02,6.01450225e-02,-3.61491562e-01,-1.28149492e-02,3.93400013e-02,-2.81514656e-01,3.53155113e-02,4.19362952e-02,-2.31397450e-01,8.83586356e-02,1.28499414e-02,-3.12525496e-01,2.20544622e-01,1.35927845e-02,-2.37197823e-01,5.96480753e-02,-1.01094879e-02,-4.05208854e-01,1.75361921e-01,6.18085209e-02,-2.63596856e-01,4.90003195e-02,3.91144439e-03,-4.00155376e-01,4.12244577e-02,3.10269371e-02,-2.24966376e-01,1.13117400e-01,1.49161221e-01,-3.42909324e-01,5.65351403e-02,-1.60441873e-02,-3.60639309e-01,3.20749554e-02,2.11021708e-02,-4.26572466e-01,1.19027038e-01,2.73387107e-02,-4.30409536e-01,1.24488758e-02,1.04611889e-01,-2.78012785e-01,1.55769436e-01,-3.75266182e-02,-2.34585628e-01,9.43272331e-02,2.00223599e-02,-4.15586523e-01,-6.69698771e-02,4.56507212e-02,-4.54892446e-01,7.88085981e-02,-3.15918731e-02,-3.61096690e-01,9.14076202e-02,6.36131952e-03,-2.52402031e-01,1.79530643e-01,1.28857962e-01,-3.32867038e-01,1.14613249e-01,6.74360406e-02,-2.76618975e-01,1.44527507e-01,-1.71872744e-02,-3.61133063e-01,6.67953504e-02,1.53614323e-02,-3.93269441e-01,6.01518385e-02,5.35602267e-02,-2.51140286e-01,3.68261604e-02,5.17799733e-02,-3.47715491e-01,1.44071543e-01,8.55285205e-02,-3.22506203e-01,4.61690625e-02,1.17385878e-01,-3.33759334e-01,1.40255118e-01,3.57327302e-02,-1.80198959e-01,9.83177481e-02,1.90801731e-02,-3.49278656e-01,1.31359685e-01,-5.67824193e-03,-3.44604327e-01,5.87377536e-02,4.39513115e-02,-3.93788841e-01,-3.41204051e-02,3.34743439e-02,-2.33083619e-01,9.96818119e-02,1.33460585e-01,-4.18825428e-01,7.66336015e-02,-4.35700181e-03,-2.68850640e-01,1.44570352e-01,-1.75168743e-03,-2.33459425e-01,3.05318734e-02,9.89642460e-02,-3.73627428e-01,5.58348874e-02,9.78394868e-02,-2.46342558e-01,1.30824389e-01,1.23722574e-01,-2.92611382e-01,1.58027606e-01,1.97153070e-02,7.22262478e+00,-4.32924824e-02,6.99178250e-01,7.28381826e+00,-1.91396248e-02,6.60256699e-01,6.88819584e+00,-1.58556630e-01,4.31980627e-01,6.78922405e+00,-1.49706027e-01,2.58139595e-01,7.00299715e+00,2.68309919e-02,3.68493957e-01,7.06725696e+00,5.61214000e-03,4.00070344e-01,7.00627063e+00,-1.80219025e-01,3.40240419e-01,6.96257625e+00,-8.86693249e-02,3.94882064e-01,2.92654528e-01,7.72900237e-02,1.56384121e-01,3.45679818e-01,1.79004220e-01,9.90113302e-02,2.60978142e-01,8.21836779e-02,2.50927591e-02,3.13423824e-01,-5.39810338e-02,-4.63399259e-02,2.22691802e-01,-2.21534197e-03,-6.78032759e-02,1.77557810e-01,1.13248308e-01,5.87085598e-02,3.38670552e-01,-2.05132265e-04,-7.05634875e-02,1.65686152e-01,1.27320785e-01,-2.44479473e-02,7.77022400e-02,1.05080836e-01,1.59314525e-01,2.48053367e-01,2.40391592e-01,1.27100302e-01,1.65024149e-01,3.44430505e-02,-7.20427305e-03,1.22714368e-01,-2.33905337e-02,-2.55469320e-02,2.74742417e-01,8.95125944e-02,-5.89366894e-02,1.22762936e-01,5.77992457e-02,-6.29919794e-03,2.40126556e-01,3.84564221e-02,5.31542660e-02,1.82728434e-01,7.42547980e-02,-1.69368101e-02,3.09672567e-01,1.02725904e-01,1.62833049e-01,4.42702834e-01,1.33805389e-01,3.35888730e-02,3.02703002e-01,8.46344128e-02,-6.39899510e-03,2.08517275e-01,1.64852264e-02,8.01286025e-02,2.26515698e-01,4.47451752e-02,2.59180861e-02,3.11646646e-01,-4.82368041e-02,1.30627955e-02,1.28630657e-01,-1.82565049e-02,6.23266920e-02,2.03276444e-01,4.29060444e-02,-6.16072971e-02,1.35114632e-01,1.36679795e-01,1.21985388e-01,1.61966663e-01,1.34908078e-01,1.07013062e-01,1.17939841e-01,1.17427325e-01,6.36147071e-02,1.54088511e-01,8.19800128e-02,3.21263263e-02,2.36897198e-01,-5.79798223e-02,1.23614525e-01,1.33795103e-01,3.44135610e-02,3.20138667e-02,8.31556520e-02,1.05786612e-01,-4.06671405e-02,1.70778742e-01,8.33041205e-02,4.24140259e-02,4.29229552e-01,9.15802399e-02,8.07908360e-02,5.23474769e-01,1.32466689e-01,1.03814736e-01,3.42177155e-01,-2.24988844e-02,-1.36547222e-01,3.40660208e-01,5.60352575e-02,-1.79457738e-02,3.47060399e-01,3.33743905e-02,8.67558322e-02,3.51503257e-01,6.41384881e-02,1.25329819e-01,2.96636687e-01,1.00855027e-01,6.81166457e-02,3.70217229e-01,1.59507737e-03,-3.98868394e-02,2.79622258e-01,1.48538279e-01,6.76029420e-02,1.32231719e-01,1.34695556e-01,1.16896040e-01,5.30963331e-02,-6.81265923e-03,4.39383302e-02,1.01034191e-01,-5.20163471e-02,1.89893680e-02,1.86228873e-01,6.87198673e-02,-1.31070432e-02,1.34257512e-01,-3.25655994e-03,1.19425566e-01,1.21260246e-01,2.63233796e-02,2.19859559e-02,2.01644011e-01,6.77941783e-02,4.87131950e-02,3.60806961e-01,8.91395509e-02,2.25021841e-01,2.73110218e-01,1.74686708e-01,-2.88558072e-02,2.71540619e-01,-6.40477363e-02,-1.56908118e-01,2.13486043e-01,8.86646063e-02,1.53325611e-02,2.87770498e-01,8.69255333e-02,5.68412170e-02,3.07938322e-01,1.13654443e-01,3.57439162e-02,3.98934180e-01,2.25849942e-03,2.14964624e-02,2.48347282e-01,1.36801498e-01,5.49874254e-02,2.90451640e-01,1.35454767e-01,1.05326648e-01,2.46082006e-01,1.75434243e-01,5.89223119e-02,2.97272615e-01,4.28187278e-02,1.07481722e-01,3.91210814e-02,6.88201053e-02,7.54842619e-02,2.06426827e-01,3.94105305e-02,8.34048464e-02,2.10833287e-01,5.11072785e-03,-3.69073191e-02,1.82944471e-01,7.94991529e-03,3.23691955e-02,-1.22716163e-01,4.83737074e-02,-5.31640227e-02,3.51864306e-01,3.70046046e-02,2.65507216e-03,3.09620815e-01,5.65726618e-02,8.92779453e-02,3.24963018e-01,-1.14444987e-02,-2.34090964e-02,3.49516087e-01,-3.75387613e-02,1.32511656e-01,2.93573845e-01,1.53702763e-01,5.70367130e-02,2.86432942e-01,-4.34200431e-02,-6.95755154e-02,2.45886014e-01,5.68122909e-02,-7.24680198e-02,3.73998338e-01,4.53284434e-02,9.01125261e-02]
def act_move(c_state, move):
    local_board = c_state.blocks[move.index_local_board]
    local_board[move.x, move.y] = move.value
    
    c_state.player_to_move *= -1
    c_state.previous_move = move

    if c_state.global_cells[move.index_local_board] == 0: # not 'X' or 'O'
        if c_state.game_result(local_board):
            c_state.global_cells[move.index_local_board] = move.value
    return c_state
    
def select_move(cur_state, remain_time):
    if turns < 10:
        depth = 5
    elif turns < 12:
        depth = 8
    elif turns < 15:
        depth = 11
    else:
        depth = 15
     
    start_time = timer()  
    if cur_state.previous_move == None:
        return UltimateTTT_Move(4, 0, 0, 1)
    valid_moves = cur_state.get_valid_moves
    if len(valid_moves) != 0:
        best_move = minimax(cur_state, valid_moves, depth, start_time, remain_time)
        return best_move
    return None

def minimax(cur_state, valid_moves, depth, start_time, remain_time):
    global possible_goals
    possible_goals = [([0,0], [1,1], [2,2]), ([0,2], [1,1], [2,0]),
                      ([0,0], [1,0], [2,0]), ([0,1], [1,1], [2,1]), 
                      ([0,2], [1,2], [2,2]), ([0,0], [0,1], [0,2]),
                      ([1,0], [1,1], [1,2]), ([2,0], [2,1], [2,2])]

    # best_move = (-inf, None)
    best_list_move = [(-inf, None)]
    for move in valid_moves:
        state = copy.deepcopy(cur_state)
        state = act_move(state, move)
        value = min_turn(state, depth-1, -inf, inf, start_time, remain_time)
        #print("Value") 
        #print(value)
        if value > best_list_move[0][0]:
            #best_move = (value, move)
            best_list_move = [(value, move)]
        if value == best_list_move[0][0]:
            best_list_move.append((value, move))
    print (timer()-start_time)
    print(best_list_move)
    if (best_list_move[0][0] != None):
        print(random.choice(best_list_move))
        return (random.choice(best_list_move))[1]  
    else:
        return random.choice(valid_moves)    

def min_turn(cur_state, depth, alpha, beta, start_time, remain_time):
    valid_moves = cur_state.get_valid_moves
    if depth <= 0 or len(valid_moves) == 0 or (timer() - start_time > 9.8) or (remain_time - (timer() - start_time) < 1):
        state = copy.deepcopy(cur_state)
        state.player_to_move *= (-1)
        return evaluate(state)
    
    
    for move in valid_moves:
        state = copy.deepcopy(cur_state)
        state = act_move(state, move)
        value = max_turn(state, depth-1, alpha, beta, start_time, remain_time)

        if value < beta:
            beta = value
        if alpha >= beta:
            break

    return beta

def max_turn(cur_state, depth, alpha, beta, start_time, remain_time):
    valid_moves = cur_state.get_valid_moves
    if depth <= 0 or len(valid_moves) == 0 or (timer() - start_time > 9.8) or (remain_time - (timer() - start_time) < 1):
        state = copy.deepcopy(cur_state)
        return evaluate(state)
    
    
    for move in valid_moves:
        state = copy.deepcopy(cur_state)
        state = act_move(state, move)
        # state.player_to_move *= (-1)
        value = min_turn(state, depth-1, alpha, beta, start_time, remain_time)

        if alpha < value:
            alpha = value
        if alpha >= beta:
            break

    return alpha

def evaluate(cur_state): 
    score = 0
    global_cells = copy.deepcopy(cur_state.global_cells)
    score += evaluate_small_box(cur_state, global_cells.reshape(3,3),0)
    for block_idx in range(9):
        block = cur_state.blocks[block_idx]
        score += evaluate_small_box(cur_state, block,block_idx+1)


    return score

def evaluate_small_box(cur_state, block,pos):
    global possible_goals
    score = 0

    player = copy.deepcopy(cur_state.player_to_move)

    pos_score=0
    if(player==1):
        pos_score=0
    else:
        pos_score=240
    
    three = Counter([player, player, player])
    two   = Counter([player, player, 0])
    one   = Counter([player, 0, 0])

    player = player*(-1)
    three_opponent = Counter([player, player, player])
    two_opponent   = Counter([player, player, 0])
    one_opponent   = Counter([player, 0, 0])



    for idxs in range(0,8):
        (x, y, z) = possible_goals[idxs]
        current = Counter([block[x[0]][x[1]], block[y[0]][y[1]]
                        , block[z[0]][z[1]]])
        if(player==1):
            if current == three:
                score += (evaluate_score1[idxs*3+pos_score+24*pos+0])
            elif current == two:
                score += (evaluate_score1[idxs*3+pos_score+24*pos+1])
            elif current == one:
                score += (evaluate_score1[idxs*3+pos_score+24*pos+2])
            elif current == three_opponent:
                score += (evaluate_score1[idxs*3+(240-pos_score)+24*pos+0])
                return score
            elif current == two_opponent:
                score += (evaluate_score1[idxs*3+(240-pos_score)+24*pos+1])
            elif current == one_opponent:
                score += (evaluate_score1[idxs*3+(240-pos_score)+24*pos+2])
        else:
            if current == three:
                score -= (evaluate_score1[idxs*3+pos_score+24*pos+0])
            elif current == two:
                score -= (evaluate_score1[idxs*3+pos_score+24*pos+1])
            elif current == one:
                score -= (evaluate_score1[idxs*3+pos_score+24*pos+2])
            elif current == three_opponent:
                score -= (evaluate_score1[idxs*3+(240-pos_score)+24*pos+0])
                return score
            elif current == two_opponent:
                score -= (evaluate_score1[idxs*3+(240-pos_score)+24*pos+1])
            elif current == one_opponent:
                score -= (evaluate_score1[idxs*3+(240-pos_score)+24*pos+2])

    return score
