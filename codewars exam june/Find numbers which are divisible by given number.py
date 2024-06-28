def divisible_by(numbers, divisor):
    helper=[]
    for i in numbers:
        if i%divisor==0:
            helper.append(i)
    return helper