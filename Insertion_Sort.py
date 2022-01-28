																	
					#		INSERTION SORT - PYTHON CODE






		n = int(input("Enter how many numbers you want to print :"))
		a = []

		for i in range(n):
				val = int(input("Enter Number"))
				a.append(val)

		def insertionSort(array):
			for step in range(1, len(array)):
				key = array[step]
				j = step - 1
				
				
				# Compare key with each element on the left of it until an element smaller than it is found
				# For descending order, change key<array[j] to key>array[j].        
				while j >= 0 and key < array[j]:
					array[j + 1] = array[j]
					j = j - 1
				
				# Place key at after the element just smaller than it.
				array[j + 1] = key



		insertionSort(a)
		print('Sorted Array in Ascending Order:')
		print(a)
		
		
#		+===============================================+
#		+			 By - Aaush Raj		+		
#		+		- aayushcontactinfo@gmail.com	+		
#		+						+						
#		+===============================================+
