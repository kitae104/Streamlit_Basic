import csv

indata = open("transport.csv", encoding="utf-8") # UTF-8로 인코딩된 파일을 열어서 a에 저장
data = csv.reader(indata)    # csv.reader() 함수를 이용하여 파일을 읽어옴

next(indata)     # 첫 번째 줄은 제목이므로 건너뜀
next(indata)     # 두 번째 줄도 건너뜀

name_list = []  # 역 이름을 저장할 리스트 name_list를 생성
sum_list = []   # 합을 저장할 리스트 sum_list를 생성    

line = input("호선을 입력하세요 : ")  # 호선을 입력받음

for row in data:

    if line == row[1]:     # 입력받은 호선과 같은 호선이면  
        row[4:] = map(int,row[4:])  # 4번째 열부터 끝까지 정수로 변환
        sum = 0     # 합을 저장할 변수 sum을 0으로 초기화
        
        for i in range(7, 10):
            sum += row[(i-4) * 2 + 5]  # 7, 9, 11번째 열의 값을 더함
        
        name_list.append(row[3])    # 역 이름을 리스트 name_list에 추가
        sum_list.append(sum)        # 합을 리스트 sum_list에 추가

print("=" * 50)
print(name_list)
print(sum_list)
indata.close()

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.figure(figsize=(12, 6))
plt.bar(name_list, sum_list, color="blue")
plt.title(line + "의 하차 인원 ")
plt.xlabel("역 이름")
plt.ylabel("인원 수")
plt.xticks(rotation=90)
plt.show()