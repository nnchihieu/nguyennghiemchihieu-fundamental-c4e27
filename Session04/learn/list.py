# Cấu trúc dữ liệu + thuật toán = chương trình
# Chuỗi là 1 danh sách các kí tự
# List gần giống chuỗi(strings): độ dài (len), lấy chỉ số(indexer)
# VD: string = "hello"=> string[4] lấy ra o

# colors=['red', 'green', 'blue']
# b = colors
# colors[0] = 'yellow'
# print(colors[0])

# CRUD:
# C: create
# R: read
# U: update
# D: delete

# 3 cách khởi tạo list:
# -Empty list: a=[]
# -a=[1,2,3]
# -a=list(range(3))

# CRUD-Create:
# -Append: list.append(elem)=> thêm phần tử vào cuối dãy
# -Insert(chèn):list.insert()
# VD: list[1,2,3]
# list.insert(0,8)
# =>list=[8,1,2,3]
# -Extend
# CRUD-Update:
# <list variable>[index]

# CRUD-Delete:
# delete by index: del list[index]=>xóa và ko trả về giá trị đã xóa
# delete by index: list.pop(index)=>xóa và trả về giá trị đã xóa
# -Delete first item: list.remove("red")

# CRUD-Slices
# list=['a', 'b', 'c', 'd']
# list[1,-1]=>['b', 'c']

# In ra các cặp:
# ls=[1,3,7,4,6]
# for i in range(5):
#     for j in range(i+1,5):
#         print('i=', i, 'j=', j, 'cặp là:', ls[i], '-', ls[j])
#         if(ls[i]+ls[j])%2 == 0:
#             print('cặp số cần tìm là:', ls[i], ' ', ls[j])
#in ra n số và in ra các cặp có tổng chẵn:
# a=[]
# n=int(input("nhập n:"))
# for i in range(n):
#     m=int(input("nhập giá trị"))
#     a.append(m)
# Tìm bộ 3 số x, y, z như sau:
# 0<=x, y, z<=100
# x^2+y^2+z^2=x*y*z

# DICTIONARY:
# Khởi tạo:
# -dic={}
# -dic=dict{}
# dic={'name':'Hiếu','age':'19'}

# dict-create:
# person={"name":"Hiếu"}
# person['age']=19
# dict-read:
# person={'name':'Hiếu', 'age':19}
# addr=person.get('address','')
# if 'address' in person:
# addr=person['address']
# print(addr)
# =>ko ra vì key ko tồn tại
# Các phần tử ko liên tiếp nhau, nên chỉ số ko có ý nghĩa, cần dùng key

# dict-update:

# dict-delete:

# dict-functions:
# -len(dict)
# -str(dict)

# dic={'computer':"máy tính", 'mouse':"chuột", 'keyboard':"bàn phím"}

# while True:
#     i=input("mời nhập từ:")
#     if i in dic:
#         print('nghĩa là:',dic[i])
#     elif(i=='exit'or'quit'):
#         break
#     else:
#         print("không có trong từ điển")

# Loop in dict:
# -Duyệt theo key:
# for v in dic:
#     print(v)
# -Duyệt theo value:
# for v in dic.values()
#     print(v)
# -Duyệt theo từng cặp:
# for k,v in dic.items()
#     print(k,':',v)


tap_nguoi=[]
nguoi_1={
    'name':'hieu'
    'age':'19'
    'sdt':
}