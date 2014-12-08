userName = ""
guess = ""
while userName=="":
    userName = input("What is your name?")
print("Good morning "+ userName)

password = "yes"
while guess!=password:
    guess = input("What is the password?")
