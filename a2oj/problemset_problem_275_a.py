# Have a grid with all lights ON
# Figure out the toggle functionality (Here I would suggest have an grid of True and False)
# If multiple number is pressed mod by 2 and check if it's even then :
#       1) Whatever the present state is will be reflected to adjacent sides.
#       2) Else if it's odd the state will toggle.


new_board = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]

user_input = []

for i in range(3):
    c = input()
    strip_down = c.split(' ')
    stripped_input = []
    for j in strip_down:
        if int(j) % 2 == 0:
            stripped_input.append(0)
        else:
            stripped_input.append(1)
    user_input.append(stripped_input)


for i in range(len(new_board)):

    for j in range(len(new_board[i])):
        
        if user_input[i][j] == 1:

            if i == 0 and j == 0:
                new_board[i][j] = not new_board[i][j]
                new_board[i][j+1] = not new_board[i][j+1]
                new_board[i+1][j] = not new_board[i+1][j]
            elif i == 1 and j == 0:
                new_board[i][j] = not new_board[i][j]
                new_board[i][j+1] = not new_board[i][j+1]
                new_board[i-1][j] = not new_board[i-1][j]
                new_board[i+1][j] = not new_board[i+1][j]
            elif i == 2 and j == 0:
                new_board[i][j] = not new_board[i][j]
                new_board[i][j+1] = not new_board[i][j+1]
                new_board[i-1][j] = not new_board[i-1][j]
            elif i == 0 and j == 1:
                new_board[i][j] = not new_board[i][j]
                new_board[i][j-1] = not new_board[i][j-1]
                new_board[i][j+1] = not new_board[i][j+1]
                new_board[i+1][j] = not new_board[i+1][j]
            elif i == 0 and j == 2:
                new_board[i][j] = not new_board[i][j]
                new_board[i][j-1] = not new_board[i][j-1]
                new_board[i+1][j] = not new_board[i+1][j]
            elif i == 1 and j == 1:
                new_board[i][j] = not new_board[i][j]
                new_board[i][j-1] = not new_board[i][j-1]
                new_board[i][j+1] = not new_board[i][j+1]
                new_board[i-1][j] = not new_board[i-1][j]
                new_board[i+1][j] = not new_board[i+1][j]
            elif i == 1 and j == 2:
                new_board[i][j] = not new_board[i][j]
                new_board[i][j-1] = not new_board[i][j-1]
                new_board[i-1][j] = not new_board[i-1][j]
                new_board[i+1][j] = not new_board[i+1][j]
            elif i == 2 and j == 1:
                new_board[i][j] = not new_board[i][j]
                new_board[i][j-1] = not new_board[i][j-1]
                new_board[i][j+1] = not new_board[i][j+1]
                new_board[i-1][j] = not new_board[i-1][j]
            elif i == 2 and j == 2:
                new_board[i][j] = not new_board[i][j]
                new_board[i][j-1] = not new_board[i][j-1]
                new_board[i-1][j] = not new_board[i-1][j]



for i in range(len(new_board)):
    output = ""
    for j in range(len(new_board[i])):
        if new_board[i][j] == True:
            output+="1"
        else:
            output+="0"
    print(output)
    output = ""
            

## Another Approach

t=[]
for i in range(3):
	a=[]
	for j in range(3):
		a.append(0)
	t.append(a)
      
print(t)
for i in range(3):
	k = list(map(int,input().split()))
	for j in range(3):
		t[i][j]+=k[j]
		if i-1>=0:
			t[i-1][j]+=k[j]
		if i+1<3:
			t[i+1][j]+=k[j]
		if j-1>=0:
			t[i][j-1]+=k[j]
		if j+1<3:
			t[i][j+1]+=k[j]
                  
		
for i in range(3):
	for j in range(3):
		if t[i][j]%2==0:
			print("1",end="")
		else:
			print("0",end="")
	print("")

