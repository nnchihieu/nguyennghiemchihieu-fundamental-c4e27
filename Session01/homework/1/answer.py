1. Kiểm tra biến:
- Một trong những tính năng mạnh mẽ nhất của ngôn ngữ lập trình là khả năng thao tác biến. Một biến là tên đề cập đến một giá trị.
- Giá trị có một số loại phổ biến như chuỗi, số nguyên hoặc số thực
Chuỗi có thể được xác định bởi vì chúng được đặt trong dấu ngoặc kép.
-Cách kiểm tra:
+type_x = type(x)
type(object_or_name, bases, dict)
param object_or_name

type(object) -> the object's type
type(name, bases, dict) -> a new type
2.  Nếu bạn đặt tên biến không hợp lệ, bạn sẽ gặp lỗi cú pháp.
Báo lỗi nếu nó có một trong ba điều dưới đây:
  + Bắt đầu bằng một chữ cái. Ex: 27code
  + Chứa một ký tự không hợp lệ, chẳng hạn như ký hiệu đô la hoặc ký hiệu pencentage (%), ... Ex: 50%
  + Đó là các từ khóa xác định cấu trúc và quy tắc của ngôn ngữ và chúng không thể được sử dụng làm tên biến. Ex: map



