SMB1 = ['Goomba', 'Mario', 'Luigi', 'Koopa', 'Peach', 'Bowser', 'Spiny']
SMB2 = ['Mario', 'Luigi', 'Toad', 'Peach', 'Birdo']
SMB3 = ['Mario', 'Luigi', 'Bowser', 'Thwomp', 'Goomba', 'Buzzy Beetle', 'Dry Bones', 'Lakitu', 'Hammer Bro']
SMW = ['Mario', 'Luigi', 'Yoshi', 'Peach', 'Thwomp', 'Goombrat', 'Cheep Cheep', 'Koopa']
SM64 = ['Mario', 'Peach', 'Pokey', 'Bob-omb', 'Spiny', 'Chain Chomp', 'Goomba']
NSMB = ['Mario', 'Luigi', 'Toad', 'Yoshi', 'Peach', 'Bowser Jr.', 'Bowser']
SM3D = ['Mario', 'Luigi', 'Toad', 'Peach', 'Rosalina', 'Luma', 'Meowser', 'Big Boo', 'Goomba', 'Stingby']

gameRecommendation = []
gameRecommend = ''

chrRecommendation = []
chrTemp = ''
chrRecommend = ''

searchType = ''
search = ''
programQuery = ''
hits = 0

def delTemp():
    '''Used only for wiping temp variables, 
    not the actual function :)'''
    gameRecommend = ''
    chrTemp = ''
    chrRecommend = ''
    searchType = ''
    search = '' 
    programQuery = ''
    hits = 0

def marioSearch():
    searchDone = False
    programDone = False
    

    print('Welcome to Mario Bros search!')
    while (programDone != True):
        searchType = input('Please input either "character" or "game" to choose what you would like to search for: ')
        if searchType == 'game':
            while (searchDone != True):

                search = input('Please choose what game you want (abbrevated): ')
                if search == 'SMB1':
                    for string in SMB1:
                        print (string)
                    searchDone = True

                elif search == 'SMB2':
                    for string in SMB2:
                        print (string)
                    searchDone = True

                elif search == 'SMB3':
                    for string in SMB3:
                        print (string)
                    searchDone = True

                elif search == 'SMW':
                    for string in SMW:
                        print (string)
                    searchDone = True

                elif search == 'SM64':
                    for string in SM64:
                        print (string)
                    searchDone = True

                elif search == 'NSMB':
                    for string in NSMB:
                        print (string)
                    searchDone = True

                elif search == 'SM3D':
                    for string in SM3D:
                        print (string)
                    searchDone = True

                else:
                    gameReccomend = input ('Sorry, that is not a valid game. Would you like to submit one? Y/N')
                    if gameRecommend == 'Y':
                        gameRecommendation += input ('Please input what game should be added (abbreveation): ')
                        print ('Your game recommendation has been added!')
                        delTemp()
                        searchDone == True
                    elif gameRecommend == 'N':
                        print ('Ok!')
                        delTemp()

        if searchType == 'character':
            while (searchDone != True):
                search = input ('Please enter a character name: ')

                for string in SMB1:
                    if search in SMB1:
                        print (string + ' - SMB1')
                        hits += 1
                for string in SMB2:
                    if search in SMB2:
                        print (string + ' - SMB2')
                        hits += 1
                for string in SMB3:
                    if search in SMB3:
                        print (string + ' - SMB3') 
                        hits += 1 
                for string in SMW:
                    if search in SMW:
                        print (string + ' - SMW')
                        hits += 1
                for string in SM64:
                    if search in SM64:
                        print (string + ' - SM64')
                        hits += 1
                for string in NSMB:
                    if search in NSMB:
                        print (string + ' - NSMB')
                        hits += 1
                for string in SM3D:
                    if search in SM3D:
                        print (string + ' - SM3D')
                        hits += 1

                if hits == 0:
                    chrRecommend = input ('Your search came out with no hits. Would you like to suggest a character? Y/N')
                    if chrReccomend == 'Y':
                        chrTemp += input ('Please input a character: ')
                        chrTemp += ' -' + input ('What game are they from?: ')
                        chrRecommendation += chrTemp
                        print ('Thank you!')
                        delTemp()
                        searchDone = True
                    elif chrRecommend == 'N':
                        print ('Ok!')
                        delTemp()

                elif hits == 1:
                    print ('Your search came out with', hits, 'hit')
                    delTemp()
                    searchDone = True
                    
                else:
                    print ('Your search came out with', hits, 'hits')
                    delTemp()
                    searchDone = True

        programQuery = input ('Would you like to do another search? Y/N')
        if programQuery == 'N':
            print ('Ok, have a nice day :)')
            delTemp()
            programDone = True

        elif programQuery == 'Y':
            print ('Taking you back...')
            delTemp()