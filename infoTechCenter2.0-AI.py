import time
import sys

def print_loading_message(ellipsis):
    message = f"InfoTech Center System Loading{'.' * ellipsis}"
    sys.stdout.write(f"\r{message}")
    sys.stdout.flush()

def print_slow(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    time_to_sleep = 1
    ellipsis = 0

    print("\n\n\nWelcome to InfoTech Center Version 2.0\n")
    print_slow("Initializing components... ", 0.02)
    time.sleep(time_to_sleep)

    print_slow("\nChecking system integrity... ", 0.02)
    time.sleep(time_to_sleep)

    print_slow("\nOptimizing performance... ", 0.02)
    time.sleep(time_to_sleep)

    print_slow("\nBooting up security protocols... ", 0.02)
    time.sleep(time_to_sleep)

    print_slow("\nLoading user interface... ", 0.02)
    time.sleep(time_to_sleep)

    print("\n")
    for x in range(20):
        print_loading_message(ellipsis)
        ellipsis = (ellipsis + 1) % 4
        time.sleep(0.1)

    print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!")

if __name__ == "__main__":
    main()
