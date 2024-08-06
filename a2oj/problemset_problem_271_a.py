year = int(input())
duplicate_year = year
newYear = ""
flag = True
DidFind = False


while flag:
    tempYear = str(duplicate_year + 1)
    duplicate_year += 1
    i = 0

    while i < len(tempYear):    
        if newYear.find(tempYear[i]) != -1:
            break
        else:
            newYear += tempYear[i]

        if i == len(tempYear) - 1:
            flag = False
            print(newYear)
        i +=1
    newYear = ""

