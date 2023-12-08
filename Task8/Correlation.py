import math


def calculate_correlation(signal1, signal2, float_point):
    N = len(signal1)
    result = []

    x1_square = [i ** 2 for i in signal1]
    x2_square = [i ** 2 for i in signal2]
    p12_denominator = math.sqrt((sum(x1_square) * sum(x2_square))) / N
    p12_denominator = round(p12_denominator, float_point)

    # from r1 to r_end
    for i in range(1, N + 1):
        signal2_shifted = signal2[i:] + signal2[0:N - (N - i)]
        print(signal2_shifted, i)
        r = round(sum([signal1[i] * signal2_shifted[i] for i in range(N)]) / N, float_point)
        p = round(r / p12_denominator, float_point)
        result.append(p)

    # r0 == r_end
    result = [result[N - 1]] + result
    return result


signal1 = [2, 1, 0, 0, 3]
signal2 = [3, 2, 1, 1, 5]

float_point = 2

print(calculate_correlation(signal1, signal2, float_point))
