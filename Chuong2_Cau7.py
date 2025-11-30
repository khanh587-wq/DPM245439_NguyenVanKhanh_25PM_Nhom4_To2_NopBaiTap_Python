# Nhập dữ liệu dạng chuỗi
name = input("Nhập tên của bạn: ")
print("Xin chào,", name)

# Nhập số nguyên và chuyển kiểu
age = int(input("Nhập tuổi của bạn: "))
print("Tuổi của bạn là:", age)

# Nhập nhiều số nguyên trên cùng một dòng
a, b = map(int, input("Nhập 2 số nguyên cách nhau dấu cách: ").split())
print("Hai số vừa nhập là:", a, b)

