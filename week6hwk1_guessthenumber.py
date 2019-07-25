import random


increase = []
increase.sort()

decrease  = []
decrease.sort()



print("""0 ile 100 araliginda bir sayi tutunuz.
Tuttugunuz sayiyi bilmeye calisacagim. Eger tuttugunuz sayi tahminimden
asagidaysa '-'ye, yukaridaysa '+'ya basarak bana yardimci olun. """ )

#Program calismiyor

a = 1

while a ==1:

    b = random.randint(0, 100)

    print(b)

    c = input("- ya da +")

    if c == "-":
        decrease += [b]
        decrease.sort()

        d = random.randint(0, decrease[1])

        print(d)
        
        c = input("- ya da +")
        
        if c == "-":
            
            decrease += [d]
            decrease.sort()

            e= random.randint( increase[-1], decrease[1])
            print(e)
            c = input("- ya da +")
           # if..............
            
        else:
            increase += [d]
            increase.sort()
            
            e= random.randint(decrease[1], 100)
            print(e)
            c = input("- ya da +")
            #if........

        
    else:
        increase += [b]
        increase.sort()

        d= random.randint(increase[-1],100)

        print(d)
        c = input("- ya da +")

        if c == "-":
            
            decrease += [d]
            decrease.sort()

            e= random.randint( increase[-1], decrease[1])
            print(e)
            c = input("- ya da +")
           # if..............
            
        else:
            increase += [d]
            increase.sort()
            
            e= random.randint(increase[-1], 100)
            print(e)
            c = input("- ya da +")
            #if........    

































#            print("Tuttugun sayi", c, "mi?")
#            yonlendirme = input("- ya da +")
#            if yonlendirme == "+" :
#                fazlalar += [c]
#                fazlalar.sort()
#                while True:
#                    if yonlendirme == "+":    
#                        c=random.randint(fazlalar[1], azlar[-1])
#                        print("Tuttugun sayi", c, "mi?")
#                        yonlendirme = input("- ya da +")
#                        fazlalar.sort()
#                        azlar.sort()
#                    else:
#                        c=random.randint(fazlalar[-1], azlar[1])
#                        print("Tuttugun sayi", c, "mi?")
#                        yonlendirme = input("- ya da +")
#                        fazlalar.sort()
#                        azlar.sort()
                        
#            else:
#                azlar += [c]
#                fazlalar.sort()
#                azlar.sort()
#else :
#    ikinci_eleme = input("Tuttugunuz sayi 75 mi?")
#    if ikinci_eleme == "+" :
#        while True:
#            d=random.randint(75, 100)
#            print("Tuttugun sayi", d, "mi?")
#            yonlendirme = input("- ya da +")
#            if yonlendirme == "+" :
#                fazlalar += [d]
#                fazlalar.sort()
#                azlar.sort()
#                
#                while True:
#                    if yonlendirme == "+":    
#                        d=random.randint(fazlalar[-1], azlar[1])
#                        print("Tuttugun sayi", d, "mi?")
#                        yonlendirme = input("- ya da +")
#                        fazlalar.sort()
#                        azlar.sort()
#                    else:
#                        d=random.randint(fazlalar[-1], azlar[1])
#                        print("Tuttugun sayi", d, "mi?")
#                        yonlendirme = input("- ya da +")
#                        fazlalar.sort()
#                        azlar.sort()
#                
#            else:
#                azlar += [d]
#                fazlalar.sort()
#                azlar.sort()
       #
