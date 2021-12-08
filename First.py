number1 = int(input("Введите  число один: "))
number2 = int(input("Введите  число два: "))

revs_number2 = 0
revs_number1 = 0
revs_result = 0


def function(number, revs):
    revs = 0
    while (number > 0):
        remainder = number % 10
        revs = (revs * 10) + remainder
        number = number // 10
    return revs


sum1 = function(number1, revs_number1)
print("1 число наоборот :", sum1)

sum2 = function(number2, revs_number2)
print("1 число наоборот :", sum2)

result = sum1 + sum2
print('Сумма: ', result)

revers_summa = function(result, revs_result)

print("Сумма наоборот: ", revers_summa)
