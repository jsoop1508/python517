'''
#i = 1
   print(1)
   print(1)
   print(1)
  i += 1

j = 1
while j <= 3:
   print(j)
   j += 1



#for 변수 in 반복가능한객체:
   실행문
rangeop) 
# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담기

month = ["1월":31, "2월":28, ]

print('== 예제 1 ==')
s = '안녕하세요.'
# [0, 1, 2, 3, 4, 5]
print("길이 출력")
print(len(s))

# 문자열[시작:종료-1:간격] / s[start:end(-1):step]
print('s를 이루는 문장 중에서 앞에 거 2개 출력')
print(s[0:2])

print('s를 이루는 문장 중에서 문자 하나 건너 뛰고 1개 출력')
print(s[1:2])

print('s를 이루는 문장 중에서 문자 4개 출력')
print(s[4])

print('s를 이루는 문장 중에서 앞에 문자 3개 건너 뛰 , 나머지 전부 출력, len')
print(s[3:len(s)])

print('s를 이루는 문장 중에서 앞에 문자 3개 건너 뛰고 , 뒤 인덱스 생략')
print(s[3:])

print("=== 예제 2 ==")
s = '안녕하세요.'

print('s를 이루는 문자를 하나씩 출력, while')

print('s를 이루는 문자를 역순으로 하나씩 출력, while')

print('s를 이루는 문장중에서 한글만 출력, for, or, continue')
for c in s:
    if c == 'a' or c == 'b' or c == 'c' or c == 'd' or 

print('s를 이루는 문장중에서 한글만 출력, for, not, in')
for c in s: 
    if c not in ['a', 'b', 'c', 'd',] 
print('프로그램 시작')
try:
    num = int(abc)
    print(num)
except ValueError:
    print('숫자로 변경할 수 없습니다.')

print("프로그램 종료")


# 클래스 ->

class Person:
    def hello(self):
        print('hi')

jin = Person() # jin은 Person의 인스턴스 
jin.hello()         
    
a = int(10)
print(a)

b = list(range(10))
b.append(20)

print(type(b))


class person:
    pass

class person():
    def hello(self):
        print('helo')

    def hi(self):
        self.hello()

jin = Person()
jin.hi()


class person():
    def __init__(self, name, age, hobby):
        self.age = age
        self.hobby = hobby
        self.hello = '안녕하세요'
        self.name = name

    def introduce(self):
        print(f"{self.hello}, 저는 {self.age}살 {self.name}입니다")

jin = Person('진', 22, '운동') # 이 떄 __init__ 매서드가 실행됐다
jin.introduce()
print(f"이름 : {jin.name}") # 클래스 외부에서 접근
print(f"나이 : {jin.age}")
print(f"취미 : {jin.hobby}")

class Person: 
    pass 

jin = Person() # 인스턴스 생성
jin.name = '진' # 인스턴스를 생성한 뒤 속성 추가 

kim = Person() 

# 클래스 속성 
class Person:
    folder = [] # 클래스 속성

    def add_files(self, file):
        self.folder.append(file)

jin = Person()
jin.add_files('txt')

kim = Person()
jin.add_files('img')

print(jin.folder)
print(kim.folder)

print(ja)
'''
