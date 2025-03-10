import dp
import aco
import time
import coordinate
import matplotlib.pyplot as plt
import mlflow

def comparison_algorithm():
    mlflow.set_tracking_uri('http://140.124.181.7:5000')
    mlflow.set_experiment('ACO Time Cost')
    start_city = 0
    num_cities = 50
    alpha = 1
    beta = 1
    evaporation_rate = 0.3
    quality_factor = 1
    iterations = 1000

    aco_time = []
    dp_time = []

    for i in range(2, num_cities):
        with mlflow.start_run() as run:
            mlflow.log_params({ "cities" : i })
            num_coordinate = i
            coordinates = coordinate.generate_coordinates(num_coordinate)
            aco_cost = calculate_aco_time_cost(alpha, beta, evaporation_rate, quality_factor, iterations, start_city, coordinates)
            dp_cost = calculate_dp_time_cost(start_city, coordinates)
            aco_time.append(aco_cost)
            dp_time.append(dp_cost)
            mlflow.log_metrics({ "ACO Time Cost" : aco_cost})
    
    draw_time_cost_graph(aco_time, dp_time, num_cities)

def calculate_aco_time_cost(alpha, beta, evaporation_rate, quality_factor, iterations, start_city, coordinates):
    start_time = time.time()
    for _ in range(5):
        aco.ant_colony_optimization(alpha, beta, evaporation_rate, quality_factor, iterations, start_city, coordinates)
    end_time = time.time()
    return round((end_time - start_time) / 5, 5)

def calculate_dp_time_cost(start_city, coordinates):
    start_time = time.time()
    for _ in range(5):
        dp.dynamic_programming(start_city, coordinates)
    end_time = time.time()
    return round((end_time - start_time) / 5, 5)

def draw_time_cost_graph(aco_time, dp_time, num_cities):
    x_axis = [i for i in range(2, num_cities)]

    f = open('./data/time_cost_log.txt', 'w')
    f.write('Cities\tACO\t\t\tDP\n')
    for i in range(len(x_axis)):
        f.write(f'{x_axis[i]}\t\t{aco_time[i]}\t\t{dp_time[i]}\n')
    f.close()

    plt.plot(x_axis, aco_time, linestyle='-', color='r', label="ACO Time Cost")
    plt.plot(x_axis, dp_time, linestyle='-', color='b', label="DP Time Cost")
    plt.xlabel('Number of Cities')
    plt.ylabel('Time Cost')
    plt.title('Time Cost Comparison (ACO vs DP)')
    plt.legend()
    plt.savefig('./images/time_cost_comparison.png')
    plt.clf()