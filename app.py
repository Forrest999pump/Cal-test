from flask import Flask, render_template, request, jsonify
from calculator import calculate, format_number

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def do_calculate():
    data = request.get_json()
    try:
        raw1 = data.get('num1', '')
        raw2 = data.get('num2', '')
        operator = data.get('operator', '')

        num1 = float(raw1) if '.' in str(raw1) else int(raw1)
        num2 = float(raw2) if '.' in str(raw2) else int(raw2)

        if operator not in ('+', '-', '*', '/'):
            return jsonify({'error': 'เครื่องหมายไม่ถูกต้อง'}), 400

        result = calculate(num1, operator, num2)

        if result is None:
            return jsonify({'error': f'ไม่สามารถหารด้วย 0 ได้ ({num1} / 0 = ไม่มีคำตอบ)'}), 400

        return jsonify({
            'num1': format_number(num1),
            'num2': format_number(num2),
            'operator': operator,
            'result': format_number(result),
        })

    except (ValueError, TypeError):
        return jsonify({'error': 'กรุณาป้อนตัวเลขให้ถูกต้อง'}), 400


if __name__ == '__main__':
    app.run(debug=True)
