phone_num = input()
n = len(phone_num)
time = 0

dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

for i in range(n):
    for j in dial:
        if i in j:
            time += dial.index(i) + 3
        
print(time)