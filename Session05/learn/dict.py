# n=int(input("nhập số số nguyên:"))
# list = []
# tong = 0
# for i in range(n):
#     m=int(input("mời nhập số:"))
#     list.append(m)
# for v in list:
#     tong += v 
# print("tổng của dãy là:", tong)


# Function ko tham số:
# def say_hi():
#     print('hi')
#     print("bye")
# say_hi()
# Function có tham số - không return
# def add_two_number(a, b):
#     print("tổng của 2 số là:", a+b)

# num1 = int(input('nhập số thứ nhất: '))
# num2 = int(input('nhập số thứ hai: '))

# add_two_number(500,1000*10)

# Function có tham số - có return
# def add_two_number(a, b):
#     return a + b
# num1 = int(input("nhập số thứ nhất: "))
# num2 = int(input("nhập số thứ hai: "))
# num3 = int(input("nhập số thứ ba: "))
# sum_1_2 = add_two_number(num1, num2)
# sum3 = add_two_number(sum_1_2, num3)
# print("tổng 3 số là: ", sum3)
# Lưu ý: 
# - Lệnh return phải nằm trong body của hàm
# - Lệnh return sẽ trả về kết quả cho lời gọi hàm: vd: tong=add_two_number(1,2)
# - Trong hàm có thể ko có, có 1 hoặc nhiều lệnh return
# - Khi gặp lệnh return thì các lênh sau đó ko thực hiện nữa.

# def abs_of_number(a):
#     if a > 0:
#         print("trị tuyệt đối là: ", a)
#         return a 
#     if a < 0:
#         print("trị tuyệt đối là: ", -a)
#         return -a
#     print('trị tuyệt đối là:', a)

# x = abs_of_number(-12)
# tong = 12 + abs_of_number(-12)
# print(x)
# print(tong)

# def evaluate(a, b, operator):
#     if operator == '*':
#         return a * b
#     elif operator == '/':
#         return a / b
#     elif operator == '+':
#         return a + b
#     elif operator == '-':
#         return a - b
#     else:
#         return 'không xử lí hàm đó'
# print(evaluate(2, 3, '/'))

def is_prime(n):
    if n < 2:
        return False
    for v in range(2,n):
        if n % v == 0:
            return False
    return True

so = int(input('nha so can kiem tra: '))
# if snt(so):
#     print('la so nguyen to')
# else:
#     print('khong la so nguyen to')
for v in range(2,so+1):
    if is_prime(v):
        print('số nguyên số là:', v)





