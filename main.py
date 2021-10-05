import csv
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

html = """\
<p>
    <strong>
        Kính gửi: Các bạn sinh viên đã đạt đủ tiêu chí “ Sinh viên 5 tốt” năm
        học 2020 - 2021 của trường Đại học Công nghệ.
    </strong>
</p>
<p>
    ĐTN - HSV trường Đại học Công nghệ xin chúc mừng các bạn đã đạt đủ các tiêu
    chí để trở thành Sinh viên 5 tốt năm học 2020 - 2021. Để chuẩn bị tốt hồ sơ
    của mình, các bạn vui lòng lưu ý 1 số công việc dưới đây:
</p>
<p>
    <strong>1.</strong>
    Tham gia vào group facebook “ SINH VIÊN 5 TỐT TRƯỜNG ĐẠI HỌC CÔNG NGHỆ -
    ĐHQGHN ” để cập nhật các thông báo hỗ trợ làm hồ sơ. Link group:
    <a href="https://www.facebook.com/groups/130215847732795">
        https://www.facebook.com/groups/130215847732795
    </a>
</p>
<p>
    <strong>2. </strong>
Hướng dẫn chuẩn bị hồ sơ:    <a href="https://bit.ly/2RvwXpo">https://bit.ly/2RvwXpo</a>
</p>
<p>
    <strong>3. </strong>
    Hoàn thiện hồ sơ, tổng hợp hồ sơ lên link drive của các bạn và nộp hồ sơ ở
    link dưới đây:
    <a href="https://forms.gle/6JvHYtWoEZioBpug8">
        https://forms.gle/6JvHYtWoEZioBpug8
    </a>
</p>
<ul type="disc">
    <li>
        <strong>Lưu ý: </strong>
        Các bạn có thể nộp trước link drive và update từng phần hồ sơ, thời hạn
        hoàn thiện hồ sơ đến 00h ngày 13/10/2021. <strong></strong>
    </li>
</ul>
<p>
    <strong>Mọi chi tiết xin liên hệ: </strong>
    Đ/c Phan Hoàng Anh - Chủ tịch Hội Sinh viên, SĐT: 0398174438.
</p>
<p>
    Hoặc Đ/c Nguyễn Thị Ngọc Mai - Phó chủ tịch Hội Sinh viên, SĐT: 0357442759.
</p>
<p>
    Trân trọng cảm ơn./.
</p>
<p>
    ------------------------
</p>
<p>
    Văn phòng Đoàn Thanh niên - Hội Sinh viên trường Đại học Công nghệ
</p>
<p>
    (Tòa nhà G3 trường ĐH Công nghệ - 144 Xuân Thuỷ, Cầu Giấy, Hà Nội)
</p>
<p>
📧 Email:    <a href="mailto:vpdoandhcn@gmail.com">mailto:vpdoandhcn@gmail.com</a>
</p>
<p>
    hoặc
</p>
<a href="mailto:hoisinhviendhcongnghe.vnu@gmail.com">
    mailto:hoisinhviendhcongnghe.vnu@gmail.com
</a>

"""
message = MIMEMultipart()
message.attach(MIMEText(html, "html"))
message["Subject"]="ĐTN - HSV.  HỖ TRỢ LÀM HỒ SƠ SINH VIÊN 5 TỐT TRƯỜNG ĐHCN"
sender_email = "huyenbui117@gmail.com"
password = input("Type your password and press enter: ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    with open("contacts_file.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for receiver_email in reader:
            server.sendmail(
                sender_email,
                receiver_email,
                message.as_string()
            )
