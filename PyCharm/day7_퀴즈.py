# 클래스 퀴즈

# 퀴즈 1
# 삼각형 클래스를 다음과 같은 속성과 메서드로 정의하여라
# 속성(이름, 밑변, 높이)
# 메서드1 - 속성 출력
# 메서드2 - 삼각형의 넓이 출력
# 삼각형의 면적 구하는 공식 = (밑변의길이 * 높이)/2




# 퀴즈 2
# 퀴즈1의 삼각형 클래스를 이용하여 인스턴스 객체를 생성하고 메서드를 호출하여라


'''
이름 = triangle1
밑변 = 10
높이 = 5
====================
삼각형 넓이 = 25.00
====================


이름 = triangle2
밑변 = 35
높이 = 27
====================
삼각형 넓이 = 472.50
====================


'''






# 퀴즈 3
# 클래스 Animal과  Animal 클래스를 상속받는 Dog 클래스를
# 정의하여라. 아래는 참고 코딩이다.


# class Animal:
#     def __init__(self...):
#         명령 입력
#
#     def info(self...):
#         명령 입력
#
#     def run(self):
#         명령 입력
#
#     def (self, food):
#         명령 입력


#
# class Dog(?):
#
#    def printName(self):
#         명령 입력
#     def shout(self):
#         명령 입력
#


# print('퀴즈 3')

class Animal:
    kind = '동물'

    def __init__(self, legs):
        self.legs = legs
    def info(self):
        print('종류 :', self.kind)
        print('다리 수 :', self.legs)
    def run(self):
        print(self.kind, '이(가) 달린다.')
    def eat(self, food):
        print(self.kind, '이(가)', food, '을(를) 먹는다.')

class Dog(Animal):
    kind = '강아지'
    legs = 4

    def __init__(self, name):
        self.name = name
    def printName(self):
        print('강아지 이름은', self.name, '이다.')
    def shout(self):
        print(self.kind, '이(가) 멍멍 짖는다.(소리를 낸다)')


# 퀴즈 4
# 퀴즈 3에서 정의한 클래스를 이용하여 다음과 같이 출력되도록
# 객체 인스턴스화하고 메서드를 호출하여라.
'''
종류 : 동물
다리수 : 4
동물 이(가) 달린다. 
동물 이(가) 물을(를) 먹는다.
==============================
종류 : 강아지
다리수 : 4
강아지 이(가) 달린다. 
강아지 이(가) 뼈다귀을(를) 먹는다.
강아지의 이름은 행운이이다.
강아지 이(가) 멍멍 짖는다.(소리를 낸다) 
'''

animal = Animal(4)
animal.info()
animal.run()
animal.eat('물')

print('-'*100)
dog = Dog('행운이')
dog.info()
dog.run()
dog.eat('뼈다귀')
dog.printName()
dog.shout()

# 퀴즈 5
# 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정된다.
# Account 클래스를 생성한 후 객체 인스턴스를 구현하도록 프로그래밍하여라.
# 객체 인스턴스는 예금주와 초기 잔액만 입력 받으며
# 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성한다.
# random 모듈 이용
'''
고객명 김민수
잔액 100
은행 SC은행
계좌 375-85-239565
'''
import random

class Account:
    bank_name = 'SC은행'
    number = '빈계좌'
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.number = str(random.randint(100,999)) + '-' \
                      + str(random.randint(10,99)) + '-' \
                      + str(random.randint(100000,999999))
        Account.account_count += 1

    def get_account_num():
        print('결과 >> ')
        print(f'총 계좌수 : {Account.account_count}')

    def deposit(self, money):
        if money >= 1:
            self.balance += money
        else:
            print('입금 불가')

    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
        else:
            print('출금 불가')

    def display_info(self):
        print('은행이름 :', self.bank_name)
        print('예금주 :', self.name)
        print('계좌번호 :', self.number)
        print('잔고 :', self.balance)

account = Account('김민수', 100)

print('고객명 ', account.name)
print('잔액 ', account.balance)
print('은행 ', account.bank_name)
print('계좌 ', account.number)

