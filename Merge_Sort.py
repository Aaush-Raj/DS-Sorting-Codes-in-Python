																		
														#				MERGE SORT - PYTHON CODE

		def merge_sort(array):
			if len(array)>1:
				left_array = array[:len(array)//2]
				right_array = array[len(array)//2:]

				merge_sort(left_array)
				merge_sort(right_array)
				
				i = 0
				j = 0
				k = 0
				while i<len(left_array) and j<len(right_array):
					if left_array[i] < right_array[j]:
						array[k] = left_array[i]
						i = i+1
					else:
						array[k] = right_array[j]
						j = j+1
					k = k+1

				while i < len(left_array):
					array[k] = left_array[i]
					i += 1
					k += 1

				while j < len(right_array):
					array[k] = right_array[j]
					j += 1
					k += 1
						
				


		array = [50,40,60,30,80,90,70,20,10,0,100]
		merge_sort(array)

		print(array)



#		+===============================================+
#		+			 By - Aaush Raj						+
#		+		- aayushcontactinfo@gmail.com			+
#		+												+
#		+===============================================+