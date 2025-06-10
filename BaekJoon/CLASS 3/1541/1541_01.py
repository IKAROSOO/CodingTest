cal = input()

num_list = list()
bool_list = list()
cal_list = list()

tmp = ""

for char in cal:
    if char != "+" and char != "-":
        tmp += char
    else:
        num_list.append(int(tmp))
        tmp = ""
        
        bool_list.append(char)
num_list.append(int(tmp))

if "-" not in bool_list:
    print(sum(num_list))
    exit()

tmp = num_list[0]
for i in range(len(bool_list)):
    if bool_list[i] == "+":
        tmp += num_list[i+1]
    else:
        cal_list.append(tmp)
        tmp = num_list[i+1]
cal_list.append(tmp)

cnt = cal_list[0]

for i in range(1, len(cal_list)):
    cnt -= cal_list[i]
    
print(cnt)