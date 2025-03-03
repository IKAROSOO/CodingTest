a, b = map(int, input().split())
LCM, GCD = 0, 0     #각각 최소공배수, 최대공약수의 약자

for i in range(1, max(a,b)+1):
    if a%i==0 and b%i==0:
        GCD = i
    
LCM = int(a*(b/GCD))

print(GCD)
print(LCM)

'''
시간복잡도 : O(n)
'''