# ​ Advanced Password Generation (Flask App)

یک اپلیکیشن تحت وب با Python + Flask برای تولید رمز عبور قوی و امن.

Demo Online: [لینک دمو](https://younes23.pythonanywhere.com/)

---

##  ویژگی‌ها
- رابط وب ساده ساخته‌شده با Flask
- تولید پسورد امن و تصادفی با تنظیمات دلخواه (طول، حروف کوچک/بزرگ، اعداد، نمادها)
- بدون نیاز به دیتابیس
- قابل استقرار روی سرورهای رایگان (Render, Railway, Heroku و…)

---

##  پیش‌نیازها
- **Python 3.10+**
- **Flask 3.1.1** (منتشرشده در 13 می 2025)

---

##  نصب و اجرا (روی لوکال)
```bash
git clone https://github.com/younesnoorzahi/Advanced-password-generation.git
cd Advanced-password-generation

# ایجاد محیط مجازی (اختیاری اما توصیه‌شده)
python -m venv venv
source venv/bin/activate    # در لینوکس / مک
venv\Scripts\activate       # در ویندوز

pip install -r requirements.txt

# اجرای اپلیکیشن
python main.py
