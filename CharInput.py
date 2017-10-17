#PyChallenge - Character Input
user_name = input("What's your name?\n")
ask_age = int(input("How old are you?\n"))
user_age = 100 - ask_age

imosGreeting = "It's a pleasure to meet you, %s! You are going to be 100 years old in %s years.\n" % (user_name, user_age)
repeat_xtimes = int(input("Pick a numer!"))

print(imosGreeting * repeat_xtimes)
