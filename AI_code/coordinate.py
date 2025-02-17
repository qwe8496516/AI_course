import math
import random as rd
import matplotlib.pyplot as plt
import numpy as np
import log

def generate_coordinates(num_coordinate):
    coordinates = set()

    while len(coordinates) < num_coordinate:
        coordinates.add((rd.randint(0, 1000), rd.randint(0, 1000)))

    coordinates = list(coordinates)
    log.log_coordinate_data(coordinates)

    return coordinates

def transfer_coordinate_to_cost_matrix(coordinates):
    distance_cost = [[distance_calculation(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]
    log.log_coordinate_cost(distance_cost)
    return distance_cost

def distance_calculation(coordinate1, coordinate2):
    return int(math.sqrt((coordinate1[0] - coordinate2[0]) ** 2 + (coordinate1[1] - coordinate2[1]) ** 2))

def draw_cities_best_path(algorithm, start_city, total_cost, best_path, coordinates):
    x_values, y_values = zip(*coordinates)
    plt.scatter(x_values, y_values, color='blue', label='cities')
    plt.scatter((coordinates[start_city][0]), (coordinates[start_city][1]), color='yellow', label='cities')

    for i in range(len(best_path) - 1):
        x1, y1 = coordinates[best_path[i]]
        plt.text(x1, y1, f'{i + 1}', fontsize=10, verticalalignment='bottom', horizontalalignment='left')

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.savefig(f'./images/cities.png')

    for i in range(len(best_path) - 1):
        x1, y1 = coordinates[best_path[i]]
        x2, y2 = coordinates[best_path[i + 1]]
        # dist = distance_calculation((x1, y1), (x2, y2)) 
        # mid_x = (x1 + x2) / 2
        # mid_y = (y1 + y2) / 2
        plt.plot([x1, x2], [y1, y2], color='brown')
        # plt.text(mid_x, mid_y, f'{dist}', fontsize=10, ha='center')
    
    plt.title(f'{algorithm}\nTotal Distance: {total_cost}')
    plt.savefig(f'./images/{algorithm}.png')
    plt.clf()

def draw_iteration_best_cost(iteration_costs):
    iterations = np.arange(1, len(iteration_costs) + 1)

    plt.plot(iterations, iteration_costs, color='blue', label='Cost')

    plt.xlabel('Iteration')
    plt.ylabel('Cost')
    plt.title('Iteration vs Cost Trend Line')
    plt.legend()
    plt.savefig(f'./images/ACO_iteration_cost.png')
    plt.clf()