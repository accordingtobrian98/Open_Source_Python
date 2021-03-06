def sum(n):
    """
    :param n: a non-negative integer
    :return: the sum 0+1+2+3+...+n
    >>> sum(10)
    55
    """
    result = 0
    sum = 0
    for i in range(0, n):
        sum += i
        result = n + sum
    return result


def write_backwards(n):
    """
    :param n: positive integer, with 4 digits, such that first and last digit are non-zero.
    return: another positive integer, written using same digits as n, in reverse order.
    >>> write_backwards(1234)
    4321
    """
    # Hint: use // and % operators.
    # Do not use loops, if-else, or strings.
    # Write your code here and replace return

    a = n%10
    b = n%100
    c = b//10
    d = n //100
    e = d % 10
    f = d // 10

    list = []
    list.append(a)
    list.append(c)
    list.append(e)
    list.append(f)
    num = int(''.join(map(str, list)))
    return num


def bouncy_ball_sequence(bounce_coefficient, height):
    """
    :param: bounce_coefficient: What portion of initial height will the ball bounce
    :param: height: height in meters
    If a bouncy ball with the given bounce_coefficient, drops from the specified height,
    return: how many times the ball will bounce before it stops (final height<.01).
    Example: bouncy_ball(.6, 553) will print the heights the ball reaches initially, and
    after each bounce, when dropped from the CN Tower (553 Meters).

    Example, CN Tower: 553 m
    >>> bouncy_ball_sequence(.6, 553)
    22
    """
    how_many = 0

    while height > .01:
        how_many += 1
        height = bounce_coefficient*height

    return how_many



def marathon_time(half_marathon, is_hilly):
    """
    :param half_marathon: best runner's half marathon time
    :param is_hilly: boolean, true if and only if marathon course is hilly.
    return: marathon time
    How Long will it take?
    A common back-of-the-envelope technique for estimating a runner's marathon time is to take their
    best half-marathon time, multiply by two and add ten minutes. This works pretty well unless the
    marathon course is hilly. If it is hilly, we add an extra 20 minutes to the estimate. Complete the
    function marathon_time that takes a half-marathon time in minutes and whether or not the marathon
    course is hilly as parameters and returns the estimated number of minutes the runner will take to run
    the full marathon.
    """
    time = 0
    if(is_hilly == True):
        time = half_marathon*2+10+20
    else:
        time = half_marathon*2+10

    return time

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(write_backwards(7685))  # expected 5867
    print(sum(5))  # expected 15
    print(bouncy_ball_sequence(.6, 0.005))  # expected 0
    print(marathon_time(300, False))
    print(marathon_time(300, True))
