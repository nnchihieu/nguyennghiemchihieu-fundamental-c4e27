# Số tiền trong tài khoản sau 9 năm:
money = int(input("số tiền đang có: "))
years = int(input("số năm gửi tiền: " ))
for i in range(1,years+1):
    money = money + (6.5/100)*money
print("số tiền qua",i,"năm: ",money) 
# Số năm cần ít nhất để mua được căn nhà 1,2 tỷ:
n = 0 
money = int(input("số tiền đang có: "))
while not money >= 1200000000 :
    money = money + (6.5/100)*money
    n = n +1
print("số năm để có 1,2 tỉ là: ",n)