# 퀴즈 6
print('-'*100)
# 퀴즈 5의 클래스에 클래스 변수를 사용해서
# Account 클래스로부터 생성된 계좌 객체와 관련된 변수를 정의하고
# 출력하도록 get_account_num() 메서드를 추가하여라.
'''
# 계좌를 3개 인스턴스화 한 경우 
chio = Account("최진수", 100)
kim = Account("김민수", 100)
lee = Account("이민수", 100)
Account.get_account_num()

결과>>
총 계좌수 :  3

'''

chio = Account("최진수", 100)
kim = Account("김민수", 100)
lee = Account("이민수", 100)
Account.get_account_num()

# 퀴즈 7
print('-'*100)
# 위에서 정의한 Account 클래스에
# 입금을 위한 deposit 메서드와
# 출금을 위한 withdraw 메서드를 하여라.
# 출금은 계좌의 잔고 이상으로 출금할 수는 없으며
# 입금은 최소 1원 이상만 가능하다.
'''
# 객체 인스턴스 참고코드. 
k = Account("kim", 100)
k.deposit(100)
k.withdraw(90)
print('잔액 => ',k.balance)

# 잔액 =>  110
'''

k = Account("kim", 100)
k.deposit(100)
k.withdraw(90)
print('잔액 => ',k.balance)


# 퀴즈 8
print('-'*100)
# 위에서 정의한 Account 클래스에
# Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를
# 추가하여라.
'''
# 객체 인스턴스 참고 소스 
print('$'*70)
p = Account("홍길동", 10000)
p.display_info()

#  >> 결과 
은행이름:  SC은행
예금주:  홍길동
계좌번호:  098-29-285603
잔고:  10000
'''

p = Account("홍길동", 10000)
p.display_info()


# 퀴즈 9
print('-'*100)
# 클래스를 이용한 자판기 메뉴를 표시하는 프로그램을 프로그래밍 하려고 한다.
# 다음과 같이 속성과 메서드를 정의하여라.
# 속성
# :  지역, 메뉴(튜플형태), 가격(튜플형태)
# 메소드
# : 메뉴 표시
# : 머신 실행


'''
# vm1 = Vending_machine('강남점',('아메리카노', '라떼'), (1200, 2000))
# vm1.start()

		 강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
'''


'''
# vm2 = Vending_machine('분당점',('아메리카노', '핫초코', '버블티'), (800, 1000, 2500))
# vm2.start()
		 분당점 
메뉴1 : 아메리카노 /  가격 800 원
메뉴2 : 핫초코 /  가격 1000 원
메뉴3 : 버블티 /  가격 2500 원

'''


'''
# vm3 = Vending_machine('부산역점',('수박쥬스','아이스아메리카노', '카푸치노', '탄산수'), (2000, 700, 1500, 1300))
# vm3.start()


부산역점 

메뉴1 : 수박쥬스 /  가격 2000 원
메뉴2 : 아이스아메리카노 /  가격 700 원
메뉴3 : 카푸치노 /  가격 1500 원
메뉴4 : 탄산수 /  가격 1300 원

'''

