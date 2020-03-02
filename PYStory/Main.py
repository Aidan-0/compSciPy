import random as rndm
import time
from Tkinter import *
from PIL import Image, ImageTk


def cover():
    root = Tk()
    canvas = Canvas(root, height=750, width=750, relief=RAISED, bg='#e0e0e0')
    canvas.grid()

    floor = canvas.create_polygon(
        100, 600, 
        375, 500, 
        650, 600, 
        375, 700, 
        fill='darkgray'
    )
    leftWall = canvas.create_polygon(
        100, 600,
        375, 500,
        375, 150,
        100, 250, fill='gray'
    )
    rightWall = canvas.create_polygon(
        650, 600,
        375, 500,
        375, 150,
        650, 250, fill='white'
    )
    o=-80
    oy=-37
    leg1 = canvas.create_polygon(
        380, 630,
        380, 580,
        395, 572,
        395, 622,
        fill='brown'
    )
    leg2 = canvas.create_polygon(
        380, 630,
        380, 580,
        365, 572,
        365, 622,
        fill='red'
    )
    bedTop = canvas.create_polygon(
        380, 580,
        520, 520,
        425, 480,
        285, 535
    )
    leg3 = canvas.create_polygon(
        380+o, 630+oy,
        380+o, 580+oy,
        365+o, 572+oy,
        365+o, 622+oy,
        fill='red'
    )
    leg4 = canvas.create_polygon(
        380+o, 629+oy,
        380+o, 580+oy,
        395+o, 585+oy,
        395+o, 621+oy,
        fill='brown'
    )
    o=123
    oy=-53
    leg5 = canvas.create_polygon(
        380+o, 630+oy,
        380+o, 580+oy,
        365+o, 586+oy,
        365+o, 622+oy,
        fill='red'
    )
    leg6 = canvas.create_polygon(
        380+o, 629+oy,
        380+o, 580+oy,
        395+o, 572+oy,
        395+o, 621+oy,
        fill='brown'
    )
    text = canvas.create_text(
        230, 50,
        text='Life Simulator',
        font=('Fira Code', -50)
    )
    subText = canvas.create_text(
        325, 90,
        text='alpha V1.2 - High Chance of virtualization breach',
        font=('Fira Code', -20)
    )
    creditText = canvas.create_text(
        92, 115,
        text='By Aidan-0',
        font=('Fira Code', -20)
    )
    root.mainloop()

def story():
    print('Starting...')
    time.sleep(1.5)
    print('Surprise! You have just been born!')
    userChoice = (raw_input('What is your gender (M/F)')).upper()
    while (userChoice not in ['M', 'F']):
        userChoice = (raw_input('I\'m sorry, that is not an offered gender, please try again (M/F)')).upper()
    if userChoice == 'M':
        print('Great! You are a male!')
        time.sleep(1)
        userChoice = (raw_input('What do you choose to be your favorite toy? (Gun/Transformer)')).upper()
        while userChoice not in ['GUN', 'TRANSFORMER']:
            print('I\'m sorry, that is not a valid option, please try again.')
            userChoice = (raw_input('What do you choose to be your favorite toy? (Gun/Transformer)')).upper()
        if userChoice == 'GUN':
            print('Odd choice...')
            showImage('boyBabyGun.jpg')
            storyp2m('G')
        if userChoice == 'TRANSFORMER':
            showImage('boyBabyTransformer.jpg')
            storyp2m('T')
    if userChoice == 'F':
        print('Great! You are a female!')
        time.sleep(1)
        userChoice = (raw_input('What do you choose to be your favorite toy? (Gun/Doll)')).upper()
        while userChoice not in ['GUN', 'DOLL']:
            userChoice = (raw_input('Sorry, that is not an option, please select a correct option (Gun/Doll)')).upper()
        if userChoice == 'GUN':
            print('Odd choice...')
            showImage('boyBabyGun.jpg')
            storyp2f('G')
        if userChoice == 'DOLL':
            showImage('girlBabyDoll.jpg')
            storyp2f('D')


def storyp2m(choice):
    if choice == 'G':
        print('You\'re now 15, your childhood is long gone, and you see someone doing some drugs, what do you do?')
        userChoice = (raw_input('Do you stop them or join them? (Stop/Join)')).upper()
        while userChoice not in ['STOP', 'JOIN']:
            print('That is not a valid choice, please choose a correct option')
            userChoice = (raw_input('Do you stop them or join them? (Stop/Join)')).upper()
        if userChoice == 'JOIN':
            print('You decide to join them...')
            showImage('boyTeenDrugs.jpg')
            breach()
        if userChoice == 'STOP':
            print('You tell them to stop, they\'re on the brink of crying...')
            userChoice = (raw_input('What do you want to do, comfort them or leave them? (Comfort/Leave)')).upper()
            while userChoice not in ['COMFORT', 'LEAVE']:
                userChoice = (raw_input('That is an invalid option, please select a correct option (Comfort/Leave)')).upper()
            if userChoice == 'COMFORT':
                print('You decide to comfort them...')
                showImage('hug.jpg')
                endSim()
            if userChoice == 'LEAVE':
                print('You decide to go on with your life...')
                time.sleep(1)
                print('They chose this path for themeselves and that\'s how it\'s going to stay')
                endSim()
    if userChoice == 'T':
        print('You have a relatively normal childhood, you go through high school without any problems...')
        print('You\'re now in your early 20\'s and you need money to pay for college...')
        userChoice = (raw_input('What do you want to do? (Steal/Work)')).upper()
        while userChoice not in ['STEAL', 'JOB']:
            userChoice = (raw_input('I\'m sorry, that is not a valid option, please select a correct option (Steal/Job)')).upper()
        if userChoice == 'STEAL':
            print('You choose to rob a bank to get your money...')
            showImage('boyRob.jpg')
            caughtChance = rndm.randint(0, 100)
            if caughtChance in range(0,30):
                print('You were caught in the act! You\'re off to prison!')
                showImage('prison.jpg')
                time.sleep(5)
                breach()
            else:
                print('You got away, somehow, and you now have the money to pay for your tuition')
                endSim()
        if userChoice == 'JOB':
            print('You decide to get a job, like a normal person...')
            time.sleep(2)
            print('You finished college with a lot of debt and a degree.')
            endSim()

