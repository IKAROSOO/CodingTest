def solution(polynomial):
    polynomial = polynomial.strip() # 양쪽 공백 제거
    terms = polynomial.split(" + ")

    x_coef = 0
    const = 0

    for term in terms:
        if "x" in term:
            coef = term.replace("x", "").strip()
            x_coef += 1 if coef == "" else int(coef)
        else:
            try:
                const += int(term)
            except ValueError:
                # 정수 변환 오류 처리 (예: 오류 메시지 출력 또는 기본값 사용)
                print(f"정수 변환 오류: {term}") # 디버깅용 print문 추가
                return "오류" # 또는 적절한 오류 처리
    result = ""

    if x_coef > 0:
        if x_coef == 1:
            result = "x"
        else:
            result = f"{x_coef}x"

    if const > 0:
        if result:
            result += " + "
        result += str(const)

    return result

# 제미나이가 푼 코드