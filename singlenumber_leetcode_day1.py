#step1:get the input list from the user

string=input("Give the input of numbers saperated by space")
#step2:splitting the entered list of numbers
list_input=string.split(" ")
print(list_input)

#step3:create the dictionary to store the values of the list
dict1={}
for i in range(0,len(list_input)):
    #if element is already present in the dict we will just increment the value
    if(dict1.get(list_input[i])):
        #getting the value from the dictionary
        value=dict1.get(list_input[i])+1
        #updating the dictionary
        dict1.update({list_input[i]:value})
    else:
        #if the element is not present in the dictionary already then we are just appending that element into dictionary
        dict1[list_input[i]]=1

key=[ key for key in dict1 if dict1[key]==1]
print(key)
