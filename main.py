from flask import Flask, render_template_string, request
import random
import string

app = Flask(__name__)

def generate_password(length=16, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    chars = ""
    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        return "لطفاً حداقل یک نوع کاراکتر انتخاب کنید!"

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

html_template = """
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تولید رمز عبور پیشرفته</title>
    <link rel="icon" href="https://cdn-icons-png.flaticon.com/512/6195/6195699.png">
    <style>
        @import url('https://v1.fontapi.ir/css/Vazir:100;300;400;500;700');

        * {
            box-sizing: border-box;
        }

        body {
            font-family: 'Vazir', sans-serif;
            background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            padding: 0;
        }

        .password-box {
            background: rgba(255, 255, 255, 0.95);
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            text-align: center;
            width: 350px;
            transition: all 0.3s ease;
        }

        .password-box:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.3);
        }

        h2 {
            margin-bottom: 20px;
            color: #333;
        }

        .password {
            font-size: 20px;
            font-weight: bold;
            margin: 20px 0;
            padding: 10px;
            background: #f0f0f0;
            border-radius: 8px;
            word-break: break-all;
            color: #007BFF;
            box-shadow: inset 0 2px 5px rgba(0,0,0,0.1);
        }

        form {
            text-align: right;
        }

        label {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin: 10px 0;
            font-size: 14px;
            color: #555;
        }

        input[type="number"] {
            width: 70px;
            padding: 5px 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
            text-align: center;
            transition: all 0.2s ease;
        }

        input[type="number"]:focus {
            border-color: #007BFF;
            outline: none;
            box-shadow: 0 0 5px rgba(0,123,255,0.3);
        }

        input[type="checkbox"] {
            width: 18px;
            height: 18px;
            accent-color: #007BFF;
        }

        button {
            margin-top: 20px;
            width: 100%;
            padding: 12px;
            border: none;
            border-radius: 10px;
            background: #007BFF;
            color: white;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        button:hover {
            background: #0056b3;
            transform: translateY(-2px);
        }
    </style>
</head>
<body>
    <div class="password-box">
        <h2>تولید رمز عبور پیشرفته</h2>
        <div class="password">{{ password }}</div>
        <form method="post">
            <label>طول رمز:
                <input type="number" name="length" value="{{ length }}" min="4" max="64">
            </label>
            <label><input type="checkbox" name="use_lower" {% if use_lower %}checked{% endif %}> حروف کوچک</label>
            <label><input type="checkbox" name="use_upper" {% if use_upper %}checked{% endif %}> حروف بزرگ</label>
            <label><input type="checkbox" name="use_digits" {% if use_digits %}checked{% endif %}> اعداد</label>
            <label><input type="checkbox" name="use_symbols" {% if use_symbols %}checked{% endif %}> کاراکترهای ویژه</label>
            <button type="submit">تولید رمز</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    length = 16
    use_lower = use_upper = use_digits = use_symbols = True

    if request.method == "POST":
        try:
            length = int(request.form.get("length", 16))
        except ValueError:
            length = 16
        use_lower = "use_lower" in request.form
        use_upper = "use_upper" in request.form
        use_digits = "use_digits" in request.form
        use_symbols = "use_symbols" in request.form

    password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
    return render_template_string(html_template, password=password, length=length,
                                  use_lower=use_lower, use_upper=use_upper,
                                  use_digits=use_digits, use_symbols=use_symbols)

if __name__ == "__main__":
    app.run(debug=True)
