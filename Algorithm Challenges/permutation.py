# Input: list [1, 2, 3]
# Potential outputs: 

array = [1, 2, 3]

# 123, 132, 213, 231, 321, 312
def permutation(array: list):
    array2:list=[]
    for i in array:
        for j in array:
            for k in array:
                if i != j and j != k and k != i:
                    array2.append(format(f"{i}{j}{k}"))
    return array2

def main():
    print(permutation(array))

main()