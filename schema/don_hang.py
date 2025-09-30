from pydantic import BaseModel, Field
from typing import List

class NguoiNhan(BaseModel):
    ho_ten: str = Field(description="Họ tên người nhận")
    so_dien_thoai: str = Field(description="Số điện thoại người nhận")
    dia_chi: str = Field(description="Địa chỉ người nhận")

class SanPham(BaseModel):
    ten_san_pham: str = Field(description="Tên sản phẩm")
    so_luong: int = Field(description="Số lượng sản phẩm")
    gia_tien: str = Field(description="Giá tiền của sản phẩm (theo 1 đơn vị hoặc combo)")

class ChiTietDonHang(BaseModel):
    so_don_hang: str = Field(description="Số đơn hàng")
    ngay_dat_hang: str = Field(description="Ngày đặt hàng")
    phuong_thuc_thanh_toan: str = Field(description="Phương thức thanh toán")

class DonHang(BaseModel):
    nguoi_nhan: NguoiNhan = Field(description="Thông tin người nhận")
    san_pham: List[SanPham] = Field(description="Danh sách sản phẩm trong đơn hàng")
    tong_tien: str = Field(description="Tổng tiền sau khuyến mãi và phí vận chuyển")
    chi_tiet_don_hang: ChiTietDonHang = Field(description="Chi tiết đơn hàng")

