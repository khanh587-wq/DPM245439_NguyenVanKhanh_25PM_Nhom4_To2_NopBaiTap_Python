def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    
    if n < 0 or n > 99:
        return "Chỉ nhập số từ 0 đến 99"
    
    if n == 0:
        return "Không"

    if n < 10:
        return don_vi[n].capitalize()

    chuc = n // 10
    dv = n % 10

    if chuc == 1:
        doc = "Mười"
    else:
        doc = don_vi[chuc].capitalize() + " mươi"

    if dv == 1:
        doc += " mốt" if chuc != 1 else " một"
    elif dv == 5:
        doc += " lăm" if chuc != 0 else " năm"
    elif dv != 0:
        doc += " " + don_vi[dv]

    return doc

n = int(input("Nhập số nguyên n (0-99): "))
print("Cách đọc:", doc_so(n))

