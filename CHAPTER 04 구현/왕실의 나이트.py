import time
point = input()
x, y = int(ord(point[0])) - ord('a') + 1, int(point[1])

start_time = time.time()

move = [
    [-2, -1], [-2, 1], [2, -1], [2, 1],
    [-1, -2], [-1, 2], [1, -2], [1, 2]
]

result = 0

for i in move:
    move_x = x + i[0]
    move_y = y + i[1]
    if move_x < 1 or move_x > 8 or move_y < 1 or move_y > 8:
        continue
    result += 1

end_time = time.time()

print("time : ", end_time - start_time)
print(result)
