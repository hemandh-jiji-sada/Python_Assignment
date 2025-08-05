def convert_temp(choice, temp):
    if choice == '1': return temp * 9/5 + 32, "°F"
    if choice == '2': return (temp - 32) * 5/9, "°C"
    if choice == '3': return temp + 273.15, "K"
    if choice == '4': return temp - 273.15, "°C"

def get_temperature():
    while True:
        val = input("Enter temperature (or 'q' to quit): ").strip().lower()
        if val in ['q', 'quit']: return 'quit'
        try: return float(val)
        except ValueError: print("Error: Please enter a valid number.")

def show_menu():
    print("\nChoose conversion:")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")
    print("3: Celsius to Kelvin")
    print("4: Kelvin to Celsius")
    print("q: Quit")

print("=== Temperature Converter ===")
while True:
    show_menu()
    choice = input("Enter option: ").strip().lower()
    if choice in ['q', 'quit']: break
    if choice not in ['1', '2', '3', '4']:
        print("Error: Invalid choice. Please select a valid option.")
        continue

    temp = get_temperature()
    if temp == 'quit': break

    converted, unit = convert_temp(choice, temp)
    print(f"Result: Converted temperature = {converted:.2f} {unit}")
