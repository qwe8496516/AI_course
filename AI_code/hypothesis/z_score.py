import math

def standard_deviation(sample_size, sample_standard_deviation):
    return sample_standard_deviation / (math.sqrt(sample_size))

def z_score(popluation_average, sample_average, popluation_standard_deviation):
    return (sample_average - popluation_average) / popluation_standard_deviation

def showResult(popluation_average, z_score_value):
    print(f"Population Average: {popluation_average:.4f}")  
    print(f"Z-Score: {z_score_value:.4f}")

# if samples > 30 then population_standard_deviation can use sample_standard_deviation to calculate
if __name__ == "__main__":
    popluation_average = 80000
    popluation_standard_deviation = 0
    sample_size = 25
    sample_average = 75000
    sample_standard_deviation = 10000
    popluation_standard_deviation = standard_deviation(sample_size, sample_standard_deviation)
    z_score_value = z_score(popluation_average, sample_average, popluation_standard_deviation)
    showResult(popluation_average, z_score_value)