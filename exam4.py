
'''
print('\n=== 2단계: 클로저 ===')

def make_multiplier(x):
    #   x는 make_multiplier 함수의 지역 변수

    def multiplier(n):
        # 내부 함수 multilier는
        # 바깥 함수의 변수 x를 사용할 수 있다. 
'''
print('==== 1단계: 함수 안에 함수 만들기 ====')
def outer():
    print("outer 함수가 실행되었습니다.")

    def inner():
        print('inner 함수가 실행되었습니다.')

    return inner # 함수 자체를 반환
#   return inner() # 함수를 실행하고 그 결과를 반환
func = outer() 
func()

def make_multiplier(x):

    # x는 make_multiplier 함수의 지역 변수

    def multiplier(n):
        # 내부 함수 multiplier는
        # 바깥 함수의 변수 x를 사용할 수 있다.
        return x * n
    
    return multiplier

def decorator(func):
    # func는 꾸며줄 함수

    def wrapper():
        print('함수 실행 전')
        func()
        print('함수 실행 후')
    
    return wrapper

def say_hello():
    print('안녕하세요')

decorated = decorator(say_hello)
decorated()

print('\n=== 4단계: 매개변수가 있는 데코레이터 ===')

def decorator_width_args(func):
    def wrapper