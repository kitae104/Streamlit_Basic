import csv
from faker import Faker
import random

# Faker 객체 생성
faker = Faker()

# CSV 파일에 저장할 헤더 정의
fields = ['avataar', 'name', 'age', 'active', 'homepage', 'email', 'gender', 'birthdate', 'status']

# 생성할 레코드 수
num_records = 100

# CSV 파일 열기
with open('profile.csv', 'w', newline='') as csvfile:
    # CSV 작성기 생성
    csvwriter = csv.writer(csvfile)

    # 헤더 쓰기
    csvwriter.writerow(fields)

    # 레코드 생성 및 쓰기
    for _ in range(num_records):
        avataar = faker.image_url()
        name = faker.name()
        age = random.randint(18, 99)
        active = random.choice([True, False])
        homepage = faker.url()
        email = faker.email()
        gender = random.choice(['Male', 'Female'])
        birthdate = faker.date_of_birth().strftime('%Y-%m-%d')
        status = random.choice(['Active', 'Inactive'])

        # 레코드 쓰기
        csvwriter.writerow([avataar, name, age, active, homepage, email, gender, birthdate, status])

print("CSV 파일이 생성되었습니다.")