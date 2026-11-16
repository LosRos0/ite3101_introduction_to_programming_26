from typing import List


def list_function(x: List[int]) -> List[int]:
    return x


n = [3, 5, 7]
print(list_function(n))

guesses_left = 3

while guesses_left > 0:
    guess = int(input("Your guess: "))

    if guess == 5:
        print("You win!")
        break

    guesses_left -= 1
else:
    print("You lose.")