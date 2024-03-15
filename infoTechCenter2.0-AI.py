import time
import sys

# Function to print a message slowly, creating a typewriter effect
def print_slow(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# Function to print loading message with ellipsis
def print_loading_message(ellipsis):
    message = f"InfoTech Center System Loading{'.' * ellipsis}"
    sys.stdout.write(f"\r{message}")
    sys.stdout.flush()

# Main function to execute the program
def main():
    # Time delay between messages
    time_to_sleep = 1
    # Initial ellipsis count
    ellipsis = 0

    # Welcome message and initialization
    print("\n\n\nWelcome to InfoTech Center Version 2.0\n")
    print_slow("Initializing components... ", 0.02)
    time.sleep(time_to_sleep)

    # System check
    print_slow("\nChecking system integrity... ", 0.02)
    time.sleep(time_to_sleep)

    # Performance optimization
    print_slow("\nOptimizing performance... ", 0.02)
    time.sleep(time_to_sleep)

    # Security boot-up
    print_slow("\nBooting up security protocols... ", 0.02)
    time.sleep(time_to_sleep)

    # Loading user interface
    print_slow("\nLoading user interface... ", 0.02)
    time.sleep(time_to_sleep)

    print("\n")  # New line before loading animation

    # Loading animation
    for x in range(20):
        print_loading_message(ellipsis)
        ellipsis = (ellipsis + 1) % 4
        time.sleep(0.1)

    # System loaded successfully
    print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!")

if __name__ == "__main__":
    main()
