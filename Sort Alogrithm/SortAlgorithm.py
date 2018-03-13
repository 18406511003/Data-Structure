#coding:utf-8
#usr:Yao
#Sort algorithm



List = [49,38,65,97,76,13,27,55]
print List
# bubble sort 
def BubbleSort(List):
	Len_list = len(List)-1
	while Len_list>2:
		for i in range(Len_list):
			if List[i]>List[i+1]:
				List[i],List[i+1] = List[i+1],List[i]
		Len_list -= 1
	return List 
# print BubbleSort(List)

# fast sort
def FastSortOnce(List,low,high):
	init = List[low]
	while low<high:
		while low<high and List[high]>init:
			high -= 1
		List[low] = List[high]
		while low<high and List[low]<init:
			low += 1
		List[high] = List[low]
	List[low] = init
	return low
def FastSort(List,low,high):
	if low < high:
		index = FastSortOnce(List,low,high)
		FastSort(List,low,index-1)
		FastSort(List,index+1,high)
	return List
# print FastSort(List,low=0,high=len(List)-1)

# heap sort

def HeapAd(List,low,length):
	leftchild = 2*low+1
	rightchild = 2*low+2
	max = low
	if low<length:
		if leftchild<length and List[max]<List[leftchild]:
			max = leftchild
		if rightchild<length and List[max]<List[rightchild]:
			max = rightchild	
		if max!=low:
			List[low],List[max] = List[max],List[low]
			HeapAd(List,max,length)
def HeapSort(List):
	length = len(List)
	for i in range(0,int(length/2))[::-1]:
		HeapAd(List,i,length)                     #建大顶堆
	for i in range(0,length)[::-1]:
		List[0],List[i] = List[i],List[0]
		HeapAd(List,0,i)
	return List
# print HeapSort(List)

# insertion sort
def InsertSort(List):
	length = len(List)
	for i in range(1,length):
		index = List[i]
		j = i-1
		while j>=0:
			if List[j]>index:
				List[j],List[j+1] = index,List[j]
			j-=1
	return List
# print InsertSort(List)

#Shell sort
def ShellSort(List,Step):
	length = len(List)
	group = length/Step
	while group >0:
		for i in range(0,group):
			j=i+group
			while j < length:
				k = j-group
				index = List[j]
				while k >= 0:
					if List[k]>index:
						List[k+group] = List[k]
						List[k] = index
					k-=group
				j+=group
		group -= 1
	return List
# print ShellSort(List,2)

# select sort
def SelectSort(List):
	length = len(List)
	for i in range(length):
		min = i
		for j in range(i+1,length):
			if List[j]< List[min]:
				min = j
		List[i],List[min] = List[min],List[i]
	return List
# print SelectSort(List)

# merge sort
def Merge(left,right):
	i,j = 0,0
	result = []
	while len(left)>i and len(right)>j:
		if left[i]>right[j]:
			result.append(right[j])
			j+=1
		else:
			result.append(left[i])
			i+=1
	
	result += left[i:]
	result += right[j:]
	return  result

def MergeSort(List):
	length = len(List)
	if len(List)<= 1:
		return List
	num = length/2
	left = MergeSort(List[:num])
	right = MergeSort(List[num:])
	return Merge(left,right)
print MergeSort(List)