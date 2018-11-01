# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:08:20 2018

@author: javie
"""


class Node(object):
    item = -1
    next = None
    def __init__(self, item, next):
        self.item = item
        self.next = next



    
def readFile(file):
    temp = None
    try:
        with open(file) as fileReader:
            for line in fileReader:
                temp = Node(line, temp)
        return temp
    except:
        pass


#combining lists
def combine(activision_list, vivendi_list):
    if activision_list is None:
        return vivendi_list
    elif vivendi_list is None:
        return activision_list
    
    temp = vivendi_list
    while temp.next is not None:
        temp = temp.next
    temp.next = activision_list
    return vivendi_list

def count(combined):
    count = 0
    while combined is not None:
        count = count + 1
        combined = combined.next
    return count


#solution_1
def sol_a(combined, length):
    temp = combined
    duplicate = []
    for i in range (length):
        temp2 = temp.next
        for j in range (i+1, length):
            if temp.item == temp2.item:
                duplicate.append(temp.item)
                break
            else:
                temp2 = temp2.next
        temp = temp.next
    return duplicate
        
def print_dup(array):
    print ('Duplicates are: ' )
    for i in array:
        print(i, end='')

#solution2
def bubbleSort(combined, length):
   if combined == None:
       print('list is empty')
       return combined
   head = combined
   for i in range(length):
       temp = head
       
       for j in range(length):
           if temp.next != None:
               if int(temp.item) > int(temp.next.item):
                   temp2 = temp.item
                   temp.item = temp.next.item
                   temp.next.item = temp2
           temp = temp.next   
   return head

def bubble_dup(dupli):
    duplicate = []
    while dupli.next != None:
        if dupli.item == dupli.next.item:
            duplicate.append(dupli.item) 
        dupli = dupli.next
    return duplicate


#solution3 
def mergeSort(combined):
    length = count(combined)
    temp = combined
    
    #base case
    if combined == None:
        print('List is empty')
        return combined
    if combined.next == None:
        return combined
    
    
    for i in range(length//2 - 1):
        temp = temp.next
        
    b = temp.next
    temp.next = None
    a = combined
    
    list_a = mergeSort(a)
    list_b = mergeSort(b)
    sortedList = None
    
    #get the root of the sorted list
    if int(list_a.item) < int(list_b.item):
        sortedList = list_a
        list_a = list_a.next
    else:
        sortedList = list_b
        list_b = list_b.next
        
    mainList = sortedList
    
    #Add in items from both lists in order to merge them together
    while list_a != None and list_b != None:  
        if int(list_a.item) < int(list_b.item):
            sortedList.next = list_a
            list_a = list_a.next
        else:
            sortedList.next = list_b
            list_b = list_b.next
        sortedList = sortedList.next
    
    #if there's anything left in the first list, add them in
    while list_a != None:
        sortedList.next = list_a
        list_a = list_a.next
        sortedList = sortedList.next
        
    #if there's anything left in the second list, add them in
    while list_b != None:
        sortedList.next = list_b
        list_b = list_b.next
        sortedList = sortedList.next
        
    #return reference to first item in list
    return mainList
        
#solution 4
def booleanCheck(combined):
    duplicate = []
    bool_arr = []
    temp = combined

    for i in range(6001):#could this hard code have been done differently?
        bool_arr.append(False)
    
    for i in range (count(combined)):
        if temp != None or temp.next != None:
            if bool_arr[int(temp.item)] == False:
                bool_arr[int(temp.item)] = True
            
            elif bool_arr[int(temp.item)] == True:
                duplicate.append((temp.item))
          
        temp = temp.next
    
    return duplicate
            


#print link list
def print_link(list):
    temp = list
    while temp is not None:
        print (temp.item)
        temp = temp.next
    return 



# =============================================================================
def main():
    activision_file = "activision.txt"
    vivendi_file = "vivendi.txt"
    
    activision_list = readFile(activision_file)
    vivendi_list = readFile(vivendi_file)
    
    combined = combine(activision_list, vivendi_list)
    length = count(combined)
    
    
    
  #solution 1 unsorted linked list prints  
# =============================================================================
#     duplicate_array = sol_a(combined, length)
#     print_link (combined)
#     print_dup(duplicate_array)
# =============================================================================
 
    #solution 2 bubble sort linked list prints
# =============================================================================
#     print('Bubble sort')
#     print_link (bubbleSort(combined, length))
#     print('Bubble Sort end')
#     
#     bubble_list = bubbleSort(combined, length)
#     bubble_array = bubble_dup(bubble_list)
#     
# =============================================================================
    # solution 2 duplicated bubble list
# =============================================================================
#     print('duplicate in bubble')
#     print_dup(bubble_array)
#     print('printed the list')
# =============================================================================
 
    # solution 3 merge sort linked list prints
# =============================================================================
#     print('merged sort')
#     print_link(mergeSort(combined))
#     print('end')

#    merge_list = mergeSort(combined)
#    merge_array = bubble_dup(merge_list)
# =============================================================================
   # solution 3 duplicated merge list
# =============================================================================
#     print('Duplicates in Merge')
#     print_dup(merge_array)
#     print('End of Duplicates')
# =============================================================================
    
   # solution 4 unsorted check if they repeat
    check = booleanCheck(combined)
    print_dup(check)
   

   
    
main()

# =============================================================================
