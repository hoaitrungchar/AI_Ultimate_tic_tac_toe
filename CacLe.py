import math, time
import numpy as np
from state import UltimateTTT_Move


ai = -1


# func 1
def checkWinCondition(board):
    a = 1
    if (
        board[0] + board[1] + board[2] == a * 3
        or board[3] + board[4] + board[5] == a * 3
        or board[6] + board[7] + board[8] == a * 3
        or board[0] + board[3] + board[6] == a * 3
        or board[1] + board[4] + board[7] == a * 3
        or board[2] + board[5] + board[8] == a * 3
        or board[0] + board[4] + board[8] == a * 3
        or board[2] + board[4] + board[6] == a * 3
    ):
        return a
    a = -1
    if (
        board[0] + board[1] + board[2] == a * 3
        or board[3] + board[4] + board[5] == a * 3
        or board[6] + board[7] + board[8] == a * 3
        or board[0] + board[3] + board[6] == a * 3
        or board[1] + board[4] + board[7] == a * 3
        or board[2] + board[5] + board[8] == a * 3
        or board[0] + board[4] + board[8] == a * 3
        or board[2] + board[4] + board[6] == a * 3
    ):
        return a
    return 0


# func 2
def minimax(position, board_to_play_on, depth, alpha, beta, maximizing):
    temp_board = -1
    calcEval = evaluateGame(position, board_to_play_on)
    if depth <= 0 or abs(calcEval) > 5000:
        return {"mE": calcEval, "tB": temp_board}
    if board_to_play_on != -1 and checkWinCondition(position[board_to_play_on]) != 0:
        board_to_play_on = -1
    if board_to_play_on != -1 and not np.any(position[board_to_play_on] == 0):
        board_to_play_on = -1

    if maximizing:
        maxEval = -math.inf
        for mm in range(9):
            evaluation = -math.inf
            # If you can play on any board, you have to go through all of them
            if board_to_play_on == -1:
                for idx in range(9):
                    if not checkWinCondition(position[mm]):
                        if position[mm][idx] == 0:
                            position[mm][idx] = ai
                            evaluation = minimax(
                                position, idx, depth - 1, alpha, beta, False
                            )["mE"]
                            position[mm][idx] = 0
                    if evaluation > maxEval:
                        maxEval = evaluation
                        temp_board = mm
                    alpha = max(alpha, evaluation)
                if alpha >= beta:
                    break
            else:
                if position[board_to_play_on][mm] == 0:
                    position[board_to_play_on][mm] = ai
                    evaluation = minimax(position, mm, depth - 1, alpha, beta, False)
                    position[board_to_play_on][mm] = 0
                if type(evaluation) is dict:
                    if evaluation["mE"] > maxEval:
                        maxEval = evaluation["mE"]
                        temp_board = evaluation["tB"]
                    alpha = max(alpha, evaluation["mE"])
                if alpha >= beta:
                    break
        return {"mE": maxEval, "tB": temp_board}
    else:
        minEval = math.inf
        for mm in range(9):
            evaluation = math.inf
            if board_to_play_on == -1:
                for idx in range(9):
                    if not checkWinCondition(position[mm]):
                        if position[mm][idx] == 0:
                            position[mm][idx] = -ai
                            evaluation = minimax(
                                position, idx, depth - 1, alpha, beta, True
                            )["mE"]
                            position[mm][idx] = 0
                        if evaluation < minEval:
                            minEval = evaluation
                            temp_board = mm
                        beta = min(beta, evaluation)
                    if beta <= alpha:
                        break
            else:
                if position[board_to_play_on][mm] == 0:
                    position[board_to_play_on][mm] = -ai
                    evaluation = minimax(position, mm, depth - 1, alpha, beta, True)
                    position[board_to_play_on][mm] = 0

                if type(evaluation) is dict:
                    if evaluation["mE"] < minEval:
                        minEval = evaluation["mE"]
                        temp_board = evaluation["tB"]
                    beta = min(beta, evaluation["mE"])
                if beta <= alpha:
                    break
        return {"mE": minEval, "tB": temp_board}


