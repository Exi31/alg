
from collections import namedtuple

thi_sinh = namedtuple("ThiSinh", "Ten Diem Khoa")
khoa_DDT = []
khoa_khac = []

print("Hãy paste (Ctrl+V) toàn bộ dữ liệu vào bên dưới.")
print("Sau khi paste xong, nhấn Enter rồi nhấn Ctrl + D để chạy:")
print("--------------------------------------------------")

# Vòng lặp vô hạn đọc dữ liệu cho đến khi hết file (EOF)
while True:
    try:
        line = input()
        if not line.strip():  # Bỏ qua dòng trống nếu có
            continue
            
        # Unpacking thông minh của bạn
        *ten, diem, khoa = line.split()
        
        ten = " ".join(ten)
        diem = int(diem)

        if khoa == "DDT": 
            khoa_DDT.append(thi_sinh(ten, diem, khoa))
        else: 
            khoa_khac.append(thi_sinh(ten, diem, khoa))
            
    except EOFError:
        # Khi bạn nhấn Ctrl+D, Python sẽ nhảy vào đây và dừng vòng lặp
        break

# Sắp xếp và tìm giải
khoa_DDT.sort(key=lambda x: x.Diem, reverse=True)
sv_giao_luu = max(khoa_khac, key=lambda x: x.Diem)

print("\n--- KẾT QUẢ TRAO GIẢI ---")
print("Giai nhat:", khoa_DDT[0].Ten)
print("Giai nhi:", khoa_DDT[1].Ten)
print("Giai ba:", khoa_DDT[2].Ten)
print("Giai giao luu:", sv_giao_luu.Ten)
