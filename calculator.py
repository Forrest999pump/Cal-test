# ===================================
# เครื่องคิดเลข (Calculator)
# ===================================

def get_number(prompt):
    """รับค่าตัวเลขจากผู้ใช้ (Integer หรือ Float)"""
    while True:
        try:
            value = input(prompt)
            # แปลงเป็น int ถ้าเป็นจำนวนเต็ม ไม่งั้นแปลงเป็น float
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            print("  [!] กรุณาป้อนตัวเลขให้ถูกต้อง เช่น 10 หรือ 3.14")


def get_operator():
    """รับเครื่องหมายดำเนินการจากผู้ใช้"""
    valid_operators = ['+', '-', '*', '/']
    while True:
        operator = input("ป้อนเครื่องหมาย (+, -, *, /): ").strip()
        if operator in valid_operators:
            return operator
        else:
            print("  [!] กรุณาเลือกเครื่องหมายที่ถูกต้อง: +, -, *, /")


def calculate(num1, operator, num2):
    """ประมวลผลการคำนวณตามเครื่องหมายที่เลือก"""
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                return None  # หารด้วยศูนย์ไม่ได้
            return num1 / num2


def format_number(value):
    """จัดรูปแบบตัวเลข: ถ้าเป็น .0 ให้แสดงเป็น int"""
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def main():
    print("=" * 40)
    print("     เครื่องคิดเลข (Calculator)")
    print("=" * 40)

    # --- ส่วนรับข้อมูล (Inputs) ---
    num1 = get_number("ป้อนตัวเลขที่ 1: ")
    operator = get_operator()
    num2 = get_number("ป้อนตัวเลขที่ 2: ")

    # --- ส่วนประมวลผล (Process) ---
    result = calculate(num1, operator, num2)

    # --- ส่วนแสดงผล (Output) ---
    print("-" * 40)
    if result is None:
        print(f"  [!] ไม่สามารถหารด้วย 0 ได้ ({num1} / 0 = ไม่มีคำตอบ)")
    else:
        n1 = format_number(num1)
        n2 = format_number(num2)
        res = format_number(result)
        print(f"  ผลลัพธ์: {n1} {operator} {n2} = {res}")
    print("=" * 40)


if __name__ == "__main__":
    main()
