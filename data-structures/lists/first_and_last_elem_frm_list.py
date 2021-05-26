# Python3 code to demonstrate  
# to get first and last element of list 
# using list comprehension 
  
# initializing list  
test_list = [1, 5, 6, 7, 4] 
  
# printing original list  
print ("The original list is : " +  str(test_list)) 
  
# using list comprehension 
# to get first and last element of list 
res =  [ test_list[i] for i in (0, -1) ] 
  
# printing result 
print ("The first and last element of list are : " +  str(res)) 
