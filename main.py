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



# 파일이름 :60252667_김예성 4차과제
# 작 성 자 :김예성
import os
investments=[]
FILE_NAME = 'invest_data.csv'

def display_menu():
    print("\n" + "="*30)
    print("   투자관리 시스템 3.0     \n")
    print("="*30)
    print("1.신규 투자 정보 등록")
    print("2.전체 투자 현황 출력")
    print("3. 투자 정보 수정")
    print("4.투자 정보 삭제")
    print("5.파일로 저장 및 종료")
    print("="*30)

def load_data():
    global investments
    investments.clear()
    if not os.path.exists(FILE_NAME):
        return
    
    try:
        with open(FILE_NAME,"r",encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts=line.split(",")
                if len(parts) == 3:
                    name = parts[0]
                    amount = int(parts[1])
                    rate = float(parts[2])
                    investments.append([name,amount,rate])
        print(f"데이터 파일({FILE_NAME})을 성공적으로 불러왔습니다.")
    except FileNotFoundError:
        print("안내 불러올 기존 데이터 파일이 없습니다.새 파일을 생성합니다.")
    except Exception as e:
        print(f"데이터 로드 중 오류 발생:{e}")

def register_investment():
    print("\n[신규 투자 정보 등록]")
    name=input("-투자 종목명:").strip()
    if not name:
        print("종목명은 비워둘 수 없습니다.")
        return
    
    try:
        amount = int(input("-투자 금액:"))
        rate = float(input("-목표 수익률:"))
        investments.append([name,amount,rate])
        print(f"{name} 종목이 정상적으로 등록되었습니다")

    except ValueError:
        print("[오류] 금액은 정수,수익률은 숫자로 입력해주세요.")

def print_investments():
    print("\n[전체 투자 현황 조회]")
    if not investments:
        print("등록된 투자 정보가 없습니다.")
        return
    print("-"*50)
    print(f"{'번호':<4} | {'종목명':<12} | {'투자 금액(원)':<12} | {'목표 수익률(%)':<10}")
    print("-"*50)

    for i,item in enumerate(investments):
        print(f"{i+1:<4} | {item[0]:<12} | {item[1]:<12} | {item[2]:<10}%")
    print("-"*50)

def update_investment():
    print("\n[투자 정보 수정]")
    print_investments()
    if not investments:
        return
    
    try:
        idx=int(input("-수정할 항목의 번호를 입력하세요:"))-1
        if 0<= idx < len(investments):
            print(f"선택한 종목: {investments[idx][0]}")
            new_name = input(" * 새 종목명 (엔터 치면 기존 유지): ")
            new_amount_str = input("* 새 투자금액 (엔터 치면 기존 유지):")
            new_rate_str=input("새 목표 수익률 (엔터 치면 기존 유지):")

            if new_name:
                investments[idx][0] = new_name
            if new_amount_str:
                investments[idx][1] = int(new_amount_str)
            if new_rate_str:
                investments[idx][2] = float(new_rate_str)
            
            print("투자 정보가 성공적으로 수정되었습니다.")
        else:
            print("올바른 번호를 입력해주세요")
    except ValueError:
        print("[오류] 올바른 형식의 숫자를 입력해주세요")

def delete_investment():
    print("\n[투자 정보 삭제]")
    print_investments()
    if not investments:
        return
    
    try:
        idx = int(input("-삭제할 항목의 번호를 입력하세요:"))-1
        if 0<= idx < len(investments):
            deleted = investments.pop(idx)
            print(f"{deleted[0]} 종목 정보가 삭제되었습니다.")
        else:
            print("올바른 번호를 선택해주세요.")
    except ValueError:
        print("[오류] 숫자를 입력해주세요.")

def save_data():
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for item in investments:
                f.write(f"{item[0]},{item[1]},{item[2]}\n")
        print("모든 데이터가 안전하게 저장되었습니다.")
    except Exception as e:
        print(f"파일 저장 중 오류가 발생했습니다:{e}")

def main():
    load_data()

    while True:
        display_menu()
        choice = input("메뉴를 선택하세요: ").strip()

        if choice == "1":
            register_investment()
        elif choice =="2":
            print_investments()
        elif choice =="3":
            update_investment()
        elif choice =="4":
            delete_investment()
        elif choice =="5":
            save_data()
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()
        
        



    
        




    




