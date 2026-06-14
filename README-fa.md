نسخه فارسی
معرفی پروژه
توسعه دهنده: فریبرز زمانی
ایمیل: fariborz499@gmail.com
تکنولوژی‌های استفاده شده: Django 4.2، Python، Bootstrap 5، SQLite، Pandas

این پروژه چیکار می‌کنه؟
یک داشبورد قدرتمند تحت وب برای مدیریت دیتاست‌های اکسل. کاربران می‌توانند فایل‌های اکسل خود را آپلود کنند، در دیتابیس ذخیره کنند و از طریق رابط کاربری وب یا API به آن‌ها دسترسی داشته باشند.

قابلیت‌های اصلی:
✅ آپلود فایل‌های اکسل (xlsx, xls)

✅ استخراج و ذخیره خودکار داده‌ها

✅ احراز هویت و مدیریت کاربران

✅ مشاهده لیست، جزئیات و حذف دیتاست‌ها

✅ صفحه‌بندی برای دیتاست‌های حجیم

✅ رابط کاربری واکنش‌گرا با Bootstrap 5

✅ API قدرتمند برای دسترسی برنامه‌نویسی

✅ پشتیبانی کامل از زبان فارسی

✅ اعتبارسنجی حجم فایل (حداکثر ۱۰ مگابایت)

✅ پردازش امن فایل‌ها

آدرس‌های API:
متد	آدرس	توضیحات
GET	/api/datasets/	دریافت لیست همه دیتاست‌ها
GET	/api/datasets/<id>/	دریافت جزئیات یک دیتاست
POST	/api/upload/	آپلود فایل اکسل جدید
نصب و راه‌اندازی:
bash
# کلون کردن پروژه
git clone [آدرس-ریپازیتوری-شما]

# ساخت محیط مجازی
python -m venv venv

# فعال کردن محیط مجازی (ویندوز)
venv\Scripts\activate

# نصب پیش‌نیازها
pip install django pandas openpyxl crispy-forms crispy-bootstrap5

# اجرای مایگریشن‌ها
python manage.py makemigrations
python manage.py migrate

# ساخت کاربر ادمین
python manage.py createsuperuser

# اجرای سرور
python manage.py runserver
نقاط دسترسی:
برنامه وب: http://127.0.0.1:8000/

پنل مدیریت: http://127.0.0.1:8000/admin/

مستندات API: http://127.0.0.1:8000/api-setup/

موارد استفاده:
تحلیلگران داده: ذخیره و مدیریت چندین دیتاست اکسل

سازمان‌ها: سیستم متمرکز ذخیره‌سازی داده

توسعه‌دهندگان: اتصال به برنامه‌های دیگر از طریق API

محققان: مدیریت کارآمد داده‌های تحقیقاتی

مزایای رقابتی / Competitive Advantages:
English:
User-friendly Interface: Simple and intuitive design

Scalable: Can handle large datasets efficiently

Secure: Each user accesses only their own data

Flexible: REST API for integration with any platform

Fast: Optimized database queries and pagination

فارسی:
رابط کاربری ساده: طراحی ساده و کاربرپسند

مقیاس‌پذیر: مدیریت کارآمد دیتاست‌های حجیم

امن: هر کاربر فقط به داده‌های خود دسترسی دارد

انعطاف‌پذیر: API REST برای اتصال به هر پلتفرمی

سریع: کوئری‌های بهینه‌شده دیتابیس و صفحه‌بندی

تماس با توسعه دهنده / Contact Developer:
Email: fariborz499@gmail.com

پیشنهادات و انتقادات: خوشحال می‌شم از نظرات شما برای بهبود این پروژه استفاده کنم.
Suggestions & Feedback: I'd be happy to use your feedback to improve this project.

لایسنس / License:
این پروژه متن‌باز است و می‌توانید آزادانه از آن استفاده کنید.
This is an open-source project and you can freely use it.
<img width="1690" height="876" alt="api" src="https://github.com/user-attachments/assets/aca09b04-ddc0-44c0-827e-eb41cb146f04" />
<img width="1874" height="903" alt="dashboard" src="https://github.com/user-attachments/assets/6851edd8-8f8c-4ef4-89dc-ec4d393e013d" />
<img width="1780" height="919" alt="detail" src="https://github.com/user-attachments/assets/63338902-fc19-42a1-ac26-22f4e042bb5b" />
<img width="1849" height="802" alt="home" src="https://github.com/user-attachments/assets/14d7b92c-13ef-408a-ae4e-8c6f2faaf47b" />
