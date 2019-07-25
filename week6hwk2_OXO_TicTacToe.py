#ODEV 2: XOX Oyunu
#		Kitapta yer alan XOX oyunu iki kisinin karsilikli oynayabilecegi sekilde duzenlenmis. Sizden bu oyunu 
#		kullanicinin bilgisayara karsi oynayabilecegi versiyonunu yapmanizi istiyoruz. Ayrica gelistireceginiz 
#		algoritma sayesinde bilgisayarin tamamen rastgele hamleler yapmasindan ziyade mantikli hamleler yapmasini 
#		saglamanizi istiyoruz. Ornegin bilgisayarin "O" hamlesini yaptigini varsayalim: 
#					X O _  
#					_ X _   
#					_ _ _
#
#		seklinde olusan bir durumda hamle sirasi bilgisayarda ve bilgisayar kaybetmemek icin sag-alt koseye "O" 
#		koymalidir.


#		Farkli bir ihtimal:
#					O X X 
#					O _ X 
#					_ _ _ 
#
#		boyle bir durumda da hamle sirasi bilgisayarda ve bilgisayar kazanma hamlesi olarak sol-alt koseye "O" koyarak 
#		oyunu bitirmelidir.

#SAD BUT CALISMIYOR, bir yerde hata veriyor

import random


board = [["___", "___", "___"],
         ["___", "___", "___"],
         ["___", "___", "___"]]

#print(board)

print("\n"*15)

for i in board:
    print("\t".expandtabs(30), *i, end="\n"*2)

kazanma_olcutleri = [[[0, 0], [1, 0], [2, 0]],
                     [[0, 1], [1, 1], [2, 1]],
                     [[0, 2], [1, 2], [2, 2]],
                     [[0, 0], [0, 1], [0, 2]],
                     [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]],
                     [[0, 0], [1, 1], [2, 2]],
                     [[0, 2], [1, 1], [2, 0]]]

koseler = [[0,0], [0,2], [1,0], [1,2], [2,0], [2,2]]

ortalar = [[0,1], [1,0], [1,1], [1,2], [1,1]]


x_spots = []

o_spots = []

while True:        
                      
    #sira = 1


    #if sira % 2 == 0:
    #    isaret = "X".center(3)
    #else:
    #    isaret = "O".center(3)

    #sira += 1

    #print()
    #print("ISARET: {}\n".format(isaret))

    
    a = input("Select a spot from top to bottom [0,1,2]: ".ljust(30))
    if a == "q":
        break

    b = input("Select a spot from left to the right[0, 1, 2]: ".ljust(30))
    if b == "q":
        break


    print("\n"*15)

    if board[a][b] == "___":
        board[a][b] = isaret
        if isaret == "X".center(3): #X girilirse bu koordinatlari
            x_spots += [[a, b]]     #xin yerleri listesine ekle
        elif isaret == "O".center(3):#O girilince bu koordinatlari
            o_spots += [[a, b]]      #onun yerleri listesine ekle
       # sira += 1

       #Check for a winner after user inserts sth
        for i in kazanma_olcutleri:   #kazanma olcutlerindeki her bir ogeye i adini verelim
            o = [z for z in i if z in o_spots] #i icindeki o_spots'ta yer alan her bir ogeye de z adini verelim
                                           #ve bunlari o adinda bir listede toplayalim
            x = [z for z in i if z in x_spots]

        print("o: ", o)                   
        print("x: ", x)
        
        if len(o) == len(i):            #eger o adli listenin uzunlugu, i degiskeninin uzunlugu ile ayniysa
            print("O KAZANDI!")         #bu durumda O harfini oynayan kazanmistir. (bu ayni surec x icin de islemekte, aciklamalari yazmadik ama aynisi oluyor.)
            quit()

        if len(x) == len(i):
            print("X KAZANDI!")
            quit()


            
    else:
        print("\nSPOT IS ALREADY TAKEN!TRY AGAIN!\n")

    for i in board:                   #to show the last situation of the board to the user.  
        print("\t".expandtabs(30), *i, end = "\n"*2)


        while True:
            opponent = random.randint(koseler[0],koseler[-1])

            if board[opponent] != "o" and board[opponent] !='x':
                board[opponent] = 'o'
                break

        #Check for a winner (after comp inserts sth)
        for i in kazanma_olcutleri:   #kazanma olcutlerindeki her bir ogeye i adini verelim
            o = [z for z in i if z in o_spots] #i icindeki o_spots'ta yer alan her bir ogeye de z adini verelim
                                           #ve bunlari o adinda bir listede toplayalim
            x = [z for z in i if z in x_spots]

        print("o: ", o)                   
        print("x: ", x)
        
        if len(o) == len(i):            #eger o adli listenin uzunlugu, i degiskeninin uzunlugu ile ayniysa
            print("O KAZANDI!")         #bu durumda O harfini oynayan kazanmistir. (bu ayni surec x icin de islemekte, aciklamalari yazmadik ama aynisi oluyor.)
            quit()

        if len(x) == len(i):
            print("X KAZANDI!")
            quit()
        else:
            print("This spot is taken.")






    for i in kazanma_olcutleri:   #kazanma olcutlerindeki her bir ogeye i adini verelim
        o = [z for z in i if z in o_spots] #i icindeki o_spots'ta yer alan her bir ogeye de z adini verelim
                                           #ve bunlari o adinda bir listede toplayalim
        x = [z for z in i if z in x_spots]

        print("o: ", o)                   
        print("x: ", x)
        
        if len(o) == len(i):            #eger o adli listenin uzunlugu, i degiskeninin uzunlugu ile ayniysa
            print("O KAZANDI!")         #bu durumda O harfini oynayan kazanmistir. (bu ayni surec x icin de islemekte, aciklamalari yazmadik ama aynisi oluyor.)
            quit()

        if len(x) == len(i):
            print("X KAZANDI!")
            quit()

            































    














