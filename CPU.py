ram = [1, 5, 2, 7, 0]

pc = 1
acc = 0
go = 0
running = True
oper = None

while running:

    go = ram[pc - 1]
    pc += 1

    if go == 1: 
        oper = ram[pc - 1]
        pc += 1
        acc = oper
        print("LOAD", oper)

    elif go == 2: 
        oper = ram[pc - 1]
        pc += 1
        acc += oper
        print("ADD", oper)

    elif go == 3:  
        oper = ram[pc - 1]
        pc += 1
        acc -= oper
        print("SUB", oper)

    elif go == 0:  
        running = False

print("ACC =", acc)
print("End of operation")