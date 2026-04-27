# 파일이름 :60252667_김예성 2차과제
# 작 성 자 :김예성
names = []
moneys = []
rates = []
profits = []

total_money = 0
total_profit = 0

count = int(input("몇 개의 투자를 입력하시겠습니까? "))

for i in range(count) :
    print(f"\n[{i+1}번째 투자 입력]")

    name = input("이름: ")
    money = int(input("투자금: "))
    rate = float(input("수익률(%): "))

    profit = money * (rate/100)
    
    names.append(name)
    moneys.append(money)
    rates.append(rate)
    profits.append(profit)

    total_money+= money
    total_profit += profit

print("\n=====투자결과=====")

for i in range(len(names)) :
    if profits[i] >0 :
        status ="수익"
    elif profits[i] < 0:
        status = "손실"
    else:
        status = "유지"

    print(f"{names[i]} -> 수익:{int(profits[i])}원 ({status})")

if len(profits) > 0 and total_profit !=0:
    avg_profit = total_profit / len(profits)
else:
    avg_profit = 0

print("\n====전체 요약====")
print(f"총 투자금:{total_money}원")
print(f"총 수익:{int(total_profit)}원")
print(f"평균 수익:{int(avg_profit)}원")   



