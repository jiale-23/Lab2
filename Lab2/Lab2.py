x = 0

def display_main_menu():
    print("Enter some numbers seperated by commas")

def get_user_input():
    x = input().split(',')
    y = [float(s) for s in x]
    return y

def avg(x):
    y = 0
    for s in x:
        y += s
    return y/len(x)

def min_man(x):
    return [sort(x)[0], sort(x)[len(x)-1]]

def sort(x):
    for i in range(len(x)):
        for j in range (len(x)-1):
            if (x[j] > x[j+1]):
                temp = x[j+1]
                x[j+1] = x[j]
                x[j] = temp

    return x
        

def median(x):
    if (len(x)%2 != 0):
        y = len(x)/2 + 0.5 - 1
        return sort(x)[int(y)]
    else:
        y = len(x)/2 - 1
        return (sort(x)[int(y)]+sort(x)[int(y)+1])/2




def main():
    display_main_menu()
    x = get_user_input()
    print(min_man(x))


if __name__ == "__main__":
    main()