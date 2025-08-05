def get_number(prompt):
    while True:
        val = input(prompt).strip().lower()
        if val in ['q', 'quit']: return 'quit'
        try: return float(val)
        except ValueError: print("Error: Please enter a valid number.")

def get_operation():
    ops = ['+', '-', '*', '/', '**', '%']
    while True:
        op = input("Enter operation (+, -, *, /, **, %): ").strip()
        if op.lower() in ['q', 'quit']: return 'quit'
        if op in ops: return op
        print("Error: Invalid operation.")

def calculate(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b
    if op == '**': return a ** b
    if op == '%': return a % b

print("=== Smart Calculator ===")
while True:
    a = get_number("First number (or 'q' to quit): ")
    if a == 'quit': break

    b = get_number("Second number (or 'q' to quit): ")
    if b == 'quit': break

    op = get_operation()
    if op == 'quit': break

    if op in ['/', '%'] and b == 0:
        print("Error: Cannot divide by zero!")
        continue

    result = calculate(a, b, op)
    print(f"Result: {a} {op} {b} = {result}")
