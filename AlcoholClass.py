# -*- coding: utf-8 -*-
#!/usr/bin/python3
from klepto.archives import file_archive

class Alcohol(object):

    totals = 0
    
    def __init__(self, fullBottles=0, threeQuarters=0, half=0, oneQuarters=0, price=0):
    
        self.fullBottles = fullBottles
        self.threeQuarters = threeQuarters
        self.half = half
        self.oneQuarters = oneQuarters
        self.price = price
        
    def total(self):
        total = (self.price*self.fullBottles)+(self.price*self.threeQuarters*.75)+(self.price*self.half*.5)+(self.price*self.oneQuarters*.25)
        Alcohol.totals += total 
        return total
        
    def __str__(self):
        return 'Full:'+str(self.fullBottles)+' threeQuarters:'+str(self.threeQuarters)+' half:'+str(self.half)+' oneQuarters:'+str(self.oneQuarters)
        
def getAmount(size=None):
    '''Take input as int error handle
    Optional size of amount'''
    while ValueError:
        try:
            if size == None:
                amount = float(input('Enter the amount: '))
                return amount
            else:
                print('Enter the amount of %s: ' %  (size))
                amount = int(input('\nAmount: '))
                return amount
        except ValueError:
            print('\nThat wasn\'t a number')
            
def getName():
    #Error handling of name.
    while KeyError:
        try:
            name = str(input('Enter a name: '))
            if name == '':
                print('Invalid name. Try again.')
            else:
                return name
        except KeyError:
            print('Invalid name. Try again.')
            
def getSize():
    #Error handling of size
    while KeyError:
        try:
            size = str(input('Enter a size: '))
            if size == '':
                print('Invalid size. Try again.')
            elif size in ['fullBottles', 'threeQuarters', 'half', 'oneQuarters', 'all']:
                return size 
        except KeyError:
            print('Invalid size. Try again.')
    
def main(): 
    
    choice = None
    try:
        alcohols = file_archive('Alcohols.txt')
        alcohols.load()
    except IOError:
        alcohols = {}
        print('alcohols doesn\'t exist.')
        
    while choice != '0':
        
        print('''Your choices are... 
            1 - Add a new alcohol bottle
            2 - Edit number bottles: 
            3 - Edit prices: 
            4 - Remove a bottle from inventory:
            5 - View alcohols in inventory.
            6 - View grandtotal of inventory.
            0 - To save and exit the program
            ''')
        
        choice = input('Which option would you like: ')
        
        if choice == '1':
            print('What is the name of the alcohol?')
            name = getName()
            if name in alcohols:
                print('Sorry this alcohol is already created. Pick the correct choice to edit.')
            else:
                alcohols[name] = Alcohol() #instantiates the new class
                
        elif choice == '2':
            print('Enter the name of the alcohol you wish to edit.')
            name = getName()
            if name in alcohols: #checking make sure alcohol is already in the list otherwise they need to create it
                print('\nWhich size of bottle or all of them?')
                print('If you want to add or subtract just take current amount\nand add however many bottles or subtract. \nExample: Current amount=10 want to take 2 away. Just enter 8 amount of bottles.')
                size = getSize()
                if size == 'all':
                    print(alcohols[name])
                    amount = getAmount(size='fullBottles')
                    setattr(alcohols[name], 'fullBottles', amount)
                    amount = getAmount(size='threeQuarters')
                    setattr(alcohols[name], 'threeQuarters', amount)
                    amount = getAmount(size='half')
                    setattr(alcohols[name], 'half', amount)
                    amount = getAmount(size='oneQuarters')
                    setattr(alcohols[name], 'oneQuarters', amount)
                elif size == 'fullBottles':  #finish rest of the sizes make it getitem and they can add or subtract. not sure on this
                    print('Currently have %s.'  % (alcohols[name].fullBottles))
                    amount = getAmount(size) 
                    setattr(alcohols[name], 'fullBottles', amount)
                elif size == 'threeQuarters':
                    print('Currently have %s.' % (alcohols[name].threeQuarters))
                    amount = getAmount(size)
                    setattr(alcohols[name], 'threeQuarters', amount)
                elif size == 'half':
                    print('Currently have %s.' % (alcohols[name].half))
                    amount = getAmount(size)
                    setattr(alcohols[name], 'half', amount)
                elif size == 'oneQuarters':
                    print('Currently have %s.' % (alcohols[name].oneQuarters))
                    amount = getAmount(size)
                    setattr(alcohols[name], 'oneQuarters', amount)
            elif name not in alcohols:
                print('This alcohol doesn\'t exist. Try again.')
        elif choice == '3':
            print('What is the name of alcohol which price you want to edit? ')
            name = getName()
            if name in alcohols:
                amount = getAmount()
                setattr(alcohols[name], 'price', amount)
            elif name not in alcohols:
                print('This alcohol doesn\'t exist. Try again.')
        elif choice == '4':
            print('Enter the name of the alcohol you wish to remove.')
            name = getName()
            if name not in alcohols:
                print('This alcohol doesn\'t exist. Try again.')
            elif name in alcohols:
                alcohols.pop(name) #deletes the key out of the dict
                alcohols.archive.pop(name)
        elif choice == '5':
            print([i for i in alcohols.keys()])
        elif choice == '6':
            Alcohol.totals = 0
            for i in alcohols.values():
                i.total()
            print(Alcohol.totals)
        elif choice == '0':
            alcohols.dump() #saves the dictionary data as is
            alcohols.archive
            print('Exiting and saving the data.')
        else:
            print('That\'s not a valid choice.')
    
main()

        

        
