#Ghi đè những vẫn chạy nội dung của class cha
class QuaiVat:
    def tan_cong(self):
        print("- Trừ 10 HP người chơi") # Logic chung phức tạp

class RongLua(QuaiVat):
    def tan_cong(self):
        # 1. Gọi logic chung (đỡ phải viết lại code trừ máu)
        super().tan_cong()
        
        # 2. Thêm logic riêng
        print("- Người chơi bị BỎNG (mất thêm 5 HP mỗi giây)")

rong = RongLua()
rong.tan_cong()