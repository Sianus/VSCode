# 리스트에서 임의의 원솟값을 업데이트하기 

def change(lst, idx, val):
    """lst[idx]의 값을 val로 업데이트"""
    lst[idx] = val

x = [11, 22, 33 ,44 ,55]
print('x =', x)

index = int(input('업데이트할 인덱스 선택 : '))
value = int(input('새로운 값 입력 : '))

change(x, index, value)
print(f'x = {x}')