# func 3
def evaluateGame(position, curr_board_index):
    val = 0
    main_bd = []
    eval_mul = [1.4, 1, 1.4, 1, 1.75, 1, 1.4, 1, 1.4]
    for i in range(9):
        val += realEvaluateSquare(position[i]) * 1.5 * eval_mul[i]
        if i == curr_board_index:
            val += realEvaluateSquare(position[i]) * eval_mul[i]
        tmpEv = checkWinCondition(position[i])
        val -= tmpEv * eval_mul[i]
        main_bd.append(tmpEv)

    val -= checkWinCondition(main_bd) * 5000
    val += realEvaluateSquare(main_bd) * 150
    return val


# func 4
def realEvaluateSquare(curr_board):
    evaluation = 0
    points = [0.2, 0.17, 0.2, 0.17, 0.22, 0.17, 0.2, 0.17, 0.2]

    for i in range(9):
        evaluation -= curr_board[i] * points[i]

    a = 2
    if (
        curr_board[0] + curr_board[1] + curr_board[2] == a
        or curr_board[3] + curr_board[4] + curr_board[5] == a
        or curr_board[6] + curr_board[7] + curr_board[8] == a
    ):
        evaluation -= 6
    if (
        curr_board[0] + curr_board[3] + curr_board[6] == a
        or curr_board[1] + curr_board[4] + curr_board[7] == a
        or curr_board[2] + curr_board[5] + curr_board[8] == a
    ):
        evaluation -= 6
    if (
        curr_board[0] + curr_board[4] + curr_board[8] == a
        or curr_board[2] + curr_board[4] + curr_board[6] == a
    ):
        evaluation -= 7
    a = -1
    if (
        (curr_board[0] + curr_board[1] == 2 * a and curr_board[2] == -a)
        or (curr_board[1] + curr_board[2] == 2 * a and curr_board[0] == -a)
        or (curr_board[0] + curr_board[2] == 2 * a and curr_board[1] == -a)
        or (curr_board[3] + curr_board[4] == 2 * a and curr_board[5] == -a)
        or (curr_board[3] + curr_board[5] == 2 * a and curr_board[4] == -a)
        or (curr_board[5] + curr_board[4] == 2 * a and curr_board[3] == -a)
        or (curr_board[6] + curr_board[7] == 2 * a and curr_board[8] == -a)
        or (curr_board[6] + curr_board[8] == 2 * a and curr_board[7] == -a)
        or (curr_board[7] + curr_board[8] == 2 * a and curr_board[6] == -a)
        or (curr_board[0] + curr_board[3] == 2 * a and curr_board[6] == -a)
        or (curr_board[0] + curr_board[6] == 2 * a and curr_board[3] == -a)
        or (curr_board[3] + curr_board[6] == 2 * a and curr_board[0] == -a)
        or (curr_board[1] + curr_board[4] == 2 * a and curr_board[7] == -a)
        or (curr_board[1] + curr_board[7] == 2 * a and curr_board[4] == -a)
        or (curr_board[4] + curr_board[7] == 2 * a and curr_board[1] == -a)
        or (curr_board[2] + curr_board[5] == 2 * a and curr_board[8] == -a)
        or (curr_board[2] + curr_board[8] == 2 * a and curr_board[5] == -a)
        or (curr_board[5] + curr_board[8] == 2 * a and curr_board[2] == -a)
        or (curr_board[0] + curr_board[4] == 2 * a and curr_board[8] == -a)
        or (curr_board[0] + curr_board[8] == 2 * a and curr_board[4] == -a)
        or (curr_board[4] + curr_board[8] == 2 * a and curr_board[0] == -a)
        or (curr_board[2] + curr_board[4] == 2 * a and curr_board[6] == -a)
        or (curr_board[2] + curr_board[6] == 2 * a and curr_board[4] == -a)
        or (curr_board[4] + curr_board[6] == 2 * a and curr_board[2] == -a)
    ):
        evaluation -= 9

    a = -2
    if (
        curr_board[0] + curr_board[1] + curr_board[2] == a
        or curr_board[3] + curr_board[4] + curr_board[5] == a
        or curr_board[6] + curr_board[7] + curr_board[8] == a
    ):
        evaluation += 6
    if (
        curr_board[0] + curr_board[3] + curr_board[6] == a
        or curr_board[1] + curr_board[4] + curr_board[7] == a
        or curr_board[2] + curr_board[5] + curr_board[8] == a
    ):
        evaluation += 6
    if (
        curr_board[0] + curr_board[4] + curr_board[8] == a
        or curr_board[2] + curr_board[4] + curr_board[6] == a
    ):
        evaluation += 7
    a = 1
    if (
        (curr_board[0] + curr_board[1] == 2 * a and curr_board[2] == -a)
        or (curr_board[1] + curr_board[2] == 2 * a and curr_board[0] == -a)
        or (curr_board[0] + curr_board[2] == 2 * a and curr_board[1] == -a)
        or (curr_board[3] + curr_board[4] == 2 * a and curr_board[5] == -a)
        or (curr_board[3] + curr_board[5] == 2 * a and curr_board[4] == -a)
        or (curr_board[5] + curr_board[4] == 2 * a and curr_board[3] == -a)
        or (curr_board[6] + curr_board[7] == 2 * a and curr_board[8] == -a)
        or (curr_board[6] + curr_board[8] == 2 * a and curr_board[7] == -a)
        or (curr_board[7] + curr_board[8] == 2 * a and curr_board[6] == -a)
        or (curr_board[0] + curr_board[3] == 2 * a and curr_board[6] == -a)
        or (curr_board[0] + curr_board[6] == 2 * a and curr_board[3] == -a)
        or (curr_board[3] + curr_board[6] == 2 * a and curr_board[0] == -a)
        or (curr_board[1] + curr_board[4] == 2 * a and curr_board[7] == -a)
        or (curr_board[1] + curr_board[7] == 2 * a and curr_board[4] == -a)
        or (curr_board[4] + curr_board[7] == 2 * a and curr_board[1] == -a)
        or (curr_board[2] + curr_board[5] == 2 * a and curr_board[8] == -a)
        or (curr_board[2] + curr_board[8] == 2 * a and curr_board[5] == -a)
        or (curr_board[5] + curr_board[8] == 2 * a and curr_board[2] == -a)
        or (curr_board[0] + curr_board[4] == 2 * a and curr_board[8] == -a)
        or (curr_board[0] + curr_board[8] == 2 * a and curr_board[4] == -a)
        or (curr_board[4] + curr_board[8] == 2 * a and curr_board[0] == -a)
        or (curr_board[2] + curr_board[4] == 2 * a and curr_board[6] == -a)
        or (curr_board[2] + curr_board[6] == 2 * a and curr_board[4] == -a)
        or (curr_board[4] + curr_board[6] == 2 * a and curr_board[2] == -a)
    ):
        evaluation += 9

    evaluation -= checkWinCondition(curr_board) * 12
    return evaluation


