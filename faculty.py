def my_faculty(n):
    mul = 1
    if n==0:
        return 1
    else:
        for mul_i in range(n,0,-1):
            mul = mul * mul_i
    return mul

# print(my_faculty(5))