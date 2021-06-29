import random 
ascii_1 = ["a","i","o","u","y","e"]
ascii_2buf = "abcdefghijklmopqrstuvwxyz"
ascii_2 = []
choice = [True,False,True]
for letter in ascii_1:
    ascii_2buf = ascii_2buf.replace(letter,"")
for letter in ascii_2buf:
    ascii_2.append(f"{letter}")
print(ascii_2)
def generate(lenn=5):
    lastchoice = None
    word = random.choice(ascii_2)
    if lastchoice == None:
        for x in range(lenn-1):
            if(random.choice(choice)):
                word += random.choice(ascii_1)
                lastchoice = True
            else:
                word += random.choice(ascii_2)
                lastchoice = False
    if(lastchoice):
        word += random.choice(ascii_2)
        lastchoice = False
    else:
        word += random.choice(ascii_1)
        d = random.choice([True,False])
        lastchoice = d
    return word
for x in range(100):
    d = random.randint(5,8)
    print(generate(d))
