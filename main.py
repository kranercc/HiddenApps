import psutil
import socket
from time import sleep
import colored
from getpass import getuser


myUsername = getuser()

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

    times = 0
    print(colored.fg("blue"))
    for proc in suspectedProcs:
        if proc.name() == process:
            print("Process run by user: " + proc.username() + " on PID: " + str(proc.pid))
            print("Command that was used to run: " + str(proc.cmdline()))
            print("Cpu usage: " + str(proc.cpu_percent()) + "%\n")
            times += 1

    print(colored.fg("red"))
    print("Occurences: " + str(times))
    print(colored.fg("white"))


def runFromCPP():
    processesPID = []
    toReturn = ""

    for p2 in suspectedProcs:
        processesPID.append(p2.name() + " " + str(p2.pid))
    
    for stringToReturn in processesPID:
        toReturn += stringToReturn + ","
    
    print(toReturn)
    
    
    

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
            answer = input("\n1. Get more info about\n2. Kill\nAnswer: ")

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

            sleep(60)
            print('\033c')


#mainLogic()
runFromCPP()
