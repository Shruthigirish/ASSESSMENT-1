def reverse(str):   
    string = "".join(reversed(str)) # reversed() function inside the join() function  
    return string   
  
str_input = input("Enter the string to be reversed :")
  
print ("The original string is : ",str_input)   
print ("The reversed string using reversed() is : ",reverse(str_input) )  