 					                                                
				#				BUBBLE SORT - PYTHON CODE
																	
																	

		number = int(input("Enter the Length of your desired Array"))
		alist = []

		for add in range(number):
			variable = int(input("Enter the number"))
			alist.append(variable)

		def bubblesort(array):
			for j in range(0,len(array)):
				for i in range(0,len(array)-1):
					if array[i] > array[i+1]:
						temp = array[i+1]
						array[i+1] = array[i]
						array[i] = temp

			return array


		buble = bubblesort(alist)
		print(buble)


#		+===============================================+
#		+			 By - Aaush Raj		+		
#		+		- aayushcontactinfo@gmail.com	+		
#		+						+						
#		+===============================================+
