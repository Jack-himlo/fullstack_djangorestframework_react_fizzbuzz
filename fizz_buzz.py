# fizz-buzz



def fizz_buzz(int):
    num = int
    for num in range(0,num):
        if num % 3 == 0 and num % 5 == 0:
            print(f"Fizz-Buzz")

        if num % 5 == 0:
            print(f"Buzz")

        if num % 3 == 0:
            print(f"Fizz")
        else:
            return f"{num}"

print(fizz_buzz(15))            