def solution(bin1, bin2):
    dec_sum = int(bin1, 2) + int(bin2, 2)
    bin_sum = bin(dec_sum)[2:]

    return bin_sum