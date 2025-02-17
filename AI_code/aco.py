import random
import coordinate

def ant_colony_optimization(alpha, beta, evaporation_rate, quality_factor, iterations, start_city, coordinates):
    total_times = 0
    distance_cost = coordinate.transfer_coordinate_to_cost_matrix(coordinates)
    num_ants = len(distance_cost)
    num_cities = len(distance_cost)
    pheromone_matrix = [[0 if i == j else 1 for j in range(num_cities)] for i in range(num_cities)]
    iteration_best_cost = []
    best_path = []
    min_cost = float('inf')

    for i in range(iterations):
        ant_paths = []
        ant_distances = []

        for ant_No in range(num_ants):
            init_city = ant_No
            ant_path = [init_city]
            ant_distance = 0
            current_city = init_city
            unvisited_cities = [city for city in range(num_cities)]
            unvisited_cities.remove(init_city)

            while unvisited_cities:
                probabilities = []
                for city in unvisited_cities:
                    if distance_cost[current_city][city] == 0:
                        continue
                    
                    distance = distance_cost[current_city][city]
                    pheromone = pheromone_matrix[current_city][city]
                    probability = (pheromone ** alpha) * ((1 / distance) ** beta)
                    probabilities.append((city, probability))

                total_probability = sum(probability for _,probability in probabilities)

                if total_probability == 0:
                    break

                for city, probability in probabilities:
                    probability = round(probability / total_probability, 2)
                    # print(probability)
            
                next_city = random.choices([city for city, _ in probabilities], [probability for _, probability in probabilities])[0]
                ant_path.append(next_city)
                ant_distance += distance_cost[current_city][next_city]
                current_city = next_city
                unvisited_cities.remove(next_city)

            ant_distance += distance_cost[next_city][init_city]

            if ant_distance < min_cost:
                min_cost = ant_distance
                best_path = ant_path

            ant_paths.append(ant_path)
            ant_distances.append(ant_distance)

        for i in range(num_cities):
            for j in range(num_cities):
                pheromone_matrix[i][j] = pheromone_matrix[i][j] * (1 - evaporation_rate)

        for ant_path, ant_distance in zip(ant_paths, ant_distances):
            for i in range(len(ant_path) - 1):
                pheromone_matrix[ant_path[i]][ant_path[i+1]] += quality_factor / ant_distance
                pheromone_matrix[ant_path[i+1]][ant_path[i]] += quality_factor / ant_distance

        # print(ant_paths)
        # print(ant_distances)
        iteration_best_cost.append(min(ant_distances))

        if (is_all_same_element(ant_distances)):
            total_times += 1

        if total_times == 10:
            break
    
    # print('best_path:', best_path)
    s_index = best_path.index(start_city)
    best_path = best_path[s_index:] + best_path[:s_index] + [start_city]
    if best_path[-2] < best_path[1]:
        best_path.reverse()

    # print(pheromone_matrix)
    return min_cost, best_path, iteration_best_cost

def is_all_same_element(ant_distances):
    return all(x == ant_distances[0] for x in ant_distances)