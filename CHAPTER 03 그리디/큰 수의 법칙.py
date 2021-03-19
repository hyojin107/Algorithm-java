import time

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

start_time = time.time()

data.sort(reverse=True)
first = data[0]
second = data[1]

result = 0

while True:
    for _ in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

end_time = time.time()

print("time : ", end_time - start_time)
print(result)
