def digit_root(num):
    if 0 <= num < 10**7:
        while num > 9:
            num = sum(int(digit) for digit in str(num))
        return num
    else:
        return None