# func 5
def evaluatePos(pos, square):
    pos[square] = ai
    evalua = 0
    points = np.array([0.2, 0.17, 0.2, 0.17, 0.22, 0.17, 0.2, 0.17, 0.2])
    a = 2
    evalua += points[square]
    a = -2
    if (
        pos[0] + pos[1] + pos[2] == a
        or pos[3] + pos[4] + pos[5] == a
        or pos[6] + pos[7] + pos[8] == a
        or pos[0] + pos[3] + pos[6] == a
        or pos[1] + pos[4] + pos[7] == a
        or pos[2] + pos[5] + pos[8] == a
        or pos[0] + pos[4] + pos[8] == a
        or pos[2] + pos[4] + pos[6] == a
    ):
        evalua += 1
    a = -3
    if (
        pos[0] + pos[1] + pos[2] == a
        or pos[3] + pos[4] + pos[5] == a
        or pos[6] + pos[7] + pos[8] == a
        or pos[0] + pos[3] + pos[6] == a
        or pos[1] + pos[4] + pos[7] == a
        or pos[2] + pos[5] + pos[8] == a
        or pos[0] + pos[4] + pos[8] == a
        or pos[2] + pos[4] + pos[6] == a
    ):
        evalua += 5

    # Block a player's turn if necessary
    pos[square] = -ai

    a = 3
    if (
        pos[0] + pos[1] + pos[2] == a
        or pos[3] + pos[4] + pos[5] == a
        or pos[6] + pos[7] + pos[8] == a
        or pos[0] + pos[3] + pos[6] == a
        or pos[1] + pos[4] + pos[7] == a
        or pos[2] + pos[5] + pos[8] == a
        or pos[0] + pos[4] + pos[8] == a
        or pos[2] + pos[4] + pos[6] == a
    ):
        evalua += 2
    pos[square] = ai
    evalua -= checkWinCondition(pos) * 15
    pos[square] = 0
    return evalua


