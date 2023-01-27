def return_tuple(target,*args):
    numbers = args
    for i in numbers:
        if i == target and 0 in numbers:
            return (i,0)
        else:
            if (target-i) in numbers:
                return (i,target-i)

print(return_tuple(6,*[2,7,6,5,1]))