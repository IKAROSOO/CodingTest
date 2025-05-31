def solution(fees, records):
    record_dict = dict()    # 주차 시간 저장
    parkingTime = dict()    # 입차 기록 저장
    fee_list = list()       # 요금 정산
    carNum_list = list()    # 차량 번호 저장

    for record in records:
        time, car_num, breakdown = record.split(" ")

        if car_num not in parkingTime:
            parkingTime[car_num] = 0
            carNum_list.append(car_num)
        
        if car_num not in record_dict:
            record_dict[car_num] = time
        else:
            parkingTime[car_num] += TimeCalculate(time, record_dict[car_num])
            del record_dict[car_num]

    for car_num, parkedTime in record_dict.items():     # 주차장에 남아있는 차량 조회
        parkingTime[car_num] += TimeCalculate("23:59", parkedTime)
    
    carNum_list.sort()

    for carNum in carNum_list:
        if parkingTime[carNum] <= fees[0]:
            fee_list.append(fees[1])
        else:
            parkingtime = parkingTime[carNum] - fees[0]
            if parkingtime%fees[2] != 0:
                fee = fees[1] + (parkingtime//fees[2] + 1)*fees[3]
            else:
                fee = fees[1] + (parkingtime//fees[2])*fees[3]
            fee_list.append(fee)
    
    return fee_list

def TimeCalculate(time1, time2):
    parts1 = time1.split(":")
    minutes1 = int(parts1[1]) + int(parts1[0])*60

    parts2 = time2.split(":")
    minutes2 = int(parts2[1]) + int(parts2[0])*60
    
    return abs(minutes1 - minutes2)