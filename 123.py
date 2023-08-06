def isPrime(number):
    count = 0
    for d in range(1, number + 1):
        if number % d == 0:
      if count == 2 or count == 1:
        print("Число является простым")
        count = 0
    else:
        print("Число не является простым")
        count = 0


number = int(input("Введите количество чисел последовательности: "))
for i in range(number):
    number = int(input("Введите число: "))
    isPrime(number)