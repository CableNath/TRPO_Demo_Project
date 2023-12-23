def complex_function(a, b, c):
    result = []
    if a > 0:
        for i in range(a):
            if i % 2 == 0:
                result.append(i * b)
            else:
                result.append(i + c)
    else:
        result.append("Error: 'a' must be greater than 0")
    
    
    return result