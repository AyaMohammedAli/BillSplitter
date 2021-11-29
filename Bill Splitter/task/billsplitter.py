import random 
class BillSplitter:
    def __init__(self):
        self.size = 0
        self.freinds = {}
    
    def check_numberOfFreinds(self):
        print("Enter the number of friends joining (including you):")
        self.size = int(input())
        if self.size <=0:
            print("No one is joining for the party")
        else:
            print("Enter the name of every friend (including you), each on a new line:")
            for i in range(self.size):
                x = input()
                self.freinds[x]= 0
            print()
            billValue = int(input("Enter the total bill value:"))
            print()
            luck = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
            print()
            if luck == "Yes":
                name = random.choice(list(self.freinds.keys()))
                print(name +" is the lucky one!")
                for key, value in self.freinds.items():
                    if key == name:
                        self.freinds.update({key: 0})
                        
                everyOneValue = round(billValue/(self.size - 1), 2)
                for key, value in self.freinds.items():
                    if key != name:
                        self.freinds.update({key: everyOneValue})
                print(self.freinds)
                print()
            elif luck == "No":
                print("No one is going to be lucky")
                everyOneValue = round(billValue/self.size,2)
                for key, value in self.freinds.items():
                    self.freinds.update({key: everyOneValue})
                print(self.freinds)
BillSplitter().check_numberOfFreinds()
