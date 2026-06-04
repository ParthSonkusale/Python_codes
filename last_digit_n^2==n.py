def green(n):
    count = 0
    num = 1

    while True:
        if str(num * num).endswith(str(num)):
            count += 1

            if count == n:
                return num

        num += 1 
