import math
import calculate

def variance(x):
    n = len(x)
    S = (calculate.sumOfSquare(x) - pow(sum(x), 2) / n) / (n - 1) 
    return S

def t_value(x1, x2, S1, S2):
    n1 = len(x1)
    n2 = len(x2)
    t = (calculate.mean(x1) - calculate.mean(x2)) / math.sqrt((S1 / n1) + (S2 / n2))
    return t

def showResult(S1, S2, mean_x1, mean_x2, t):
    print(f"Mean of Sample 1: {mean_x1:.4f}")
    print(f"Mean of Sample 2: {mean_x2:.4f}")
    print(f"Variance of Sample 1: {S1:.4f}")
    print(f"Variance of Sample 2: {S2:.4f}")
    print(f"T-Value: {t:.4f}")

if __name__ == '__main__':
    x1 = [11, 1, 0, 2, 0]
    x2 = [11, 11, 5, 8, 4]
    mean_x1 = calculate.mean(x1)
    mean_x2 = calculate.mean(x2)
    S1, S2 = variance(x1), variance(x2)
    t = t_value(x1, x2, S1, S2)
    showResult(S1, S2, mean_x1, mean_x2, t)