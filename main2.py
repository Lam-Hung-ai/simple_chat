from schema import DonHang
from chat import get_info_with_structure, get_text_from_images
from instruction import INSTRUCTION_2

if __name__ == "__main__":
    key = ""
    # Nên dùng đường dẫn tuyệt đối để tránh lỗi
    text_images = get_text_from_images(["/home/lamhung/code/simple_chat/images/3.jpeg", "/home/lamhung/code/simple_chat/images/4.jpeg"])
    noi_dung = "\n".join(text_images)
    print("Nội dung trong các ảnh:", noi_dung)
    don_hang_dict = get_info_with_structure(
        thong_tin_buu_kien=noi_dung, 
        schema=DonHang, 
        instruction=INSTRUCTION_2,
        api_key=key)
    if isinstance(don_hang_dict, DonHang):
        print("Kết quả trích xuất được:")
        print("Thông tin người nhận:", don_hang_dict.nguoi_nhan)
        print("Thông tin sản phẩm:", don_hang_dict.san_pham)
        print("Thông tin tổng tiền:", don_hang_dict.tong_tien)
        print("Chi tiết đơn hàng:", don_hang_dict.chi_tiet_don_hang)
