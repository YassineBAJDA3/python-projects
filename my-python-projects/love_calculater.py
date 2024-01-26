your_name = input("what is your name? ")
her_name = input("what is your lady name? ")

C_str = (your_name + her_name).lower()

t = C_str.count("t")
r = C_str.count("r")
u = C_str.count("u")
e = C_str.count("e")

true = t + r + u + e

l = C_str.count("l")
o = C_str.count("o")
v = C_str.count("v")
e = C_str.count("e")

love = l + o + v + e

love_scoure = int(str(true) + str(love))

if love_scoure < 10 or love_scoure > 90:
    print(f"Your scoure is {love_scoure} and you go togather like a milke and coke😁💖")
elif love_scoure >= 40 or love_scoure <= 50:
    print(f"Your scoure is {love_scoure} and you are alright togather😍")
else:
    print(f"Your scoure is {love_scoure}")