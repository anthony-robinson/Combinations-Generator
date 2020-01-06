import sys

argv2 = int(sys.argv[2])
argv1 = int(sys.argv[1])
X_all = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def construct_Set(size):
    X = X_all[:size]
    return X
X = construct_Set(argv1)
def Ugenerator(arr,choices,combos):
    if choices == 0:
        print(combos)
    else:
        for i in range(len(arr)):
            Ugenerator(arr[i + 1:len(arr)], choices - 1, combos + arr[i])
output = ""
Ugenerator(X, argv2, output)