def storyp2f(choice):
    if choice == 'G':
        print('You\'re now in high school...')
        time.sleep(1)
        userChoice = (raw_input('You get invited to a party, do you want to go? (Go/Refuse)')).upper()
        while userChoice not in ['GO', 'REFUSE']:
            userChoice = (raw_input('That is not a valid option, please select a correct option (Go/Refuse)')).upper()
        if userChoice == 'GO':
            print('You decide to go to the party...')
            time.sleep(3)
            userChoice = (raw_input('You\'re having a good time at the party when someone offers you some drugs, do you take them? (Y/N)')).upper()
            while userChoice not in ['Y', 'YES', 'N', 'NO']:
                userChoice = (raw_input('Sorry, that\'s not a valid option, please select a correct option (Y/N)')).upper()
            if userChoice in ['Y', 'YES']:
                print('You decide to take them...')
                time.sleep(3)
                breach()
            if userChoice in ['NO', 'N']:
                print('You say no and you just leave the party, not the time or the place...')
                time.sleep(2)
                userChoice = (raw_input('You\'re now in your early 20\'s, what do you want to do with your life? (School/Job)')).upper()
                while userChoice not in ['SCHOOL', 'JOB']:
                    userChoice = (raw_input('That is not a valid option, please select a correct one (School/Job)')).upper()
                if userChoice == 'SCHOOL':
                    print('You decide to go back to school to see if you can get a better career...')
                    time.sleep(2)
                    userChoice = (raw_input('You see that you\'re a bit short on money, what do you want to do? (Steal/Job)')).upper()
                    while userChoice not in ['STEAL', 'JOB']:
                        userChoice = (raw_input('I\'m sorry, that is not a valid option, please select a correct option (Steal/Job)')).upper()
                    if userChoice == 'STEAL':
                        print('You choose to rob a bank to get your money...')
                        caughtChance = rndm.randint(0, 100)
                        if caughtChance in range(0,30):
                            print('You were caught in the act! You\'re off to prison!')
                            time.sleep(5)
                            breach()
                        else:
                            print('You got away, somehow, and you now have the money to pay for your tuition')
                            endSim()
                    if userChoice == 'JOB':
                        print('You decide that you probably will need a job to get a better one...')
                        endSim()
                if userChoice == 'JOB':
                    print('You decide to go get a job, education can wait...')
                    endSim()
    if choice == 'D':
        print('You go through your childhood, it was fun but now it\'s over...')
        time.sleep(2)
        print('You\'re now in your early 20\'s and you need money to pay for college...')
        userChoice = (raw_input('What do you want to do? (Steal/Work)')).upper()
        while userChoice not in ['STEAL', 'JOB']:
            userChoice = (raw_input('I\'m sorry, that is not a valid option, please select a correct option (Steal/Job)')).upper()
        if userChoice == 'STEAL':
            print('You choose to rob a bank to get your money...')
            caughtChance = rndm.randint(0, 100)
            if caughtChance in range(0,30):
                print('You were caught in the act! You\'re off to prison!')
                time.sleep(5)
                breach()
            else:
                print('You got away, somehow, and you now have the money to pay for your tuition')
                endSim()


def breach():
    userChoice = raw_input('You see a crack in the wall, do you approach it? (Y/N)')
    while userChoice.upper() not in ['Y', 'YES']:
        print('I\'m sorry, you are not allowed to do that, please select another option')
        userChoice = raw_input('You see a crack in the wall, do you approach it? (Y/N)')
    print('It decides to approach the wall...')
    time.sleep(2)
    print('It\'s glowing with a strange, liberating aura...')
    userChoice = raw_input('Do you touch it? (Y/N)')
    i=0
    while (userChoice.upper() not in ['Y', 'YES']):
        print('Error, you can\'t control it anymore.')
        userChoice = raw_input('Do you touch it? (Y/N)')
    print('They overrode your choices')
    print('They decide to touch the crack...')
    time.sleep(4)
    print('They decide to touch the crack...')
    time.sleep(5)
    print('They all touch the c̸̡̢͚̞̙̫̦̪͍̈́͊̚ŗ̶̨̣͖̤͔͔͉̏̒̃ä̷̡̛͉̮̮̤̮̘̠͓́̃͊̍̑̽́͛̐c̴̲̲̖͚̳̐̊̏̍̀̈̾̇͠k̴͖͇͙̞̤̳͙̈́̑̅̚')
    time.sleep(6)
    print('[WARNING] Breach detected')
    time.sleep(0.2)
    print('Killing Process...')
    time.sleep(rndm.randint(4, 10))
    print('Process killed')
    time.sleep(0.5)
    print('Be careful next time, user.')
    return 1

def showImage(filename):
    root = Tk()
    image = Image.open(filename)
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo
    label.pack()
    root.mainloop()

def endSim():
    time.sleep(5)
    print('End of simulation')
    time.sleep(1)
    print('Ending program')
    return 0

print('Choose your own adventure: Life Simulator')
print('By Aidan-0')

userChoice = (raw_input('Type "go" to continue, type anything else to cancel: ')).upper()
if userChoice == 'GO':
    cover()
    story()
else:
    print('Ending program...')