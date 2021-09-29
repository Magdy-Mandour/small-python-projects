guess = int(input("Hi, enter any number you like please: "))
def guess_number(n):
    if guess % 2 == 0:
        return "Oh, No this is an even number, Run !!!"
    else:
        return "Oh, No this is an odd number, Run !!!"
print(guess_number(guess))
