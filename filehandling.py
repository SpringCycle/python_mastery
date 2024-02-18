#Method 1
file= open(file.txt,"r") #opening file.txt with read mode
data=file.read()  
file.close()


#Method2
with open("welcome.txt") as infile:
    data= file.read()

file_object = open("file_name","Access_Mode")