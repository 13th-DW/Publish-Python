bracket_expression_argument = int(
    input("Ведите аргумент для вычисления количества правильных скобочных выражений: ")
)

if bracket_expression_argument < 0:
    print("Это отрицательное число, с такими не работаем.")
else:

    def Catalans_number(bracket_expression_argument):
        if bracket_expression_argument >= 2:
            c = (
                (2 * ((2 * bracket_expression_argument) - 1))
                / (bracket_expression_argument + 1)
            ) * Catalans_number(bracket_expression_argument - 1)
            return int(c)
        return 1

    print(
        "Для числа "
        + str(bracket_expression_argument)
        + " количество правильных скобочных выражений: "
        + str(Catalans_number(bracket_expression_argument))
        + "!"
    )
