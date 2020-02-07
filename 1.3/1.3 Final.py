# region lists
SMB1 = ['Goomba', 'Mario', 'Luigi', 'Koopa', 'Peach', 'Bowser', 'Spiny']
SMB2 = ['Mario', 'Luigi', 'Toad', 'Peach', 'Birdo']
SMB3 = ['Mario', 'Luigi', 'Bowser', 'Thwomp', 'Goomba', 'Buzzy Beetle', 'Dry Bones', 'Lakitu', 'Hammer Bro']
SMW = ['Mario', 'Luigi', 'Yoshi', 'Peach', 'Thwomp', 'Goombrat', 'Cheep Cheep', 'Koopa']
SM64 = ['Mario', 'Peach', 'Pokey', 'Bob-omb', 'Spiny', 'Chain Chomp', 'Goomba']
NSMB = ['Mario', 'Luigi', 'Toad', 'Yoshi', 'Peach', 'Bowser Jr.', 'Bowser']
SM3D = ['Mario', 'Luigi', 'Toad', 'Peach', 'Rosalina', 'Luma', 'Meowser', 'Big Boo', 'Goomba', 'Stingby']
# endregion


def marioSearch():
    '''Search through all of your favorite Super Mario Bros characters and what games they were from!
       If I missed anyone/any game, make sure to suggest them using the suggestion feature!'''

    # ! To anyone running, make sure that you're running this through Python 3, or it will not work !

    # region variables
    # Region and end are only for vscode code folding
    searchDone = False
    # programDone = False
    hits = 0
    gameRecommendation = []
    gameRecommend = ''

    chrRecommendation = []
    chrTemp = ''
    chrRecommend = ''

    searchType = ''
    search = ''
    programQuery = ''
    # endregion

    print('Welcome to Mario Bros search!')
    while (searchDone != True):
        searchType = (input('Please enter either "Character" or "Game" to choose what you would like to search for. To cancel, type "Cancel": ')).title()
        if searchType == 'Game':
            while (searchDone != True):

                search = (input('Please choose what game you want (abbrevated): ')).upper()
                # region if-else for game
                
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
                # endregion
                else:
                    while (searchDone != True):
                        gameRecommend = input('Sorry, that is not a valid game. Would you like to submit this one? Y/N: ')
                        if gameRecommend.upper() in ['Y', 'YES']:
                            gameRecommendation.append(search.title())
                            print (gameRecommendation)
                            print ('Your game recommendation has been added!')
                            searchDone = True
                        elif gameRecommend.upper() in ['N', 'NO']:
                            print ('Ok, no problem.')
                            searchDone = True
                        else:
                            print ('That is not a valid option, please try again.')
                        
        elif searchType == 'Character':
            while (searchDone != True):
                # region for loops for character
                search = (input('Please enter a character name: ')).title()
                for string in SMB1:
                    if search == string:
                        print (string + ' - SMB1')
                        hits += 1
                for string in SMB2:
                    if search == string:
                        print (string + ' - SMB2')
                        hits += 1
                for string in SMB3:
                    if search == string:
                        print (string + ' - SMB3') 
                        hits += 1 
                for string in SMW:
                    if search == string:
                        print (string + ' - SMW')
                        hits += 1
                for string in SM64:
                    if search == string:
                        print (string + ' - SM64')
                        hits += 1
                for string in NSMB:
                    if search == string:
                        print (string + ' - NSMB')
                        hits += 1
                for string in SM3D:
                    if search == string:
                        print (string + ' - SM3D')
                        hits += 1
                # endregion 
                
                if hits == 0:
                    while (searchDone != True):
                        chrRecommend = input ('Your search came out with no hits. Would you like to suggest a character? Y/N: ')
                        if chrRecommend.upper() in ['Y', 'YES']:
                            chrTemp += search + ' - ' + (input('What game are they from?: ')).upper()
                            chrRecommendation.append(chrTemp)
                            print (chrRecommendation)
                            print ('Thank you!')
                            searchDone = True

                        elif chrRecommend.upper() in ['N', 'NO']:
                            print ('Ok!')
                            searchDone = True

                        else:
                            print ('Sorry, that is not a valid option')

                elif hits == 1:
                    print ('Your search came out with', 1, 'hit')
                    searchDone = True
                    
                else:
                    print ('Your search came out with', hits, 'hits')
                    searchDone = True
                    
        elif searchType == 'Cancel':
            print ('Ok, sorry about that!')
            searchDone = True            
        elif (searchDone != True):
            print ('That input was not recognized, please try again')  

    print ('Have a nice day :)')

marioSearch()
