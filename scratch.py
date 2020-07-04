import random
from datetime import datetime

words = ["fox", "box", "code", "run", "away", "hack", "good", "password", "paw", "cute", "cat", "dog", "game", "ahri",
         "fish", "girl", "are", "you", "reading", "this", "dummy", "happy", "cactus", "kill", "end", "email", "dark",
         "sad", "kid", "solo", "learn", "night", "sun", "moon", "light", "cookies", "howl", "sky", "boy", "toy", "kiss",
         "bliss", "phone", "home", "rome", "anime", "hand", "feet", "drool", "jump", "shy", "troll", "running", "bear",
         "tree", "free", "me", "from", "this", "rainbow", "prison", "card", "key", "hugging", "flower", "python",
         "alone", "play", "player", "friend", "tower", "funny", "bun", "bunny", "earth", "memory", "town", "toe",
         "lips", "makeup", "yummy", "pony", "giggling", "private", "secret", "meme", "victory", "square", "pants",
         "sponge", "strong", "jealous", "jelly", "zap", "excited", "quick", "pink", "red", "blue", "cool", "this", "is",
         "super", "awesome", "new", "nice", "strong", "newspaper"]
passwordlist = []
print("***********************************")
print("Password Scrambler V.2.901 developed by Suraj Sharma.")
print("generates a complex password out of a simple input")


def addword():
    global passwordlist
    word = random.choice(words)
    if random.randint(0, 2) == 0:
        chance = random.randint(0, 100)
        if "o" in word and random.randint(0, 100) > chance:
            word = word.replace("o", "0")
        if "i" in word and random.randint(0, 100) > chance:
            word = word.replace("i", "1")
        if "e" in word and random.randint(0, 100) > chance:
            word = word.replace("e", "3")
        if "s" in word and random.randint(0, 100) > chance:
            s = ["5", "$"]
            word = word.replace("s", random.choice(s))
        if "a" in word and random.randint(0, 100) > chance:
            a = ["@", "4"]
            word.replace("a", random.choice(a))
        if "b" in word and random.randint(0, 100) > chance:
            word = word.replace("b", "8")
        pass
    if random.randint(0, 2) == 0:
        word = word.upper()
    if random.randint(0, 6) == 0:
        i = 0
        a = list(word)
        l = []
        for w in a:
            if i:
                l.append(w.upper())
            else:
                l.append(w)
            i = int(not i)
        word = "".join(l)
    passwordlist.append(word)


def addnumber():
    global passwordlist
    num = "0"
    chance = random.randint(0, 100)
    if random.randint(0, 100) > chance:
        now = datetime.now()
        num = random.randint(1950, now.year)
    elif random.randint(0, 100) > chance:
        ns = []
        n = random.randint(0, 9)
        c = 0
        while c < 10:
            ns.append(str(n))
            c += random.randint(1, 10)
        num = "".join(ns)
    else:
        num = random.randint(0, 999)
    passwordlist.append(str(num))


def addxchar():
    global passwordlist
    chars = ["/", "&", "$", "@", "#", "=", "!", "?", "%", "*", "+", "-", "~", ">", "<", "(", ")", "_", " "]
    char = ""
    if random.randint(0, 1) == 0:
        ns = []
        n = str(random.choice(chars))
        c = 0
        while c < 9:
            ns.append(n)
            c += random.randint(1, 10)
        char = "".join(ns)

    else:
        char = random.choice(chars)
    passwordlist.append(char)


password = ""
add = ["addword()", "addword()", "addnumber()", "addxchar()"]

while len(password) < random.randint(20, 45):
    exec(random.choice(add))
    password = "".join(passwordlist)
print("Your strong memorable password is:")
print("")
print(password)
print("")
print("Enter domain you want password for")
x=input()
print("")
f= open("pass.txt","a")
f.write(x+"   "+password+"\n")
