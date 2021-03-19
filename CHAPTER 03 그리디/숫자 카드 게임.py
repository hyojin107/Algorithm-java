import time

n, m = map(int, input().split())
card = [list(map(int, input().split())) for _ in range(n)]

start_time = time.time()

result = 0

for i in range(len(card)):
    min_value = min(card[i])
    result = max(result, min_value)

end_time = time.time()

print("time : ", end_time - start_time)
print(result)

