from klepto.archives import file_archive

class Alcohol(object):

	totals = []
	
	def __init__(self, size=
                     '1l', fullBottles=0, threeQuarters=0, half=0, oneQuarters=0, price=0):
	
		self.size = size
		self.fullBottles = fullBottles
		self.threeQuarters = threeQuarters
		self.half = half
		self.oneQuarters = oneQuarters
		self.price = price
		
	def total(self):
		total = (self.price*self.fullBottles)+(self.price*self.threeQuarters*.75)+(self.price*self.half*.5)+(self.price*self.oneQuarters*.25)
		Alcohol.totals.append(total)
		return total
		
	def bottles(self):
		self.fullBottles = fullBottles
		self.threeQuarters = threeQuarters
		self.half = half
		self.oneQuarters = oneQuarters
		
def getAmount(size=None):
	'''Take input as int error handle
	Optional size of amount'''
	while ValueError:
		try:
			if size == None:
				amount = int(input('Enter the amount: '))
				return amount
			else:
				print('Enter the amount of %s: ' %  (size))
				amount = int(input('\nAmount: '))
				return amount
		except ValueError:
			print('\nThat wasn\'t a number')
			
def getName():
	#Error handling of name.
	name = ''
	while KeyError:
		name = input('\nName: ')
		return name
		
	
def main():	
	
	choice = None
	try:
		alcohols = file_archive('Alcohols.txt')
		alcohols.load()
	except IOError:
		print('%s doesn\'t exist.' % (alcohols))
		
	while choice != '0':
		
		print('''Your choices are... 
			1 - Add a new alcohol bottle and information
			2 - Edit number bottles: 
			3 - Edit prices: 
			4 - Remove a bottle:
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
				alcohols[name] = Alcohol #instantiates the new class
				
		elif choice == '2':
			print('Enter the name of the alcohol you wish to edit.')
			name = getName()
			if name in alcohols: #checking make sure alcohol is already in the list otherwise they need to create it
				amount = getAmount(size='fullBottles')
				setattr(name, fullBottles, amount)
				amount = getAmount(size='threeQuarters')
				setattr(name, threeQuarters, amount)
				amount = getAmount(size='half')
				setattr(name, half, amount)
				amount = getAmount(size='oneQuarters')
				setattr(name, oneQuarters, amount)
			elif name not in alcohols:
				print('This alcohol doesn\'t exist. Try again.')
			else:
				print('Debugging purposes')
		elif choice == '3':
			print('What is the name of alcohol which price you want to edit? ')
			name = getName()
			if name in alcohols:
				amount = getAmount()
				setattr(name, price, amount)
			elif name not in alcohols:
				print('This alcohol doesn\'t exist. Try again.')
			else:
				print('Debugging purposes')
		elif choice == '4':
			print('Enter the name of the alcohol you wish to remove.')
			name = getName()
			if name not in alcohols:
				print('This alcohol doesn\'t exist. Try again.')
			elif name in alcohols:
				alcohols.pop(name, None) #Pops the key out of the dict and return None if keyerror raised
			else:
				print('Debugging purposes')
		elif choice == '5':
			print(alcohols.keys())
			print(alcohols.values())
		elif choice == '6':
			print(sum(Alcohol.totals))
		elif choice == '0':
			print('Exiting and saving the data.')
	
			alcohols.dump() #saves the dictionary data as is
		else:
			print('That\'s not a valid choice.')
			choice = input('Which option would you like: ')
	
main()

'''Still more work to be done but at a good stopping point to show you even in a small amount of time
I can do alot of good work. Also I'm not even sure if I'm using classes correctly at this point I haven't
run this on any data but the general idea, I believe, is presentable.'''	
		

		
