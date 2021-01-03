import math

from Asmantak.PSO import *


class UI:
    def __init__(self, fileIn, fileTest):
        self.fileIn = fileIn
        self.fileTest = fileTest

    def printCommands(self):
        print("1: Particle Swarm | Evolutive Metohd")
        print("0: Exit")

    def getFromFileInput(self):
        l = []
        with open(self.fileIn, "r") as filestream:
            for line in filestream:
                li = []
                currentline = line.split(",")
                for j in range(7):
                    li.append(int(currentline[j + 1]))
                l.append(li)
        return l

    def getFromFileOut(self):
        l = []
        with open(self.fileIn, "r") as filestream:
            for line in filestream:
                li = []
                currentline = line.split(",")
                for j in range(8, 11):
                    li.append(float(currentline[j]))
                l.append(li)
        return l

    def getFromFileTest(self):
        l = []
        with open(self.fileTest, "r") as filestream:
            for line in filestream:
                li = []
                currentline = line.split(",")
                for j in range(7):
                    li.append(float(currentline[j + 1]))
                l.append(li)
        return l

    def getOutFromFileTest(self):
        l = []
        with open(self.fileTest, "r") as filestream:
            for line in filestream:
                li = []
                currentline = line.split(",")
                for j in range(8, 11):
                    li.append(float(currentline[j]))
                l.append(li)
        return l

    # first out
    def getStreamOut1(self):
        l = self.getFromFileOut()
        stream1 = []
        for x in l:
            stream1.append([x[0]])
        return stream1

    # second out
    def getStreamOut2(self):
        l = self.getFromFileOut()
        stream1 = []
        for x in l:
            stream1.append([x[1]])
        return stream1

    # third out
    def getStreamOut3(self):
        l = self.getFromFileOut()
        stream1 = []
        for x in l:
            stream1.append([x[2]])
        return stream1

    # we run our method here
    def checkAcc(self, found, real):
        if (math.fabs(math.floor(found) - math.floor(real)) <= 3):
            return True
        return False

    def runMethod3(self):
        new_in = self.getFromFileTest()
        new_out = self.getOutFromFileTest()
        acc = 0
        slumpAcc = 0
        flowAcc = 0
        stAcc = 0
        predicitons = []
        for index in range(len(new_in)):
            p = []
            m1 = Method(self.getFromFileInput(), self.getStreamOut1())
            m2 = Method(self.getFromFileInput(), self.getStreamOut2())
            m3 = Method(self.getFromFileInput(), self.getStreamOut3())
            print("We wil introduse this new input: \n")
            print(new_in[index])
            res1 = m1.model([new_in[index]])
            res2 = m2.model([new_in[index]])
            res3 = m3.model([new_in[index]])
            print("Our prediction:\n")

            print("SLUMP(cm)")
            print(res1[0][0])
            print("Real result: ")
            print(new_out[index][0])
            p.append(res1[0][0])
            if (self.checkAcc(res1[0][0], new_out[index][0])):
                acc = acc + 1
            if (self.checkAcc(res1[0][0], new_out[index][0])):
                slumpAcc = slumpAcc + 1

            print("FLOW(cm)")
            print(res2[0][0])
            print("Real result: ")
            print(new_out[index][1])
            p.append(res2[0][0])
            if (self.checkAcc(res2[0][0], new_out[index][1])):
                acc = acc + 1
            if (self.checkAcc(res2[0][0], new_out[index][1])):
                flowAcc = flowAcc + 1

            print("Compressive Strength (28-day)(Mpa)")
            print(res3[0][0])
            print("Real result: ")
            print(new_out[index][2])
            p.append(res3[0][0])
            if (self.checkAcc(res3[0][0], new_out[index][2])):
                acc = acc + 1
            if (self.checkAcc(res3[0][0], new_out[index][2])):
                stAcc = stAcc + 1
            predicitons.append(p)
        print("Accuracy:", acc / (len(new_in) * 3))
        print("Slump Accuracy:", slumpAcc / len(new_in))
        print("Flow Accuracy:", flowAcc / len(new_in))
        print("Strength Accuracy:", stAcc / len(new_in))
        return predicitons

    def calculateEstimate(self, w, first, second, third):
        total = w[0] + w[1] + w[2]
        return (w[0] * first + w[1] * second + w[2] * third) / total

    def run(self):
        print("Welcome to our ML Algorithm for predicting Cement Size and Value given some real life data! \n")
        print("The entity has the atributes: ")
        print("Cement,Slag,Fly ash,Water,SP,Coarse Aggr,Fine Aggr.")
        print(
            "Base on this we will find a model that can deduce the: future SLUMP(cm),FLOW(cm),Compressive Strength (28-day)(Mpa)\n")
        while (True):
            self.printCommands()
            i = input('Enter command: ')
            if (i == '0'):
                print("Bye")
                break
            if (i == '1'):
                self.runMethod3()


