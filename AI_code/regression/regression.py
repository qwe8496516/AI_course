import math
import calculate

def slope_intercept(SSxy, SSx, x, y):
    b0 = calculate.mean(y) - (SSxy / SSx) * calculate.mean(x)
    b1 = SSxy / SSx
    return b0, b1

def covariance(x, y):
    n = len(x)
    mean_x = calculate.mean(x)
    mean_y = calculate.mean(y)
    SSxy = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / (n - 1)
    SSx = sum(pow((x[i] - mean_x), 2) for i in range(n)) / (n - 1)
    SSy = sum(pow((y[i] - mean_y), 2) for i in range(n)) / (n - 1)
    return SSxy, SSx, SSy

def coorelationCoefficientSquare(SSxy, SSx, SSy):
    return pow(SSxy, 2) / (SSx * SSy)

def coorelationCoefficient(CCS, b1):
    if (b1 < 0):
        return math.sqrt(CCS) * (-1)
    else:
        return math.sqrt(CCS)

def sumOfSquares(SSxy, SSx, SSy, len):
    SSR = pow(SSxy, 2) * (len - 1) / SSx
    SST = SSy * (len - 1)
    SSE = SST - SSR
    return SSR, SST, SSE

def degreeOfFreedomBetweenAndWithin(x, y):
    dfb = 1
    dfw = len(x) - 2
    return dfb, dfw
    
def meanSumOfSquare(SSR, SSE, dfb, dfw):
    MSB = SSR / dfb
    MSW = SSE / dfw
    return MSB, MSW

def f_value(MSB, MSW):
    return MSB / MSW

def showResult(SSxy, SSx, SSy, b0, b1, CCS, CC, SSR, SST, SSE, dfb, dfw, MSB, MSW, F):
    print(f"SSxy: {SSxy:.4f}")
    print(f"SSx: {SSx:.4f}")
    print(f"SSy: {SSy:.4f}")
    print(f"b0: {b0:.4f}")
    print(f"b1: {b1:.4f}")
    print(f"Regression Function: y = {b0:.4f} + {b1:.4f} * x")
    print(f"Coorelation Coefficient Square: {CCS:.4f}")
    print(f"Coorelation Coefficient: {CC:.4f}")
    print(f"SSR: {SSR:.4f}")
    print(f"SST: {SST:.4f}")
    print(f"SSE: {SSE:.4f}")
    print(f"Degree of Freedom Between: {dfb}")
    print(f"Degree of Freedom Within: {dfw}")
    print(f"Mean Sum of Square Between: {MSB:.4f}")
    print(f"Mean Sum of Square Within: {MSW:.4f}")
    print(f"F Value: {F:.4f}")

if __name__ == '__main__':
    x = [50, 53, 60, 53, 63, 70, 60, 53, 60, 86]
    y = [156, 179, 189, 160, 185, 210, 189, 168, 191, 237]
    length = len(x)
    SSxy, SSx, SSy = covariance(x, y)
    b0, b1 = slope_intercept(SSxy, SSx, x, y)
    CCS = coorelationCoefficientSquare(SSxy, SSx, SSy)
    CC = coorelationCoefficient(CCS, b1)
    SSR, SST, SSE = sumOfSquares(SSxy, SSx, SSy, length)
    dfb, dfw = degreeOfFreedomBetweenAndWithin(x, y)
    MSB, MSW = meanSumOfSquare(SSR, SSE, dfb, dfw)
    F = f_value(MSB, MSW)
    showResult(SSxy, SSx, SSy, b0, b1, CCS, CC, SSR, SST, SSE, dfb, dfw, MSB, MSW, F)