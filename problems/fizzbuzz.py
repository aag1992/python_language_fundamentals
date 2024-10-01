def fizzbuzz(num):
    for i in range(num):
        if (i % 3 == 0) and (i % 5 == 0):
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        print(i)


fizzbuzz(100)
