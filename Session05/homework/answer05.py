# 1) Lý do chúng ta nên dùng hàm:
# - Khi dùng hàm, mỗi hàm có thể dùng đi dùng lại nhiều lần mà không cần viết lại đoạn code khi sử dụng các lệnh khác -> đoạn code ngắn gọn,
# dễ hiểu,tiết kiệm thời gian.
# Khi dùng hàm, mỗi khi cần chỉ cần đưa ra tên hàm và tùy mục đích sử dụng mà định nghĩa tên hàm.

# 2) Cú pháp hàm:
# def <tên hàm> ([tham số]):
#     câu lệnh

# 3) Cú pháp gọi tên hàm:
# <tên hàm>(tham số)

# 4) Return:
# - Dùng để trả lại 1 hay nhiều giá trị của hàm.
# - Khi kết thúc hàm, nếu không dùng return thì giá trị của nó sẽ mất luôn và không thể sử dụng lại.
# - Cú pháp: 
# def <tên hàm>([tham số]):
#     câu lệnh
#     return <biến để trả lại giá trị>

# 5) Không nhất thiết phải sử dụng return trong mọi hàm mà chỉ dùng khi cần trả lại giá trị của hàm.

# 6) Tham số của hàm là các giá trị mà hàm dùng để xử lí các câu lệnh, tác vụ trong hàm (có thể là lệnh print hoặc return).
# def <tên hàm>(a,b,c):
#     câu lệnh

# 7) Để dùng các hàm ở tệp khác, ta cần truy xuất tên tệp chứa 1 hay nhiều hàm cần dùng.
# - Cú pháp:
#     import <tên tệp chứa hàm>
#     <tên tệp chứa hàm>.func()
# hoặc
#     from <tên tệp chứa hàm> import <hàm>
#     <hàm> 

