# 클래스 변수
# 클래스 정의시 지정된 공용 변수
# 생성자 함수 위에 정의

class Test:
    # 공용변수, 클래스 변수
    msg = 'Test 클래스입니다.'

    # 생성자 메서드
    def __init__(self, name):
        self.name = name

    # 일반 메서드
    def print_info(self):
        print('name => ', self.name)

# 객체 인스턴스화
test1 = Test('test1')
# 객체 메서드 호출
test1.print_info()

# 인스턴스 생성후 접근
# - 인스턴스명.클래스변수명
# - 클래스명.클래스변수명
print('name 속성은?', test1.name)
print('test1.msg 속성은?', test1.msg)
print('Test.msg 속성은?', Test.msg)

# 동일한 주소값을 가지고 있다.
# id(객체이름) : 주소 표시
print(id(test1.msg), id(Test.msg))
print(id(test1.msg) == id(Test.msg))

# 상속(Inheritance)이란?
# 부모클래스의 속성이랑 메소드를 그대로 가진다.
# class 클래스이름(부모클래스1,부모클래스2...)
# 부모 클래스 = 조상 클래스 = 슈퍼 클래스
# 자식 클래스 = 파생 클래스

# 부모 클래스 => Country
# 자식 클래스 => Korea

class Country:
    # 클래스 변수 정의
    name_title = '국가명'
    population_title = '인구'
    capital_title = '수도'

    # 일반 메서드 정의
    def show(self):
        print('국가 클래스의 메서드 show 입니다.')

class Korea(Country):
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population

    def show_info(self):
        print('\n'*2+'$'*50)
        print(self.name, self.name_title)
        print(self.capital, self.capital_title)
        print(self.population, self.population_title)
        print()

# 인스턴스화
kor = Korea('대한민국', '서울', '5164만')
kor.show_info()
# 부모 클래스에서 상속받은 메서드 호출
kor.show()

# 다중 클래스 상속
# 부모클래스1 papa - 아파트, 차, 김철수
# 부모클래스2 mama - 오피스텔, 전동스쿠터, 이영희
# 자식클래스 - 아파트, 차 , 오피스텔, 전동스쿠터, 로봇청소기, 김은주

# 부모클래스를 상속해서 자식 클래스 만들기
# class 자식클래스명(부모클래스명1, 부모클래스명2....):
#   명령문

class Papa:
    family_name = '김'

    def __init__(self, name):
        self.name = name

    def asset_info1(self):
        print('아파트','차')

    def print_info(self):
        print(f'Papa 이름 => {self.family_name}{self.name}')

class Mama:
    family_name = '이'

    def __init__(self, name):
        self.name = name

    def asset_info2(self):
        print('오피스텔', '전동스쿠터')

    def print_info(self):
        print(f'Mama 이름 => {self.family_name}{self.name}')

class Child(Papa, Mama):

    def __init__(self, name):
        self.name = name

    def asset_info3(self):
        print('로봇 청소기')

    def print_info(self):
        print(f'Child 이름 => {self.family_name}{self.name}')

# 부모 클래스 인스턴스화
papa = Papa('철수')
papa.print_info()
papa.asset_info1()

print('-'*100)
mama = Mama('영희')
mama.print_info()
mama.asset_info2()

print('-'*100)
child = Child('은주')
child.asset_info1()
child.asset_info2()
child.asset_info3()
child.print_info()

# 부모 클래스와 자식 클래스의 관계 확인
# issubclass(자식클래스,부모클래스)
# : 자식클래스와 부모 클래스와의 관계 표시 (True / False)
# 부모 클래스 정보 표시
# 클래스명.__bases__ => 튜플 형태

print(issubclass(Child, Papa))
print(issubclass(Child, Mama))
print(issubclass(Papa, Mama))

# 부모 클래스 : Tiger, Lion
# 자식 클래스 : Liger

class Tiger:
    kind = '호랑이'

    def jump(self):
        print('호랑이처럼 멀리 점프하기')
    def cry(self):
        print('호랑이 : 어흥 ~ ')

class Lion:
    kind = '사자'

    def bite(self):
        print('사자처럼 한입에 꿀꺽하기')
    def cry(self):
        print('사자 : 으르렁 ~ ')

class Liger(Tiger,Lion):
    kind = '라이거'

    def play(self):
        print('라이거만의 사육사와 재미있게 놀기')

    def cry(self):
        print('라이거 : 어흥~ 으르렁~')

    def cry1(self):
        super().cry()