class Vending_machine:
    location = '지역'
    menu = ()
    price = ()
    money = 0

    def __init__(self, location, menu, price):
        self.location = location
        self.menu = menu
        self.price = price

    def start(self):
        print('\t\t', self.location)
        for i in range(len(self.menu)):
            print(f'메뉴{i+1} : {self.menu[i]} / 가격 {self.price[i]}원')

    def buying(self):
        self.start()

        while True:
            print('주문하실 메뉴의 금액을 삽입구에 넣어주세요')
            self.money = input('투입 =>').strip()
            if self.money.isdigit() == False:
                print('금액만 입력해 주세요.')
                continue
            else:
                self.money = int(self.money)
                break

        buy = False
        cnt = 0
        while(cnt < len(self.price)):
            if self.money >= self.price[cnt]:
                buy = True
            cnt += 1

        if buy:
            print('주문이 가능합니다.')
            self.menu_select()
        else:
            print('투입 금액이 부족하여 주문이 불가능합니다.')
            print('투입구를 확인하여 주세요(환불) =>', self.money)
            self.money = 0

    def menu_select(self):

        while True:
            print('\n')
            print('='*10, '메뉴를 선택하세요', '='*10)

            for i in range(len(self.menu)):
                print(f'{i+1}. {self.menu[i]}', end='\t')
            print('(활불 및 다시 시작 q)')
            print('='*30)

            select_num = input('선택 => ').strip()
            if select_num == 'q':
                print(f'투입구를 확인하여 주세요(금액 활불) => {self.money}원')
                break
            if select_num.isdigit() == False:
                print('잘못된 입력입니다.')
                continue
            select_num = int(select_num)
            if select_num > len(self.menu) or select_num < 1:
                print('선택 번호의 메뉴가 없습니다.')
                continue
            if self.money >= self.price[select_num-1]:
                print('='*30)
                print(f'주문하신 {self.menu[i-1]}가 나왔습니다.')
                self.money -= self.price[select_num-1]
                print(f'잔돈은 {self.money}원 입니다.')
                self.money = 0
                break
            else:
                print('투입 금액이 부족하여 주문이 불가능합니다.')




vm1 = Vending_machine('강남점',('아메리카노', '라떼'), (1200, 2000))
vm1.start()

vm2 = Vending_machine('분당점',('아메리카노', '핫초코', '버블티'), (800, 1000, 2500))
vm2.start()

vm3 = Vending_machine('부산역점',('수박쥬스','아이스아메리카노', '카푸치노', '탄산수'), (2000, 700, 1500, 1300))
vm3.start()

# 퀴즈 10 :
# 퀴즈 9의 자판기 머신 클래스에 금액을 투입하여
# 투입한 금액에 따라 메세지를 출력하는
# 메서드를 추가하고 실행되도록 프로그램하여라.

'''
		 강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원

주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => Yes
투입한 금액이 올바르지 않습니다. 주문이 불가능합니다.
투입 => 

'''

'''
# 예시 

		 강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원

주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => 2000
주문이 가능합니다.

'''

'''
		 강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원

주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => 500
투입 금액이 부족하여 주문이 불가능합니다.
투입구를 확인하여 주세요(환불) => 500원

'''



# 퀴즈 11 :
print('-'*100)
# 퀴즈 10의 자판기 머신 클래스에서 아래 출력 화면을
# 참조하여 메서드를 추가하고 실행되도록 하여라.
# - 투입금액에 따른 메뉴 선택
# - 메뉴 선택에 따른 메시지 출력
# - 잔돈 메시지

'''


		 강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => 1500
주문이 가능합니다.

========== 메뉴를 선택하세요 ==========
1.아메리카노   2.라떼    (환불 및 다시 시작 q)
======================================
선택 => 2
투입 금액이 부족하여 주문이 불가능합니다.


========== 메뉴를 선택하세요 ==========
1.아메리카노   2.라떼    (환불 및 다시 시작 q)
======================================
선택 => 567
선택 번호의 메뉴가 없습니다.

========== 메뉴를 선택하세요 ==========
1.아메리카노   2.라떼    (환불 및 다시 시작 q)
======================================
선택 => hhh
잘못된 입력입니다.

========== 메뉴를 선택하세요 ==========
1.아메리카노   2.라떼    (환불 및 다시 시작 q)
======================================
선택 => q
투입구를 확인하여 주세요(금액 환불) => 1500원


		 강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => 900
투입 금액이 부족하여 주문이 불가능합니다.
투입구를 확인하여 주세요(환불) => 900원


		 강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => 2000
주문이 가능합니다.

========== 메뉴를 선택하세요 ==========
1.아메리카노   2.라떼    (환불 및 다시 시작 q)
======================================
선택 => 1

=====================================
주문하신 아메리카노가 나왔습니다.
잔돈은 800원 입니다.


'''

vm1.buying()
