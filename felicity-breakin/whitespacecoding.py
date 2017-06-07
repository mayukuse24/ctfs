file_contents = open("program.cpp").read()

tabs=newline=space=0
for character in file_contents:
    if character == " ":
        print('S ', end="", flush=True)
        space +=1
    elif character == '\t':
        print('T ', end="", flush=True)
        tabs += 1
    elif character == '\n':
        print('L\n', end="", flush=True)
        newline += 1
        
print(space,tabs,newline)
