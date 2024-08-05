code = input()
i = 0
decoded = ""

while i < len(code):
    if code[i] == "-" and code[i+1] == "-":
        decoded+="2"
        i+=1
    elif code[i] == "-" and code[i+1] == ".":
        decoded += "1"
        i+=1
    else:
        decoded += "0"
    i+=1

print(decoded)


# Optimal Implementation - 
R=str.replace
print(R(R(R(input(),'--','2'),'-.','1'),'.','0'))