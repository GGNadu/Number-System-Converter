in_no = input("Enter Number: ")
base = int(input("Enter Base: "))

new_list = []
if base > 10:
    num_list = [(b) for b in in_no]
    num_list2 = num_list
    x = len(num_list2)
    while x > 0:
        if num_list2 [0] == 'A':
            num_list2 [0] = 10
        elif num_list2 [0] == 'B':
            num_list2 [0] = 11
        elif num_list2 [0] == 'C':
            num_list2 [0] = 12
        elif num_list2 [0] == 'D':
            num_list2 [0] = 13
        elif num_list2 [0] == 'E':
            num_list2 [0] = 14
        elif num_list2 [0] == 'F':
            num_list2 [0] = 15
        new_list.append (num_list2 [0])
        num_list2.pop (0)
        x = x-1
        new_list = [int (a) for a in new_list]
    
else :
   new_list = [int (a) for a in in_no]


i=0
c=0
x1=0
le = len(new_list)

while le > 0 :
    i = new_list[-1] * (base**c)
    x1= x1+i
    c=c+1
    new_list.pop (-1)
    le= le-1

print("\n================================================")
print(f"{in_no} and {base} base convert to Decimal")
print (x1)
