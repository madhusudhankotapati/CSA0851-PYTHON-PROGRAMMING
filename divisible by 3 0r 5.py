def check_divisibility():
    num = int(input("Enter a number: "))
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} is divisible by both 3 and 5.")
    else:
        print(f"{num} is not divisible by both 3 and 5.")
check_divisibility()
