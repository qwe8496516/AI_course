import coordinate

def dynamic_programming(start_city, coordinates):
    distance_cost = coordinate.transfer_coordinate_to_cost_matrix(coordinates)   # 座標轉換成距離矩陣
    num_cities = len(distance_cost)   # 城市數量
    all_cities = [i for i in range(num_cities)]   # 建立所有城市的列表
    unvisited_cities = all_cities.copy()   # 建立所有城市列表的副本
    unvisited_cities.remove(start_city)   # 移除起點
    dp = dict()  # 動態規劃字典
    path = dict()   # 記錄最佳路徑

    def tsp(current_city, cities_to_visit):
        cities_to_visit_t = (current_city, tuple(sorted(cities_to_visit)))   # 轉換成 tuple
        if cities_to_visit_t in dp:   # 如果已經計算過，直接回傳 value
            return dp[cities_to_visit_t]
        
        if not cities_to_visit:   # 如果所有城市都走過一次，回到起點
            cost = distance_cost[current_city][start_city]   # 回到起點的距離
            dp[cities_to_visit_t] = cost    # 更新動態規劃字典
            return cost
        
        min_cost = float('inf')   # 初始化最小距離成本
        min_cost_path = None    # 初始化最小距離成本的路徑
        for next_city in cities_to_visit:
            remaining_cities = cities_to_visit.copy()   # 剩餘城市副本
            remaining_cities.remove(next_city)   # 移除下一個城市
            cost = distance_cost[current_city][next_city] + tsp(next_city, remaining_cities)    # 計算成本
            
            if cost < min_cost:    # 如果成本小於最小成本
                min_cost = cost    # 更新最小成本
                min_cost_path = next_city   # 更新最小成本的路徑

        dp[cities_to_visit_t] = min_cost    # 更新動態規劃字典
        path[cities_to_visit_t] = min_cost_path    # 更新最佳路徑
        return min_cost

    def get_best_path(start_city, unvisited_cities):
        best_path = [start_city]    # 初始化最佳路徑
        current_city = start_city   # 初始化當前城市
        cities_to_visit = unvisited_cities.copy()   # 剩餘城市副本
        while cities_to_visit:
            next_city = path[(current_city, tuple(cities_to_visit))]   # 取得下一個城市
            best_path.append(next_city)   # 加入最佳路徑
            cities_to_visit.remove(next_city)   # 移除已經走過的城市
            current_city = next_city   # 更新當前城市

        best_path.append(start_city)   # 回到起點
        return best_path
    
    min_cost = tsp(start_city, unvisited_cities)    # 執行動態規劃
    best_path = get_best_path(start_city, unvisited_cities)   # 取得最佳路徑
    return min_cost, best_path