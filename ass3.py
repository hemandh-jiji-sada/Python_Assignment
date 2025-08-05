units = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000
}

def get_input(msg):
    while True:
        val = input(msg).strip().lower()
        if val in ["q", "quit"]: return "quit"
        return val

def get_number():
    while True:
        val = get_input("Enter value to convert (or 'q' to quit): ")
        if val == "quit": return "quit"
        try: return float(val)
        except: print("Error: Enter a valid number.")

def get_unit(prompt):
    while True:
        unit = get_input(prompt)
        if unit == "quit": return "quit"
        if unit in units: return unit
        print("Error: Use mm, cm, m, or km.")

print("=== Length Unit Converter ===")
while True:
    val = get_number()
    if val == "quit": break
    from_u = get_unit("From unit (mm, cm, m, km): ")
    if from_u == "quit": break
    to_u = get_unit("To unit (mm, cm, m, km): ")
    if to_u == "quit": break

    result = val * units[from_u] / units[to_u]
    print(f"{val} {from_u} is equal to {result:.4f} {to_u}")
