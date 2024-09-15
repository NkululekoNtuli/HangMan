def body_parts ():
    head = "O"
    torso = "|"
    left_arm = "/"
    right_arm = "\\"
    return(head, torso, left_arm, right_arm)

secret_word = input("Enter playing word: ")
secret_word_caps = secret_word.upper()
print("Welcome players, Do Not Let The Man Hang!!")
word_len = len(secret_word)
print("The word has ", word_len,"letters")

attempt = 0
while attempt < 6:
    guess = input("Guess a letter: ")
    guess_caps = guess.upper()
    if guess_caps in secret_word_caps:
        print("Correct! \nThere is", secret_word.count(guess), guess_caps,"in the word" )
        secret_word_caps = secret_word_caps.replace(guess_caps,"")
        attempt -= 1
    elif attempt == 0:
        print("Incorrect!")
        head, torso, left_arm, right_arm = body_parts()
        print("     ",head)
    elif attempt == 1:
        print("Incorrect!")
        head, torso, left_arm, right_arm = body_parts()
        print("     ",head,"\n    ",left_arm)
    elif attempt == 2:
        print("Incorrect!")
        head, torso, left_arm, right_arm = body_parts()
        print("     ",head,"\n   ",left_arm,torso,)
    elif attempt == 3:
        print("Incorrect!")
        head, torso, left_arm, right_arm = body_parts()
        print("     ",head,"\n   ",left_arm,torso,right_arm)
    elif attempt == 4:
        print("Incorrect!")
        head, torso, left_arm, right_arm = body_parts()
        print("     ",head,"\n   ",left_arm,torso,right_arm,"\n    ",left_arm)
        #Uses left arm because its the same as the left leg
    elif attempt == 5:
        print("Incorrect!")
        head, torso, left_arm, right_arm = body_parts()
        print("     ",head,"\n   ",left_arm,torso,right_arm,"\n    ",left_arm,right_arm)
        #Uses right arm because its the same as the right leg
    attempt += 1