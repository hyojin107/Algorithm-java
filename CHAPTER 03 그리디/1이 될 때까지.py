import time

n, k = map(int, input().split())

start_time = time.time()

result = 0

while n != 1:
    n = (n // k) if (n % k == 0) else (n - 1)
    result += 1

end_time = time.time()

print("time : ", end_time - start_time)
print(result)

