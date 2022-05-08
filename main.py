from ourPackages import *

B = FC()
D = updateDatabase()
if D.checkUpdate():
    D.update()
    exit()
while 1:
    cls()
    print(Fore.BLACK + Back.GREEN + "==============================================")
    print(Fore.GREEN + '''               H4CK3R5 F4C3 D3T3C7!0N              ''')
    print(Fore.BLACK + Back.GREEN + "==============================================")
    print(Fore.WHITE + "How can we Help you .. ?")
    print(Fore.YELLOW + '''Face Detection from  1) Image  2) Web Cam 3) Exit''')
    C = int(input("Please Choose the one Option : "))
    if C == 1:
        D = os.listdir("testData")
        L = []
        N_L = []
        for img in D:
            L.append(img)
            N_L.append(os.path.splitext(img)[0])
        for i in range(len(N_L)):
            print(i+1, ")", N_L[i])
        C1 = int(input("Please Choose the Image You want ..  : "))
        Img = cv.imread(f'testData/{L[C1-1]}')
        animate()
        B.image_find(Img)
    elif C == 2:
        B.start_rec(0)
    elif C == 3:
        break
    else:
        print("Please Choose Correct option ... ")
    time.sleep(2)
