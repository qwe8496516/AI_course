import coordinate

def dynamic_programming(start_city, coordinates):
    distance_cost = coordinate.transfer_coordinate_to_cost_matrix(coordinates)
    num_cities = len(distance_cost)
    all_cities = [i for i in range(num_cities)]
    unvisited_cities = all_cities.copy()
    unvisited_cities.remove(start_city)
    dp = dict()
    path = dict()

    def tsp(current_city, cities_to_visit):
        cities_to_visit_t = (current_city, tuple(sorted(cities_to_visit)))
        if cities_to_visit_t in dp:
            # print(current_city, cities_to_visit)
            return dp[cities_to_visit_t]
        
        if not cities_to_visit:
            cost = distance_cost[current_city][start_city]
            dp[cities_to_visit_t] = cost
            return cost
        
        min_cost = float('inf')
        min_cost_path = None
        for next_city in cities_to_visit:
            remaining_cities = cities_to_visit.copy()
            remaining_cities.remove(next_city)
            cost = distance_cost[current_city][next_city] + tsp(next_city, remaining_cities)
            
            if cost < min_cost:
                min_cost = cost
                min_cost_path = next_city

        dp[cities_to_visit_t] = min_cost
        path[cities_to_visit_t] = min_cost_path
        # print(current_city, cities_to_visit, min_cost)
        return min_cost

    def get_best_path(start_city, unvisited_cities):
        best_path = [start_city]
        current_city = start_city
        cities_to_visit = unvisited_cities.copy()
        while cities_to_visit:
            next_city = path[(current_city, tuple(cities_to_visit))]
            best_path.append(next_city)
            cities_to_visit.remove(next_city)
            current_city = next_city

        best_path.append(start_city)
        return best_path
    
    min_cost = tsp(start_city, unvisited_cities)
    best_path = get_best_path(start_city, unvisited_cities)
    return min_cost, best_path