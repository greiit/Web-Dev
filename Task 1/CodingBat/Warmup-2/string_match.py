def string_match(a, b):
    mn = min(len(a), len(b))
    counter = 0

    for i in range(mn - 1):
        if(a[i:i+2] == b[i:i+2]):
            counter += 1

    return counter
