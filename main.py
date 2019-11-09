import psutil
import socket
from time import sleep
import colored


myUsername = socket.gethostname()

myProcsNames = []
myProcs = []

suspectedProcs = []


for p in psutil.process_iter():
    if p.username() == myUsername:
        myProcsNames.append(p.name())
        myProcs.append(p)





for pN in range(len(myProcsNames)):
    numberOfAppearences = myProcsNames.count(myProcsNames[pN])
    if numberOfAppearences > 1:
        suspectedProcs.append(myProcs[pN])


procsToIter = []

for sP in suspectedProcs:
    procsToIter.append(sP.name())

procsToIter = list(dict.fromkeys(procsToIter))


def getInfo(process):
    pass

def mainLogic():
    endProgram = False
    perline = 0
    while not endProgram:

            for p in range(len(procsToIter)):
                print(colored.fg("purple_1b"), end="")

                print(str(p+1)+ ". " + procsToIter[p] + "\t", end="" )
                perline += 1
                if perline == 3:
                    print("\n")
                    perline = 0


            print(colored.fg("white"))
            answer = input("\n1. Get more info about\n2. Kill ")

            if answer == "2" or answer == "kill" or answer == "Kill":
                killWho = input("Who: ")
                for proc in suspectedProcs:
                    if proc.name() == killWho:
                        proc.kill()
                        print("Succesfully killed")
                        sleep(1)

            if answer == "1":
                infoWho = input("Who: ")
                getInfo(infoWho)

            if procsToIter[p] == procsToIter[-1]:
                endProgram = True

            print('\033c')


mainLogic()