moves = 0
remainTime = 120


def select_move(cur_state, remain_time):
    global moves, remainTime
    start_t = time.time()
    valid_moves = cur_state.get_valid_moves
    main_board = np.copy(cur_state.global_cells, order="K")
    boards = np.copy(cur_state.blocks, order="K")

    my_move = UltimateTTT_Move(-1, -1, -1, cur_state.player_to_move)
    best_move = -1
    best_score = [
        -math.inf,
        -math.inf,
        -math.inf,
        -math.inf,
        -math.inf,
        -math.inf,
        -math.inf,
        -math.inf,
        -math.inf,
    ]

    cur_board = (
        cur_state.previous_move.x * 3 + cur_state.previous_move.y
        if cur_state.previous_move
        else -1
    )

    # 9x3x3 np array
    if cur_state.player_to_move == 1:
        boards = boards * -1
        main_board *= -1
    # flatten to 9x9 python list
    boards = boards.reshape(9, 9)
    # Calculates the remaining amount of empty squares for depth of minimax
    count = 0
    for board in boards:
        if checkWinCondition(board) == 0:
            count += board.size - np.count_nonzero(board)

    # current board has a winnner then cal the big square to move next
    if cur_board == -1 or checkWinCondition(boards[cur_board]) != 0:
        savedMm = 0
        depth = 4
        if np.count_nonzero(main_board == 0) < 4:
            depth = 5
        if np.count_nonzero(main_board == 0) < 3:
            depth = 6
        savedMm = minimax(boards, -1, min(depth, count), -math.inf, math.inf, True)

        # if moves < 10:
        #     savedMm = minimax(boards, -1, min(4, count), -math.inf, math.inf, True)
        # elif moves < 18:
        #     savedMm = minimax(boards, -1, min(5, count), -math.inf, math.inf, True)
        # else:
        #     savedMm = minimax(boards, -1, min(6, count), -math.inf, math.inf, True)
        cur_board = savedMm["tB"]
    for i in range(9):
        if boards[cur_board][i] == 0:
            best_move = i
            break
    if best_move != -1:
        for a in range(9):
            if boards[cur_board][a] == 0:
                score = evaluatePos(boards[cur_board], a) * 45
                best_score[a] = score
        for b in range(9):
            if checkWinCondition(boards[cur_board]) == 0:
                if boards[cur_board][b] == 0:
                    boards[cur_board][b] = ai
                    savedMm = 0
                    depth = 4
                    if np.count_nonzero(main_board == 0) < 4:
                        depth = 5
                    if np.count_nonzero(main_board == 0) < 3:
                        depth = 6
                    savedMm = minimax(
                        boards, b, min(depth, count), -math.inf, math.inf, False
                    )
                    # if moves < 18:
                    #     savedMm = minimax(
                    #         boards, b, min(4, count), -math.inf, math.inf, False
                    #     )
                    # else:
                    #     savedMm = minimax(
                    #         boards, b, min(5, count), -math.inf, math.inf, False
                    #     )
                    # if moves < 20:
                    #     savedMm = minimax(
                    #         boards, b, min(5, count), -math.inf, math.inf, False
                    #     )
                    # elif moves < 32:
                    #     savedMm = minimax(
                    #         boards, b, min(6, count), -math.inf, math.inf, False
                    #     )
                    # else:
                    #     savedMm = minimax(
                    #         boards, b, min(7, count), -math.inf, math.inf, False
                    #     )
                    score2 = savedMm["mE"]
                    boards[cur_board][b] = 0
                    best_score[b] += score2
        for i in range(len(best_score)):
            if best_score[i] > best_score[best_move]:
                best_move = i
    my_move.index_local_board = cur_board
    my_move.x = best_move // 3
    my_move.y = best_move % 3
    elapsed_time = time.time() - start_t
    remainTime -= elapsed_time

    # print(f"{moves}: {elapsed_time} - {remainTime}")
    moves += 1
    print("Cac",elapsed_time)
    return my_move
