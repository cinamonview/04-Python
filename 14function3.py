




print(f"{'기본 내장 함수':-^50}")

data1 = list(range(1,11))
print(data1)
print('len=', len(data1))
print('sum=', sum(data1))
print('max=', max(data1))
print('min=', min(data1))



print(f"{'enumerate()':-^50}")
for i, v in enumerate(data1):
    print(i,v, end=', ')
print()



data2 = dict(birth = 1970, name = "홍길똥", size = "100cm")
for i, v in enumerate(data2):
    print(i,v, data2[v], end=', ')
print()


print(f"{'eval()':-^50}")
print(eval('1+2'))
print(eval("'hi'+'a'"))



print(f"{'sorted()':-^50}")
numbers = (8,7,6,8,4,9,7,5,3,2,7,4,9,8,2,6,5)
print(sorted(numbers))



print(f"{'이터레이터(iterator)':-^50}")
it = iter([1,2,3,4,5,99])
while it:
    row = next(it)
    if row ==99:
        break
    print(row, end=", ")
print()


import random
count = 0
for i in iter(lambda : random.randint(0,10),2):
    print(i, end=', ')
    count += 1
else:
    print('\n 난수 2가 생성되어 종료')
    
print(f'반복횟수:{count}')