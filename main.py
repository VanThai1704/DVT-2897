def tinh_tong():
    try:
        # Bước 1: Nhập dữ liệu từ bàn phím
        num1 = input("Nhập số thứ nhất: ")
        num2 = input("Nhập số thứ hai: ")

        # Bước 2: Chuyển đổi từ chuỗi sang số thực (float)
        # Sử dụng float để có thể cộng được cả số nguyên và số thập phân
        tong = float(num1) + float(num2)

        # Bước 3: In kết quả ra màn hình
        # Dùng f-string để định dạng chuỗi cho đẹp
        print(f"--- Kết quả ---")
        print(f"Tổng của {num1} và {num2} là: {tong}")

    except ValueError:
        # Xử lý lỗi nếu người dùng nhập chữ thay vì nhập số
        print("Lỗi: Vui lòng chỉ nhập các con số!")

if __name__ == "__main__":
    tinh_tong()