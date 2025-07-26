import random

D = int(input("Enter the range of numbers you want to guess from:\n"))

N = random.randint(1,D)

G = 0

A = 0

while G != N:

    G = int(input("Enter a number:\n"))

    if G == N - 1 or G == N + 1:

     print("You are really close!")

     A += 1

    elif G < N:

        print("Guess higher")

        A += 1

    elif G > N:

        print("Guess lower")

        A += 1

    else:

        print("Congratulations, you won!")

        print("It took you", A, "attempts to guess the number!")