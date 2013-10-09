def Input():
    while True:
        Value = int(input("Enter the odd number to get the factorization of: "))

        if Value <=0:
            print("Please enter a positive number")
            continue

        if Value%2 == 0:
            print("Please enter an odd number")
            continue

        Case = int(input("Would you like (1) the Greatest prime factor, or (2) the whole factorization: ")) 

        if (Case!=1) and (Case!=2):
            print("Please enter either 1 or 2")
            continue

        break
    return Value, Case
    
def factor(Value, Case):
    if Case == 1:
        Result = 1
        i = 3
        while i <= (Value/3):
            if (Value%i == 0):
                if Result < i:
                    Result = i
                Value = Value/i
                i = 3
            i +=2
        if Value > Result:
            Result = int(Value)
    else:
        Result = []
        i = 3
        cutoff = Value/3
        while i <= cutoff:
            if (Value%i == 0):
                Result.append(i)
                Value = Value/i
                i = 3
                cutoff = int(Value/i)
            i +=2
            cutoff = int(Value/i)
        Result.append(int(Value))
    return Result

def Display(Result):
    print(Result)
    
def main():
    while True:
        Value, Case = Input();
        Result = factor(Value,Case)
        Display(Result)
        Quit = input("Press q to quit, or any key to continue")
        if Quit == "q":
            break

if __name__ == "__main__":
    main()
