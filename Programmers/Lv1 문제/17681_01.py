def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        bin_num1 = format(arr1[i], f"0{n}b")
        bin_num2 = format(arr2[i], f"0{n}b")
        
        combined_str = ""
        
        for j in range(n):
            if bin_num1[j] == "1" or bin_num2[j] == "1":
                combined_str += "#"
            else:
                combined_str += " "
        answer.append(combined_str)
    
    return answer