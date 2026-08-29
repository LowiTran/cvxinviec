import base64
from pathlib import Path

import streamlit as st


# =========================================================
# CẤU HÌNH STREAMLIT
# =========================================================
st.set_page_config(
    page_title="CV Trần Văn Lợi",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# ĐƯỜNG DẪN FILE ẢNH
# =========================================================
BASE_DIR = Path(__file__).resolve().parent
PHOTO_PATH = BASE_DIR / "profile.jpg"


# =========================================================
# DỮ LIỆU CV
# =========================================================
NAME = "TRẦN VĂN LỢI"
ROLE = "THỰC TẬP SINH"

PHONE = "0372763338"
EMAIL = "loitran260505@gmail.com"

ADDRESS = """496/63/2D Dương Quảng Hàm P6
Gò Vấp"""

EDUCATION_TITLE = 'Sinh viên năm 3 Ngành “Tài chính ngân hàng”'
EDUCATION_YEARS = "2023 - 2026"
EDUCATION_SCHOOL = "Trường Đại học Nguyễn Tất Thành"

CAREER_OBJECTIVE = (
    "Là sinh viên năm 3 chuyên ngành Tài Chính - Ngân hàng tại Trường "
    "Đại Học Nguyễn Tất Thành, đang tìm kiếm cơ hội được tại vị trí khởi "
    "đầu thực tập tại Ngân hàng Thương mại Cổ phần Ngoại thương Việt Nam "
    "(Vietcombank), để áp dụng những kiến thức và kỹ năng đã tích lũy, "
    "cùng với tinh thần ham học hỏi sẽ tiếp thu được nhiều kinh nghiệm "
    "hơn và phát bản thân trở thành một chuyên viên tài chính có năng lực, "
    "đóng góp và sự phát triển cho doanh nghiệp"
)

SKILLS = [
    "Kỹ năng tin học văn phòng: Word, Excel, Powerpoint",
    "Kỹ năng giao tiếp",
    "Kỹ năng làm việc nhóm",
    "Kỹ năng quản lý thời gian",
]

HOBBIES = [
    "Du lịch",
    "Thể thao",
    "Thích khám phá những thứ mới mẻ",
]

ACTIVITIES = [
    {
        "date": "Tháng 3/2025",
        "content": (
            "Tham gia học tập và thực hành phân tích đầu tư chứng khoán "
            "tại Công ty Chứng khoán Rồng Việt và Công ty Chứng khoán Phú Hưng"
        ),
    },
    {
        "date": "Tháng 11/2025",
        "content": (
            "Tham gia học tập và thức hành Thẩm định Tín dụng "
            "tại Ngân hàng Vietcombank - Thống Nhất"
        ),
    },
]


# =========================================================
# ĐỌC ẢNH CHÂN DUNG
# =========================================================
photo_b64 = ""

if PHOTO_PATH.exists():
    photo_b64 = base64.b64encode(PHOTO_PATH.read_bytes()).decode("utf-8")


if photo_b64:
    photo_html = (
        f'<img class="avatar" '
        f'src="data:image/jpeg;base64,{photo_b64}" '
        f'alt="Trần Văn Lợi">'
    )
else:
    photo_html = '<div class="avatar avatar-placeholder">ẢNH</div>'


# =========================================================
# CSS
# =========================================================
st.markdown(
    """
    <style>

    /* ================================
       FONT
    ================================= */
    @import url(
        'https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800'
        '&family=Libre+Baskerville:wght@400;700'
        '&display=swap'
    );

    /* ================================
       MÀU CHỦ ĐẠO
    ================================= */
    :root {
        --green: #2b8176;
        --green-dark: #236f66;
        --text: #181818;
        --white: #ffffff;
    }

    /* ================================
       NỀN STREAMLIT
    ================================= */
    .stApp {
        background: #eeeeee;
    }

    [data-testid="stAppViewContainer"]
    .main
    .block-container {
        max-width: 1180px;
        padding: 28px 22px 45px;
    }

    /* ================================
       KHUNG CV
    ================================= */
    .cv-page {
        width: 100%;
        min-height: 1490px;
        background: var(--white);
        overflow: hidden;
        box-shadow: 0 8px 28px rgba(0, 0, 0, 0.08);
        font-family: 'Libre Baskerville', Georgia, serif;
        color: var(--text);
    }

    .cv-grid {
        display: grid;
        grid-template-columns: 39% 61%;
    }

    /* ================================
       CỘT TRÁI
    ================================= */
    .left {
        background: var(--green);
        color: white;
        padding: 34px 30px 52px;
        min-height: 1490px;

        border-radius:
            0
            0
            62px
            62px;
    }

    /* ================================
       CỘT PHẢI
    ================================= */
    .right {
        background: white;
        padding: 52px 42px 70px 46px;
    }

    /* ================================
       ẢNH
    ================================= */
    .avatar-wrap {
        display: flex;
        justify-content: center;
        margin: 0 auto 36px;
    }

    .avatar {
        width: 248px;
        height: 248px;

        border-radius: 50%;
        object-fit: cover;
        object-position: center 18%;

        display: block;
    }

    .avatar-placeholder {
        display: flex;
        justify-content: center;
        align-items: center;

        background: #4b97d8;

        font-family: 'Be Vietnam Pro', sans-serif;
        font-size: 22px;
        font-weight: 700;
    }

    /* ================================
       TIÊU ĐỀ CỘT TRÁI
    ================================= */
    .left-heading {
        margin: 26px 0 18px;

        font-size: 22px;
        font-weight: 700;

        letter-spacing: 0.2px;
    }

    /* ================================
       THÔNG TIN LIÊN HỆ
    ================================= */
    .contact-row {
        display: grid;

        grid-template-columns: 38px 1fr;

        gap: 12px;

        align-items: center;

        margin: 14px 0;

        font-size: 16px;

        line-height: 1.55;
    }

    .contact-icon {
        width: 34px;
        height: 34px;

        border-radius: 50%;

        background: white;

        color: var(--green);

        display: flex;

        align-items: center;
        justify-content: center;

        font-family: 'Be Vietnam Pro', sans-serif;

        font-size: 17px;
        font-weight: 800;
    }

    /* ================================
       BOX TIÊU ĐỀ TRÁI
    ================================= */
    .left-section-title {
        background: white;
        color: var(--green);

        text-align: center;

        font-size: 19px;
        font-weight: 700;

        padding: 10px 12px 9px;

        margin:
            28px
            -6px
            26px;

        font-family:
            'Libre Baskerville',
            Georgia,
            serif;
    }

    /* ================================
       HỌC VẤN
    ================================= */
    .education,
    .skills {
        font-size: 15.2px;

        line-height: 1.9;
    }

    .education p {
        margin: 0 0 7px;
    }

    /* ================================
       KỸ NĂNG
    ================================= */
    .skills ul {
        padding-left: 24px;

        margin: 0;
    }

    .skills li {
        margin-bottom: 8px;
    }

    /* ================================
       TÊN
    ================================= */
    .name {
        color: var(--green);

        font-family:
            'Libre Baskerville',
            Georgia,
            serif;

        font-size: 44px;

        line-height: 1.12;

        font-weight: 700;

        letter-spacing: 1px;

        margin: 0 0 26px;

        text-align: center;
    }

    /* ================================
       VỊ TRÍ
    ================================= */
    .role {
        display: inline-block;

        color: white;

        background: var(--green);

        font-size: 21px;

        font-weight: 700;

        padding: 9px 20px 8px;

        border-radius: 22px;

        margin-bottom: 28px;
    }

    /* ================================
       SECTION
    ================================= */
    .section {
        margin: 12px 0 38px;
    }

    .section-head {
        display: flex;

        align-items: center;

        margin-bottom: 36px;
    }

    .pill {
        background: var(--green);

        color: white;

        border-radius: 24px;

        padding:
            9px
            20px
            8px;

        font-size: 18px;

        line-height: 1.18;

        font-weight: 700;

        white-space: nowrap;
    }

    .rule {
        height: 1px;

        background: #2f2f2f;

        flex: 1;

        margin-left: 12px;
    }

    /* ================================
       NỘI DUNG
    ================================= */
    .body {
        font-size: 15.2px;

        line-height: 1.95;

        text-align: left;
    }

    .body p {
        margin: 0;
    }

    /* ================================
       SỞ THÍCH
    ================================= */
    .hobby-list {
        padding-left: 24px;

        margin: 0;
    }

    .hobby-list li {
        margin-bottom: 5px;

        font-size: 15.3px;

        line-height: 1.9;
    }

    /* ================================
       HOẠT ĐỘNG
    ================================= */
    .activity {
        margin-bottom: 30px;

        font-size: 15.2px;

        line-height: 1.95;
    }

    .activity-date {
        margin-bottom: 4px;
    }

    .activity-text {
        padding-left: 25px;

        position: relative;
    }

    .activity-text::before {
        content: '•';

        position: absolute;

        left: 1px;

        top: 0;

        font-size: 22px;
    }

    /* ================================
       RESPONSIVE
    ================================= */
    @media (max-width: 900px) {

        .cv-grid {
            grid-template-columns: 1fr;
        }

        .left {
            min-height: unset;

            border-radius: 0;
        }

        .right {
            padding:
                36px
                28px
                50px;
        }

        .cv-page {
            min-height: unset;
        }

        .name {
            font-size: 36px;
        }
    }

    @media (max-width: 580px) {

        [data-testid="stAppViewContainer"]
        .main
        .block-container {
            padding: 0;
        }

        .cv-page {
            box-shadow: none;
        }

        .left,
        .right {
            padding-left: 22px;
            padding-right: 22px;
        }

        .pill,
        .role {
            white-space: normal;
            text-align: center;
        }

        .name {
            font-size: 30px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# HTML CV
# =========================================================
activities_html = ""

for item in ACTIVITIES:
    activities_html += f"""
        <div class="activity">
            <div class="activity-date">
                {item["date"]}
            </div>

            <div class="activity-text">
                {item["content"]}
            </div>
        </div>
    """


skills_html = "".join(
    f"<li>{skill}</li>"
    for skill in SKILLS
)

hobbies_html = "".join(
    f"<li>{hobby}</li>"
    for hobby in HOBBIES
)


cv_html = f"""
<div class="cv-page">

    <div class="cv-grid">

        <!-- =====================================================
             CỘT TRÁI
        ====================================================== -->
        <aside class="left">

            <div class="avatar-wrap">
                {photo_html}
            </div>


            <!-- THÔNG TIN CÁ NHÂN -->
            <div class="left-heading">
                THÔNG TIN CÁ NHÂN
            </div>


            <div class="contact-row">
                <div class="contact-icon">
                    ☎
                </div>

                <div>
                    {PHONE}
                </div>
            </div>


            <div class="contact-row">
                <div class="contact-icon">
                    ✉
                </div>

                <div>
                    {EMAIL}
                </div>
            </div>


            <div class="contact-row">
                <div class="contact-icon">
                    ⌂
                </div>

                <div>
                    {ADDRESS.replace(chr(10), "<br>")}
                </div>
            </div>


            <!-- HỌC VẤN -->
            <div class="left-section-title">
                HỌC VẤN
            </div>

            <div class="education">

                <p>
                    {EDUCATION_TITLE}
                </p>

                <p>
                    {EDUCATION_YEARS}
                </p>

                <p>
                    {EDUCATION_SCHOOL}
                </p>

            </div>


            <!-- KỸ NĂNG -->
            <div class="left-section-title">
                KỸ NĂNG
            </div>

            <div class="skills">

                <ul>
                    {skills_html}
                </ul>

            </div>

        </aside>


        <!-- =====================================================
             CỘT PHẢI
        ====================================================== -->
        <main class="right">

            <!-- TÊN -->
            <div class="name">
                {NAME}
            </div>


            <!-- VỊ TRÍ -->
            <div class="role">
                {ROLE}
            </div>


            <!-- =================================================
                 MỤC TIÊU NGHỀ NGHIỆP
            ================================================== -->
            <section class="section">

                <div class="section-head">

                    <div class="pill">
                        MỤC TIÊU NGHỀ NGHIỆP
                    </div>

                    <div class="rule"></div>

                </div>


                <div class="body">

                    <p>
                        {CAREER_OBJECTIVE}
                    </p>

                </div>

            </section>


            <!-- =================================================
                 SỞ THÍCH
            ================================================== -->
            <section class="section">

                <div class="section-head">

                    <div class="pill">
                        SỞ THÍCH
                    </div>

                    <div class="rule"></div>

                </div>


                <div class="body">

                    <ul class="hobby-list">

                        {hobbies_html}

                    </ul>

                </div>

            </section>


            <!-- =================================================
                 HOẠT ĐỘNG NGOẠI KHÓA
            ================================================== -->
            <section class="section">

                <div class="section-head">

                    <div class="pill">
                        HOẠT ĐỘNG NGOẠI KHÓA
                    </div>

                    <div class="rule"></div>

                </div>


                <div class="body">

                    {activities_html}

                </div>

            </section>

        </main>

    </div>

</div>
"""


st.markdown(
    cv_html,
    unsafe_allow_html=True
)
