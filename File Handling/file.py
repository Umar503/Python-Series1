
#write in file and if file does not exist create that file

with open('umr.txt', 'r', encoding='utf-8') as file:
    
    content = file.read()
    print(content)
file.close()


#write over the existing file text;

f = open('umr.txt','w')
f.write("Wellcome Mr Umar!")
f.close()


#append text to file

f = open('umr.txt','a')
f.write("\nI am glad to see you.")
f.close()


#Read the first line

f = open('umr.txt')
first_line= f.readline()
print(first_line)