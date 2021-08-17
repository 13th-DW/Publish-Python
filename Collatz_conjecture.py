import time

print("")
print(" .d8888b.           888 888          888")
time.sleep(0.1)
print("d88P  Y88b          888 888          888")
time.sleep(0.1)
print("888    888          888 888          888")
time.sleep(0.75)
print("888         .d88b.  888 888  8888b.  888888 88888888")
time.sleep(0.1)
print('888        d88""88b 888 888     "88b 888       d88P')
time.sleep(0.25)
print("888    888 888  888 888 888 .d888888 888      d88P")
time.sleep(0.1)
print("Y88b  d88P Y88..88P 888 888 888  888 Y88b.   d88P")
time.sleep(0.1)
print(' "Y8888P"   "Y88P"  888 888 "Y888888  "Y888 88888888')
time.sleep(0.3)
print("")
print("                           d8b                   888")
time.sleep(0.05)
print("                           Y8P                   888")
time.sleep(0.05)
print("                                                 888")
time.sleep(0.1)
print(" .d8888b .d88b.  88888b.  8888  .d88b.   .d8888b 888888 888  888 888d888 .d88b.")
time.sleep(0.1)
print(
    'd88P"   d88""88b 888 "88b "888 d8P  Y8b d88P"    888    888  888 888P"  d8P  Y8b'
)
time.sleep(0.05)
print(
    "888     888  888 888  888  888 88888888 888      888    888  888 888    88888888"
)
time.sleep(0.05)
print("Y88b.   Y88..88P 888  888  888 Y8b.     Y88b.    Y88b.  Y88b 888 888    Y8b.")
time.sleep(0.05)
print(' "Y8888P "Y88P"  888  888  888  "Y8888   "Y8888P  "Y888  "Y88888 888     "Y8888')
time.sleep(0.05)
print("                           888")
time.sleep(0.05)
print("                          d88P")
time.sleep(0.05)
print('                        888P"')

description_text = [
    [
        "\nThe Collatz conjecture is a conjecture in mathematics that concerns \nsequences defined as follows: start with any positive integer n. \nThen each term is obtained from the previous term as follows: if the \nprevious term is even, the next term is one half of the previous term. \nIf the previous term is odd, the next term is 3 times the previous term plus 1. \nThe conjecture is that no matter what value of n, the sequence will always reach 1."
    ],
    [
        "\nThe conjecture is named after Lothar Collatz, who introduced the idea in 1937, \ntwo years after receiving his doctorate. \nIt is also known as the 3n + 1 problem, the 3n + 1 conjecture, \nthe Ulam conjecture (after Stanisław Ulam), Kakutani's problem (after Shizuo Kakutani), \nthe Thwaites conjecture (after Sir Bryan Thwaites), Hasse's algorithm \n(after Helmut Hasse), or the Syracuse problem.\nThe sequence of numbers involved is sometimes referred to as the\nhailstone sequence or hailstone numbers (because the values are \nusually subject to multiple descents and ascents like hailstones in a cloud), \nor as wondrous numbers."
    ],
    [
        '\nPaul Erdős said about the Collatz conjecture: "Mathematics may not be ready \nfor such problems." He also offered US$500 for its solution. \nJeffrey Lagarias stated in 2010 that the Collatz conjecture \n"is an extraordinarily difficult problem, completely out of reach of present day mathematics."'
    ],
    ["\nLink to Wikipedia: https://en.wikipedia.org/wiki/Collatz_conjecture"],
    [
        "\nConsider the following operation on an arbitrary positive integer:\n - If the number is even, divide it by two.\n - If the number is odd, triple it and add one."
    ],
    [
        "\nBut if we can find a number that will eventually close in a loop other than 4 - 2 - 1,\nor will lead to infinity at the end of the calculations, we will be able\nto refute this conjunction. Let's try to find it.\n"
    ],
]

for string in description_text:
    l = list("".join(string))
    for char in l:
        print(char, end="", flush=True)
        time.sleep(0.025)
    print(end="\n")


def collatz_conjecture():
    calculation_number = int(input("Enter the Natural number you want to check: "))

    calculation_number_1 = calculation_number
    step_counter = 0

    while calculation_number_1 not in {0, 1}:
        if calculation_number_1 % 2 == 0:
            print(int(calculation_number_1))
            calculation_number_1 = calculation_number_1 / 2
        elif calculation_number_1 % 2 != 0:
            print(int(calculation_number_1))
            calculation_number_1 = (3 * calculation_number_1) + 1
        step_counter += 1

    print(
        "Entered number "
        + str(int(calculation_number))
        + "\n"
        + "Steps "
        + str(int(step_counter))
        + "\n"
        + "Result "
        + str(int(calculation_number_1))
        + "\n"
    )

    continue_test = input("Want to try some more?(Y/N): ")

    if continue_test in {"Y", "y"}:
        collatz_conjecture()
    else:
        print("See you later!")


collatz_conjecture()
