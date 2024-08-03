first_line_input = input()

number_of_children = int(first_line_input.split()[0])
time_for_arrangement = int(first_line_input.split()[1])

student_pos = 0


current_arrangement = list(input())

def swap(pos1, pos2):
    current_arrangement[pos1], current_arrangement[pos2] = current_arrangement[pos2], current_arrangement[pos1]



for iteration in range(0, time_for_arrangement):
    while student_pos < number_of_children:
        if current_arrangement[student_pos] == "B" and number_of_children - 1 == student_pos:
            break
        elif current_arrangement[student_pos] == "B" and current_arrangement[student_pos + 1] == "G":
            swap(student_pos, student_pos + 1)
            student_pos += 1
        student_pos += 1
    
    student_pos = 0


print("".join(current_arrangement))


# To check - 
t=int(input()[2:]);s=input()
while t:s=s.replace('BG','GB');t-=1
print(s)