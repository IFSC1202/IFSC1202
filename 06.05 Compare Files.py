# open file in read mode
file_1 = open(" Compare File A", "r")
file_2 = open (" Compare File B", "r")
print("comparing files" , " " + " Compare File A" , + " Compare File B" , sep=("/n"))
file_1 = file_1. readline ()
file_2 = file_2. readline ()
line_no = 1
with open (" Compare File A:") as file1:
    with open(" Compare File B: ") as file2:
     same = set(file1).intersection(file2)
print("Common lines in both files: ") 
for line in same:
    print(line,end ="")    
print("/n")  
print("Difference lines in both files: ")  
while file_1_line != " " or file_2_line != "":
    file_1_line = file_1_line . rstrip()
    file_2_line = file_2_line . rstrip()
    if file_1_line != file_2_line:
        print("" , "line-d%" % line_no,file_1_line)
    else:
        print("", "line-d%" % line_no, file_1_line) 
    if file_2_line == "" :
        print("#" , "line-%d" % line_no, file_2_line) 
    else:
        print("#", "line_d%" % line_no, file_2_line)
    print() 
file_1_line = file_1.readline()
file_2_line = file_2. readline()       
line_no += 1
file_1.close()
file_2.close()   
