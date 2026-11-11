# 클로저(closure) 데코레이터(Decorator)

# 

print('====1단계: 함수 안에 함수 만들기 ===')
def outer():
    print("outer 함수가 실행되었습니다.")

    def inner():
        print('inner 함수가 실행되었습니다.')

    return inner # 함수 자체를 반환
#    return inner() # 함수를 실행하고 그 결과를 반환

func = outer() 
func()