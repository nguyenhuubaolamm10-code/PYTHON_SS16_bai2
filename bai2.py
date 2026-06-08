# Danh sách thuốc ngày hôm qua (Lịch sử bệnh án cần giữ nguyên)
yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

# Hàm tạo và cập nhật đơn thuốc cho ngày mới
def update_prescription(old_prescription):
    # Lập trình viên cố gắng sao chép đơn thuốc sang ngày mới
    new_prescription = old_prescription.copy()
    # Cố gắng đổi tên thuốc ở vị trí đầu tiên (index 0) từ Panadol thành Paracetamol
    new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")
    # Thêm thuốc mới cho ngày hôm nay
    new_prescription.append("Oresol")
    return new_prescription
    
# Hệ thống chạy cấp thuốc cho ngày hôm nay
today_prescription = update_prescription(yesterday_prescription)
print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)

# Tại sao dòng lệnh new_prescription.append("Oresol") lại làm thay đổi cả biến yesterday_prescription nằm tít ở ngoài hàm? 
# Giải thích bản chất của phép gán new_prescription = old_prescription.
# vì chưa gán lại giá trị của biến 

# Để thực sự tạo ra một "bản sao" (copy) độc lập của List mà không ảnh hưởng đến List gốc, 
# ta có thể dùng những cách nào trong Python? (Kể tên ít nhất 2 cách).
# new_prescription = old_prescription[:]
# new_prescription = old_prescription.copy()

# Tại sao lệnh new_prescription[0].replace("Panadol", "Paracetamol") không có tác dụng?
# vì chưa gán lại giá trị của biến new_prescription[0]

# Cần sửa lại cú pháp ở câu 3 như thế nào để phần tử ở vị trí index 0 của danh sách thực sự được cập nhật thành tên thuốc mới?
# new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")