# 과세 표준
def tax_layer(y_payment: int):
    if y_payment > 50000:
        return 7
    if 30000 < y_payment <= 50000:
        return 6
    if 15000 < y_payment <= 30000:
        return 5
    if 8800 < y_payment <= 15000:
        return 4
    if 4600 < y_payment <= 8800:
        return 3
    if 1200 < y_payment <= 4600:
        return 2
    if 0 < y_payment <= 1200:
        return 1


# 세율
tax_rate = [6, 15, 24, 35, 38, 40, 42]

# 누진공제
tax_discount = [0, 108, 522, 1490, 1940, 2540, 3540]


# 산출세액
def salary_to_tax(tax_layer: int, y_payment: int):
    return y_payment * tax_rate[tax_layer - 1] / 100 - tax_discount[tax_layer - 1]


while True:
    try:
        i = int(input("세전연봉을 입력해 주세요 : "))
    except ValueError:
        print("숫자만 입력해주세요.")
        continue
    print(f"세전연봉 {i} / 세후연봉 {i - int(salary_to_tax(tax_layer(i), i))} (소득세: {int(salary_to_tax(tax_layer(i), i))}만원)")
