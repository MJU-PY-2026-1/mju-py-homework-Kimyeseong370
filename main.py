# 파일이름 :60252667_김예성 3차과제
# 작 성 자 :김예성
names = []
moneys = []
rates = []
profits = []

total_profit = 0

def calc_profit(money,rate):
    profit= money * rate /100
    return profit

def add_invest():
    global total_profit

    print("\n[투자 추가]")
    name=input("투자 이름 입력: ")
    money=int(input("투자 금액 입력: "))
    rate=float(input("수익률 입력: "))

    profit = calc_profit(money,rate)

    names.append(name)
    moneys.append(money)
    rates.append(rate)
    profits.append(profit)

    total_profit +=profit

    print("\n투자 정보가 저장되었습니다!")
    print(f"예상 수익 : {profit:.1f}원")

def show_invest():
    print("\n[투자 조회]")

    if len(names) == 0:
        print("저장된 투자 정보가 없습니다")
        return
    
    for i in range(len(names)):
        print(f"\n[{i+1}번째 투자]")
        
        print(f"투자 이름 : {names[i]}")
        print(f"투자 금액 : {moneys[i]}원")
        print(f"수익률 : {rates[i]}%")
        print(f"예상 수익 : {profits[i]}원")

def analyze_invest():
     print("\n[투자 분석]")

     if len(profits) == 0:
        print("분석할 투자 정보가 없습니다.")
        return

     max_profit = max(profits)
     index = profits.index(max_profit)

     print(f"총 예상 수익 : {total_profit:.1f}원")
     print(f"최고 수익 투자 : {names[index]}")
     print(f"최고 수익 금액 : {max_profit:.1f}원")

while True:

    print("\n=======================")
    print("대학생투자관리 프로그램")
    print("=======================")
    print("1.투자 추가")
    print("2.투자 조회")
    print("3.투자 분석")
    print("4.종료")

    menu = input("메뉴 선택 : ")

    if menu == "1":
        add_invest()

    elif menu == "2":
        show_invest()
    elif menu == "3":
        analyze_invest()
    elif menu == "4":
        print("프로그램을 종료합니다")
        break
    else:
        print("\n잘못된 입력입니다.")



