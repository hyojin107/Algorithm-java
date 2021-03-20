import time
N, M = map(int, input().split())
A, B, d = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(N)]

start_time = time.time()

direction = [
    [-1, 0], [0, 1], [1, 0], [0, -1]
]

end = False

result = 1
turn_count = 0

while True:
    # 왼쪽으로 회전
    d = d - 1 if d != 0 else 3
    turn_count += 1

    move_A = A + direction[d][0]
    move_B = B + direction[d][1]

    if game_map[move_A][move_B] == 1:
        if turn_count == 3:
            # 바라보는 방향 유지하며 뒤로 이동
            move_d = d - 2 if d != 0 else 2
            A += direction[move_d][0]
            B += direction[move_d][1]
            turn_count = 0
            if game_map[A][B] == 1:
                break
    else:
        game_map[A][B] = 1
        A = move_A
        B = move_B
        turn_count = 0
        result += 1

end_time = time.time()

print("time : ", end_time - start_time)
print(result)
