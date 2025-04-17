# 用处：爬虫请求头…… （需要表单数据时）
from faker import Faker
fake = Faker('zh-CN') # 指定地区语言 组成：语言代码-国家（地区）代码

student = []


for i in range(5):
  student.append({"name":fake.name(),"address":fake.address(), "phone":fake.phone_number()})

# for i in range(len(student)):
#   print(student[i])
for i in student:
  print(i)