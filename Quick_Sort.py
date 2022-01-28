
							#		QUICK SORT - PYTHON CODE
																			
																					
		array = [99,11,22,55,44,66,33,77,88]

		def Quick_Sort(array,start,end):
			if start >= end:
				return
			pivot = array[start]
			i = start + 1
			j = end
			
			while True:
				while i<=j and array[i]<= pivot:
					i = i + 1
				while i<=j and array[j] >= pivot:
					j = j - 1
				if i<=j:
					array[i],array[j] = array[j],array[i]
				else:
					break

			 
			array[start],array[j] = array[j],array[start]

			if (start - j > 1):
				Quick_Sort(array,start,j-1)
			if (end - j > 1):
				Quick_Sort(array,j+1,end)
			return array

		Quick_Sort(array,0,len(array)-1)
		print(array)
																								
	
#		+===============================================+
#		+			 By - Aaush Raj		+		
#		+		- aayushcontactinfo@gmail.com	+		
#		+						+						
#		+===============================================+
