# Question 16(a)

# Examination Number: XXXXXX


from random import choice


fruits = ['apple', 'cherry', 'orange']


random_fruit_1 = choice(fruits)

random_fruit_2 = choice(fruits)

random_fruit_3 = choice(fruits)

random_fruit_loop = fruits[0]

apple_count = 0

orange_count = 0

cherry_count = 0


print(f"Random Fruit 1: {random_fruit_1}")

print(f"Random Fruit 2: {random_fruit_2}")

print(f"Random Fruit 3: {random_fruit_3}\n")


if random_fruit_1 == "cherry":

    print("First Fruit is cherry.")


if random_fruit_1 == random_fruit_2:

    print("First pair match.")


if random_fruit_1 == "cherry" and random_fruit_2 == "cherry":

    print("First Pair are cherries.")


if random_fruit_1 == random_fruit_2 or random_fruit_1 == random_fruit_3 or random_fruit_2 == random_fruit_3:

    print("Matching pair.")


for i in range(0,100):

    random_fruit_loop = choice(fruits)

    if random_fruit_loop == "apple":

        apple_count+=1

    elif random_fruit_loop == "cherry":

        cherry_count+=1

    else:

        orange_count+=1


print(f"apple {apple_count}")

print(f"orange {orange_count}")

print(f"cherry {cherry_count}")




# Question 16(b)

# Examination Number: XXXXXX


from random import choice


fruits = ["apple", "cherry", "orange"]


new_fruit = ""

guess = ""

fruit_slot_1 = ""

fruit_slot_2 = ""

fruit_slot_3 = ""

win = 0

attempts = 0


print(f"The initial group of fruits is:\n{fruits}")


new_fruit = input("Please enter a new fruit:\n")

fruits.append(new_fruit)


print(f"The new group of fruits is:\n{fruits}")


while guess not in fruits:

    guess = input("Please enter your chosen fruit:\n")

    if guess in fruits:

        pass

    else:

        print(f"{guess} is not in the list {fruits}.")


while win == 0:

    fruit_slot_1 = choice(fruits)

    fruit_slot_3 = choice(fruits)

    fruit_slot_2 = choice(fruits)

    if fruit_slot_1 == fruit_slot_2 and fruit_slot_2 == fruit_slot_3:

        win = 1

        attempts+=1


print(f"You won in {attempts} attempts.")