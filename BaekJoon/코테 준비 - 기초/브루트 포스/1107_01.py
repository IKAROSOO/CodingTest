def is_valid(num_str, broken):
    for char in num_str:
        if int(char) in broken:
            return False
    return True

def remote(channel_num, broken):
    current_channel = 100

    min_cnt = abs(channel_num - current_channel)

    for channel in range(1000000):
        channel_str = str(channel)

        if is_valid(channel_str, broken):
            min_cnt = min(min_cnt, len(channel_str) + abs(channel_num - channel))
    
    return min_cnt

channel = int(input())
M = int(input())

if M:
    broken = list(map(int, input().split()))
else:
    broken = []

print(remote(channel, broken))