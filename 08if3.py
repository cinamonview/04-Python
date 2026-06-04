kor = int(input("국어점수를 입력하세요 : "))
eng = int(input("영어점수를 입력하세요 : "))
math = int(input("수학점수를 입력하세요 : "))
avg = (kor + eng + math) / 3

print(kor," ", eng ," ", math, " ", avg)

if avg>=90:
  print("A학점입니다.")
elif 90>avg>=80:
  print("B학점입니다.")
elif 80>avg>=70:
  print("C학점입니다.")
elif 70>avg>=60:
  print("D학점입니다.")
else:
  print("F학점입니다.")
  
  
  