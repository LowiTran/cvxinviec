import streamlit as st

# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="CV - Trần Văn Lợi",
    page_icon="👩‍💼",
    layout="wide"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

    /* Toàn bộ trang */
    .stApp {
        background-color: white;
    }

    .main {
        padding-top: 20px;
    }

    /* Font */
    html, body, [class*="css"] {
        font-family: Arial, sans-serif;
    }

    /* Tên */
    .name {
        font-size: 38px;
        font-weight: bold;
        color: #c6283d;
        margin-bottom: 5px;
    }

    /* Chức danh */
    .job {
        font-size: 22px;
        color: #222222;
        margin-bottom: 15px;
    }

    /* Giới thiệu */
    .intro {
        font-size: 16px;
        line-height: 1.6;
        text-align: justify;
        color: #222222;
    }

    /* Tiêu đề section */
    .section-title {
        font-size: 21px;
        font-weight: bold;
        color: #111111;
        border-top: 3px solid #c6283d;
        border-bottom: 3px solid #c6283d;
        padding: 7px 5px;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    /* Nội dung */
    .content {
        font-size: 16px;
        line-height: 1.55;
        color: #222222;
    }

    /* Tên trường / công ty */
    .bold {
        font-weight: bold;
    }

    /* Kinh nghiệm */
    .experience-date {
        font-size: 16px;
        font-weight: bold;
    }

    .company {
        font-size: 16px;
        font-weight: bold;
    }

    /* Bullet */
    .bullet {
        margin-left: 15px;
        line-height: 1.5;
        font-size: 15px;
    }

    /* Kỹ năng */
    .skill-title {
        font-size: 16px;
        font-weight: bold;
        margin-top: 12px;
    }

    .skill-content {
        font-size: 15px;
        line-height: 1.5;
    }

    /* Thông tin cá nhân */
    .info-row {
        font-size: 16px;
        margin-bottom: 10px;
    }

    .icon {
        color: #c6283d;
        font-weight: bold;
        margin-right: 10px;
    }

    /* Ảnh */
    .profile-img {
        width: 100%;
        max-width: 300px;
        border: 1px solid #dddddd;
    }

    /* Timeline */
    .timeline {
        border-left: 3px solid #777777;
        margin-left: 10px;
        padding-left: 25px;
    }

    .dot {
        width: 12px;
        height: 12px;
        background-color: #c6283d;
        border-radius: 50%;
        position: absolute;
        margin-left: -33px;
        margin-top: 5px;
    }

    /* Ẩn menu Streamlit */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# PHẦN 1: ẢNH + THÔNG TIN GIỚI THIỆU
# =========================================================

col1, col2 = st.columns([1, 2.2], gap="large")

with col1:

    st.image(
        "photo.jpg",
        width=300
    )

with col2:

    st.markdown(
        '<div class="name">TRẦN VĂN LỢI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="job">Nhân viên dịch vụ khách hàng</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<hr style="border: 1px solid #222222;">',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        '<div class="job">Mục Tiêu Nghề Nghiệp</div>
        Là sinh viên năm 3 chuyên ngành Tài Chính - Ngân hàng tại Trường
        Đại Học Nguyễn Tất Thành, đang tìm kiếm cơ hội được tại vị trí khởi
        đầu thực tập tại Ngân hàng Thương mại Cổ phần Ngoại thương Việt
        Nam (Vietcombank), để áp dụng những kiến thức và kỹ năng đã tích
        lũy, cùng với tinh thần ham học hỏi sẽ tiếp thu được nhiều kinh nghiệm
        hơn và phát bản thân trở thành một chuyên viên tài chính có năng lực,
        đóng góp và sự phát triển cho doanh nghiệp
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# PHẦN 2: THÔNG TIN CÁ NHÂN - HỌC VẤN - CHỨNG CHỈ
# =========================================================

col1, col2, col3 = st.columns([1, 1.15, 1.1], gap="large")


# ---------------------------------------------------------
# THÔNG TIN CÁ NHÂN
# ---------------------------------------------------------

with col1:

    st.markdown(
        '<div class="section-title">THÔNG TIN CÁ NHÂN</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-row">
            <span class="icon">●</span>
            26/05/2005
        </div>

        <div class="info-row">
            <span class="icon">✉</span>
            lowitran2005@gmail.com
        </div>

        <div class="info-row">
            <span class="icon">☎</span>
            0372763338
        </div>

        <div class="info-row">
            <span class="icon">📍</span>
            496/63/2D Dương Quảng Hàm
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# HỌC VẤN
# ---------------------------------------------------------

with col2:

    st.markdown(
        '<div class="section-title">HỌC VẤN</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="content">

        <div class="bold">
        Đại học Nguyễn Tất Thành
        </div>

        Tài chính - Ngân hàng

        <br>

        2023 - 2027

        <br>

        Chuyên ngành Tài chính ngân hàng

        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# CHỨNG CHỈ
# ---------------------------------------------------------

with col3:

    st.markdown(
        '<div class="section-title">CHỨNG CHỈ</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="content">

        Tin học:

        <br>

        Word, Excel, PDF

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# =========================================================
# KINH NGHIỆM LÀM VIỆC
# =========================================================

st.markdown("## KINH NGHIỆM LÀM VIỆC")
st.divider()

col_time, col_content = st.columns([1, 3])

with col_time:
    st.markdown("🔴 **06/2025 - 08/2026**")

with col_content:
    st.markdown("### Ngân Hàng Nhà Nước Việt Nam")
    
    st.markdown("**Nhân viên tư vấn và chăm sóc khách hàng**")
    
    st.markdown("""
    - Liên hệ tệp **+1000 khách hàng tiềm năng** và tư vấn khách hàng sử dụng các sản phẩm.
    
    - Tiếp nhận và xử lý các yêu cầu của khách hàng về sản phẩm.
    
    - Chăm sóc khách hàng cũ, hỗ trợ giải đáp mọi thắc mắc của khách hàng đối với sản phẩm đang sử dụng.
    """)
    
# =========================================================
# PHẦN 4: KỸ NĂNG + NGƯỜI THAM KHẢO
# =========================================================

col1, col2 = st.columns([1, 1], gap="large")


# ---------------------------------------------------------
# KỸ NĂNG
# ---------------------------------------------------------

with col1:

    st.markdown(
        '<div class="section-title">KỸ NĂNG</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="skill-title">
            Kỹ năng giao tiếp
        </div>

        <div class="skill-content">
            Giao tiếp và giải đáp thắc mắc của khách hàng
        </div>


        <div class="skill-title">
            Kỹ năng làm việc nhóm
        </div>

        <div class="skill-content">
            Control được công việc trong nhóm, phân chia cho các
            thành viên trong nhóm hoặc có trách nhiệm với nhiệm vụ
            được giao
        </div>


        <div class="skill-title">
            Kỹ năng quản lý thời gian
        </div>

        <div class="skill-content">
            Phân bổ thời gian hợp lý cho từng công việc
        </div>


        <div class="skill-title">
            Kỹ năng tin học
        </div>

        <div class="skill-content">
            Soạn thảo văn bảng, làm sile
        </div>
        """,
        unsafe_allow_html=True
    )
# Quá trình hoạt động
    st.markdown("""
    <div class="section-card">
        <div class="section-title">🚀 Quá trình hoạt động</div>
        <ul class="content-text" style="padding-left: 1.2rem;">
            <li style="margin-bottom: 0.9rem;">
                <strong>Workshop Đầu tư chứng khoán</strong> - "Bản tính đầu tư & tự tin chiến thắng"<br>
                <span style="color: #718096; font-size: 0.9rem;">Tháng 8/2024</span>
            </li>
            <li style="margin-bottom: 0.9rem;">
                <strong>Học phần “Phân tích đầu tư chứng khoán”</strong><br>
                Thực hành tại Công ty Chứng khoán Rồng Việt và Công ty Chứng khoán Phú Hưng<br>
                <span style="color: #718096; font-size: 0.9rem;">Tháng 4/2025</span>
            </li>
            <li>
                <strong>Học phần “Thẩm định tín dụng”</strong><br>
                Thực hành tại Ngân hàng Vietcombank - Thống Nhất<br>
                <span style="color: #718096; font-size: 0.9rem;">Tháng 11/2025</span>
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# NGƯỜI THAM KHẢO
# ---------------------------------------------------------

with col2:

    st.markdown(
        '<div class="section-title">NGƯỜI THAM KHẢO</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="content">

        <div class="bold">
            Trần Hoàng Tuấn Kiệt
        </div>

        Trưởng Phòng Hành Chính Nhân Sự (SM) - Ngân hàng TMCP
        Ngoại Thương Việt Nam (VCB)

        </div>
        """,
        unsafe_allow_html=True
    )
