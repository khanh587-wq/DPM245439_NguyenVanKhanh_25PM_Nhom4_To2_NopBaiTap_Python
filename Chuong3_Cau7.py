import datetime

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

try:
    current_date = datetime.date(nam, thang, ngay)
    next_date = current_date + datetime.timedelta(days=1)
    print("Ngày kế tiếp là:", next_date.strftime("%d/%m/%Y"))
except ValueError:
    print("Ngày không hợp lệ! Vui lòng kiểm tra lại.")
