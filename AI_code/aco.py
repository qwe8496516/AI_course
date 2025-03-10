import random
import coordinate
# import mlflow

def ant_colony_optimization(alpha, beta, evaporation_rate, quality_factor, iterations, start_city, coordinates):
    # mlflow.set_tracking_uri('http://140.124.181.7:5000')
    # mlflow.set_experiment('ACO')
    distance_cost = coordinate.transfer_coordinate_to_cost_matrix(coordinates)  # 座標轉換成距離矩陣
    num_ants = len(distance_cost)   # 螞蟻數量
    num_cities = len(distance_cost)   # 城市數量
    pheromone_matrix = [[0 if i == j else 1 for j in range(num_cities)] for i in range(num_cities)]   # 初始費洛蒙濃度矩陣
    iteration_best_cost = []   # 每次iteration的最短路徑長度
    best_path = []   # 最短路徑
    min_cost = float('inf')   # 最短路徑長度

    for i in range(iterations):
        # with mlflow.start_run() as run:
            ant_paths = []  # 每次iteration所有螞蟻的路徑
            ant_distances = []   # 螞蟻路徑長度

            # mlflow.log_params({ "iterations" : i })

            for ant_No in range(num_ants):
                init_city = ant_No   # 起始城市 (分配到不同初始城市)
                ant_path = [init_city]  # 加入初始城市到路徑
                ant_distance = 0    
                current_city = init_city  # 初始化當前城市
                unvisited_cities = [city for city in range(num_cities)]  # 建立所有城市的列表
                unvisited_cities.remove(init_city)  # 移除起點
                
                while unvisited_cities:
                    probabilities = []
                    # 計算未到達城市的機率
                    for city in unvisited_cities:
                        distance = distance_cost[current_city][city]    # 取得 current_city 與 city 之間的距離
                        pheromone = pheromone_matrix[current_city][city]    # 計算 current_city 到 city 的費洛蒙濃度
                        probability = (pheromone ** alpha) * ((1 / distance) ** beta)
                        probabilities.append((city, probability))

                    total_probability = sum(probability for _,probability in probabilities)

                    if total_probability == 0:
                        break

                    for city, probability in probabilities:
                        probability = round(probability / total_probability, 2)  # 計算機率 
                
                    next_city = random.choices([city for city, _ in probabilities], [probability for _, probability in probabilities])[0]   # 隨機選擇下一個城市
                    ant_path.append(next_city)   # 將下一個 city 加入路徑
                    ant_distance += distance_cost[current_city][next_city]  # 取得 current_city 與 city 之間的距離
                    current_city = next_city    # 更新 current_city
                    unvisited_cities.remove(next_city)   # 移除已經走過的城市

                ant_distance += distance_cost[next_city][init_city]  # 回到起點

                if ant_distance < min_cost:
                    min_cost = ant_distance
                    best_path = ant_path

                ant_paths.append(ant_path)
                ant_distances.append(ant_distance)

            # mlflow.log_metrics({"cost" : min_cost})

            # 更新費洛蒙濃度
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

            # if (is_all_same_element(ant_distances)):
            #     total_times += 1

            # if total_times == 10:
            #     break
    
    # print('best_path:', best_path)
    s_index = best_path.index(start_city)
    best_path = best_path[s_index:] + best_path[:s_index] + [start_city]
    if best_path[-2] < best_path[1]:
        best_path.reverse()

    # print(pheromone_matrix)
    return min_cost, best_path, iteration_best_cost

def is_all_same_element(ant_distances):
    return all(x == ant_distances[0] for x in ant_distances)