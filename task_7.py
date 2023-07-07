def digit_root(num):
    if 1 <= num < 10**7:
        sum = 0
        for n in str(num):
            sum += int(n)

        if sum > 9:
            sum1 = 0
            for s in str(sum):
                sum1 += int(s)

            if sum1 > 9:
                sum2 = 0
                for s1 in str(sum1):
                    sum2 += int(s1)

                if sum2 > 9:
                    sum3 = 0
                    for s2 in str(sum2):
                        sum3 += int(s2)
                    print(sum3)

                else:
                    print(sum2)

            else:
                print(sum1)

        else:
            print(sum)