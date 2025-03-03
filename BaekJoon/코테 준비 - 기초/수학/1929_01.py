def Prime_Number(number):
    if number == 1:
        return False
    if number == 2 :
        return True
    if number % 2 == 0:
        return False
    
    for i in range(3, int(number**0.5)+1, 2):
        if number % i == 0:
            return False

    return True

m, n = map(int, input().split())
nums = [i for i in range(m, n+1)]
# nums = range(m, n+1)  -> 해당 방식이 더 효율적

for num in nums:
    if Prime_Number(num):
        print(num)


'''
시간복잡도 : O(n^(3/2))
'''