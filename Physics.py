def calculate_force():
  print("\n--- Newton's Second Law (F = m * a) ---")
  mass = float(input("Enter mass (kg): "))
  acceleration = float(input("Enter acceleration (m/s^2): "))
  force = mass * acceleration
  print(f" Result -> Force: {force:.2f} N\n")


def calculate_kinetic_energy():
  print("\n--- Kinetic Energy (KE = 1/2 * m * v^2) ---")
  mass = float(input("Enter mass (kg): "))
  velocity = float(input("Enter velocity (m/s): "))
  ke = 0.5 * mass * (velocity**2)
  print(f" Result -> Kinetic Energy: {ke:.2f} J\n")


def calculate_voltage():
  print("\n--- Ohm's Law (V = I * R) ---")
  current = float(input("Enter current (Amps): "))
  resistance = float(input("Enter resistance (Ohms): "))
  voltage = current * resistance
  print(f" Result -> Voltage: {voltage:.2f} V\n")


def calculate_potential_energy():
  print("\n--- Gravitational Potential Energy (PE = m * g * h) ---")
  mass = float(input("Enter mass (kg): "))
  height = float(input("Enter height (m): "))
  gravity_input = input(
      "Enter acceleration due to gravity (press Enter for default 9.81): "
  )
  gravity = float(gravity_input) if gravity_input else 9.81
  pe = mass * gravity * height
  print(f" Result -> Potential Energy: {pe:.2f} J\n")


def calculate_speed():
  print("\n--- Average Speed (v = d / t) ---")
  distance = float(input("Enter distance (m): "))
  time = float(input("Enter time (s): "))
  if time == 0:
    print(" Error: Time cannot be zero.\n")
    return
  speed = distance / time
  print(f"✨ Result -> Speed: {speed:.2f} m/s\n")


def main():
  while True:
    print("=================================")
    print("      PHYSICS FORMULA MENU       ")
    print("=================================")
    print("1. Newton's Second Law (Force)")
    print("2. Kinetic Energy")
    print("3. Ohm's Law (Voltage)")
    print("4. Gravitational Potential Energy")
    print("5. Average Speed")
    print("6. Exit")
    print("---------------------------------")

    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
      calculate_force()
    elif choice == "2":
      calculate_kinetic_energy()
    elif choice == "3":
      calculate_voltage()
    elif choice == "4":
      calculate_potential_energy()
    elif choice == "5":
      calculate_speed()
    elif choice == "6":
      print(" Exiting calculator. Goodbye!")
      break
    else:
      print(" Invalid choice. Please enter a number between 1 and 6.\n")


if __name__ == "__main__":
  main()