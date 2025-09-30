from instruction import INSTRUCTION
from chat import get_info

if __name__ == "__main__":
    noi_dung="""
Nguyen Van A (+84)91*****23
123 Đường ABC, Phường XYZ, Quận 1, Hồ Chí Minh, Việt Nam

Thay đổi địa chỉ

(PT Cửa hàng Chính hãng

—= [LS1] Combo 2 chai Dầu gội XyzCare
2 sản phẩm
Chính hãng 100% Trả hàng miễn phí
: _ Freeship
x1 450.000đ

——&. Quà miễn phí [GIFT] Sữa tắm XyzCare
Mặc định

Chính hãng 100%
Freeship

Trả hàng miễn phí

x1

í\ Trả hàng miễn phí thuận tiện

© Liên hệ với người bán 9›

Vấn đề về sản phẩm, trước khi vận chuyển và các câu hỏi khác

Thay đổi địa chỉ Hủy đơn hàng

‹ Đã đặt hàng
G) Liên hệ với người bán L2

Vấn đề về sản phẩm, trước khi vận chuyển và các câu hỏi khác

(2) Liên hệ với TikTok ›
Vấn đề về tài khoản, thanh toán, khiếu nại và sau vận chuyển

Tổng quan đơn hàng

Tổng phụ 450.000đ
Vận chuyển 45.000đ
Phiếu giảm giá -30.000đ
Phiếu giảm giá của người bán -20.000đ
Phiếu giảm giá vận chuyển của TikTok -45.000đ

Tổng 400.000đ

Chi tiết đơn hàng

Số đơn hàng 5900123456789 (©
Ngày đặt hàng 30 tháng 9 2025, 09:45 SA
Phương thức thanh toán Cash on Delivery

Thay đổi địa chỉ Hủy đơn hàng"""
    key = ""
    print(get_info(noi_dung, INSTRUCTION, key))