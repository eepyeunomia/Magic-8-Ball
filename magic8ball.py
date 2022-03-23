title = '''

    __  __                        __                 ____         ___             __  __ 
   F  \/  ]     ___ _     ___ _   LJ    ____        F __ J       F _ ",   ___ _   LJ  LJ 
  J |\__/| L   F __` L   F __` L       F ___J.     J `--' L     J `-'(|  F __` L  FJ  FJ 
  | |`--'| |  | |--| |  | |--| |  FJ  | |---LJ     / ,--. \     | ,--.\ | |--| | J  LJ  L
  F L    J J  F L__J J  F L__J J J  L F L___--.    F L__J J     F L__J \F L__J J J  LJ  L
 J__L    J__LJ\____,__L )-____  LJ__LJ\______/F   J\______/L   J_______J\____,__LJ__LJ__L
 |__L    J__| J____,__FJ\______/F|__| J______F     J______F    |_______FJ____,__F|__||__|
                        J______F                                                         
'''
ball = '''
        ____
    ,dP9CGG88@b,
  ,IP  _   Y888@@b,
 dIi  (_)   G8888@b
dCII  (_)   G8888@@b
GCCIi     ,GG8888@@@
GGCCCCCCCGGG88888@@@
GGGGCCCGGGG88888@@@@...
Y8GGGGGG8888888@@@@P.....
 Y88888888888@@@@@P......
 `Y8888888@@@@@@@P'......
    `@@@@@@@@@P'.......
        """"........
'''


def magicBall():
    responses = ["It is certain.", 
    "It is decidedly so.", 
    "Without a doubt.", 
    "Yes definitely.", 
    "You may rely on it.", 
    " As I see it, yes.", 
    "Most likely.", 
    "Outlook good.", 
    "Yes.", 
    "Signs point to yes.", 
    "Reply hazy, try again.", 
    "Ask again later.", 
    "Better not tell you now.", 
    "Cannot predict now.", 
    "Concentrate and ask again.", 
    "Don't count on it.", 
    "My reply is no.", 
    "My sources say no.", 
    "Outlook not so good.", 
    "Very doubtful."]
    
    question = input("What do you want to ask the Magic 8 Ball? ")
    if question == str(cmd):
        print(random.choice(responses))
        again = input("Run Again? ")
        if again == "yes":
            magicBall()
        else:
            main()
    else:
        print(random.choice(responses))
        again2 = input("Run Again? ")
        if again2 == "yes":
            magicBall()
        else:
            main()


def main():
    print(title)
    print(ball)
    magicBall()


main()
