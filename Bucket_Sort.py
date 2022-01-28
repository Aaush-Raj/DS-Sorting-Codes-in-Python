															 
												#			BUCKET SORT - PYTHON CODE



def insertionSort(n):
	for i in range(1, len(n)):
		up = n[i]
		j = i - 1
		while j >= 0 and n[j] > up:
			n[j + 1] = n[j]
			j -= 1
		n[j + 1] = up	
	return n	
			
def bucketSort(array):
	arr = []
	Bucket_Num = 10 
	for i in range(Bucket_Num):
		arr.append([])
	for j in array:
		index_b = int(Bucket_Num * j)
		arr[index_b].append(j)
	for i in range(Bucket_Num):
		arr[i] = insertionSort(arr[i])
	k = 0
	for i in range(Bucket_Num):
		for j in range(len(arr[i])):
			array[k] = arr[i][j]
			k += 1
	return array
array = [99,11,22,55,44,66,33,77,88]
print(bucketSort(array))




#		+===============================================+
#		+			 By - Aaush Raj						+
#		+		- aayushcontactinfo@gmail.com			+
#		+												+
#		+===============================================+