def solution(id_pw, db):
    identify, password = id_pw[0], id_pw[1]

    for user_data in db:
        if user_data[0] == identify:
            if user_data[1] == password:
                return "login"
            else:
                return "wrong pw"
    else:    
        return "fail"

    # -> for문이 전부 동작했을 경우, else문이 실행된다.
    # -> 중간에 for문이 break되는 경우, else문은 실행되지 않는다.