import dp
import aco
import coordinate
import compare

if __name__ == '__main__':

    # #instance 1  (4 cities)
    # distance_cost = [
    #     [0, 10, 15, 20],
    #     [10, 0, 35, 25],
    #     [15, 35, 0, 30],
    #     [20, 25, 30, 0]
    # ]
    # #answer: 80

    # #instance 2 (6 cities)
    # distance_cost = [
    #     [0,  64,  378, 519, 434, 200],
    #     [64,  0,  318, 455, 375, 164],
    #     [378, 318, 0,  170, 265, 344],
    #     [519, 455, 170, 0,  223, 428],
    #     [434, 375, 265, 223, 0,  273],
    #     [200, 164, 344, 428, 273, 0]
    # ]
    # #answer: 1248

    # #instance 3 (11 cities)
    # distance_cost = [
    #     [0, 29, 20, 21, 16, 31, 100, 12, 4, 31, 18],
    #     [29, 0, 15, 29, 28, 40, 72, 21, 29, 41, 12],
    #     [20, 15, 0, 15, 14, 25, 81, 9, 23, 27, 13],
    #     [21, 29, 15, 0, 4, 12, 92, 12, 25, 13, 25],
    #     [16, 28, 14, 4, 0, 16, 94, 9, 20, 16, 22],
    #     [31, 40, 25, 12, 16, 0, 95, 24, 36, 3, 37],
    #     [100, 72, 81, 92, 94, 95, 0, 90, 101, 99, 84],
    #     [12, 21, 9, 12, 9, 24, 90, 0, 15, 25, 13],
    #     [4, 29, 23, 25, 20, 36, 101, 15, 0, 35, 18],
    #     [31, 41, 27, 13, 16, 3, 99, 25, 35, 0, 38],
    #     [18, 12, 13, 25, 22, 37, 84, 13, 18, 38, 0]
    # ]
    # #answer: 253

    # #instance 4 (13 cities)
    # distance_cost = [
    #     [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
    #     [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
    #     [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
    #     [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
    #     [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
    #     [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
    #     [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
    #     [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
    #     [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
    #     [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
    #     [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
    #     [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
    #     [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0],
    # ]
    # #answer: 7293

    # #instance 4 (15 cities)
    # distance_cost = [
    #     [-1, 141, 134, 152, 173, 289, 326, 329, 285, 401, 388, 366, 343, 305, 276],
    #     [141, -1, 152, 150, 153, 312, 354, 313, 249, 324, 300, 272, 247, 201, 176],
    #     [134, 152, -1, 24, 48, 168, 210, 197, 153, 280, 272, 257, 237, 210, 181],
    #     [152, 150, 24, -1, 24, 163, 206, 182, 133, 257, 248, 233, 214, 187, 158],
    #     [173, 153, 48, 24, -1, 160, 203, 167, 114, 234, 225, 210, 190, 165, 137],
    #     [289, 312, 168, 163, 160, -1, 43, 90, 124, 250, 264, 270, 264, 267, 249],
    #     [326, 354, 210, 206, 203, 43, -1, 108, 157, 271, 290, 299, 295, 303, 287],
    #     [329, 313, 197, 182, 167, 90, 108, -1, 70, 164, 183, 195, 194, 210, 201],
    #     [285, 249, 153, 133, 114, 124, 157, 70, -1, 141, 147, 148, 140, 147, 134],
    #     [401, 324, 280, 257, 234, 250, 271, 164, 141, -1, 36, 67, 88, 134, 150],
    #     [388, 300, 272, 248, 225, 264, 290, 183, 147, 36, -1, 33, 57, 104, 124],
    #     [366, 272, 257, 233, 210, 270, 299, 195, 148, 67, 33, -1, 26, 73, 96],
    #     [343, 247, 237, 214, 190, 264, 295, 194, 140, 88, 57, 26, -1, 48, 71],
    #     [305, 201, 210, 187, 165, 267, 303, 210, 147, 134, 104, 73, 48, -1, 30],
    #     [276, 176, 181, 158, 137, 249, 287, 201, 134, 150, 124, 96, 71, 30, -1]
    # ]
    # #answer: 1194

    # #instance 5 (20 cities)
    # distance_cost = [
    #     [0, 56, 31, 87, 43, 65, 29, 74, 52, 69, 38, 94, 23, 81, 47, 66, 58, 77, 35, 92],
    #     [56, 0, 45, 68, 52, 73, 41, 85, 61, 78, 49, 90, 36, 88, 53, 70, 63, 82, 39, 95],
    #     [31, 45, 0, 57, 37, 50, 28, 64, 42, 60, 30, 80, 22, 75, 34, 55, 48, 67, 26, 83],
    #     [87, 68, 57, 0, 74, 95, 63, 98, 82, 99, 71, 92, 58, 90, 77, 85, 78, 97, 65, 100],
    #     [43, 52, 37, 74, 0, 59, 39, 79, 50, 66, 42, 88, 30, 82, 46, 68, 60, 79, 36, 91],
    #     [65, 73, 50, 95, 59, 0, 54, 90, 67, 85, 55, 99, 46, 97, 61, 80, 72, 91, 49, 100],
    #     [29, 41, 28, 63, 39, 54, 0, 71, 45, 62, 34, 83, 24, 78, 31, 53, 46, 65, 25, 81],
    #     [74, 85, 64, 98, 79, 90, 71, 0, 86, 99, 73, 95, 69, 94, 80, 92, 84, 100, 72, 100],
    #     [52, 61, 42, 82, 50, 67, 45, 86, 0, 75, 49, 91, 36, 88, 53, 72, 64, 83, 40, 96],
    #     [69, 78, 60, 99, 66, 85, 62, 99, 75, 0, 71, 98, 58, 95, 77, 86, 79, 98, 66, 100],
    #     [38, 49, 30, 71, 42, 55, 34, 73, 49, 71, 0, 85, 28, 81, 45, 64, 57, 76, 35, 90],
    #     [94, 90, 80, 92, 88, 99, 83, 95, 91, 98, 85, 0, 78, 96, 89, 100, 92, 100, 86, 100],
    #     [23, 36, 22, 58, 30, 46, 24, 69, 36, 58, 28, 78, 0, 74, 32, 52, 44, 63, 21, 80],
    #     [81, 88, 75, 90, 82, 97, 78, 94, 88, 95, 81, 96, 74, 0, 85, 97, 89, 100, 77, 100],
    #     [47, 53, 34, 77, 46, 61, 31, 80, 53, 77, 45, 89, 32, 85, 0, 69, 61, 80, 37, 93],
    #     [66, 70, 55, 85, 68, 80, 53, 92, 72, 86, 64, 100, 52, 97, 69, 0, 73, 92, 60, 99],
    #     [58, 63, 48, 78, 60, 72, 46, 84, 64, 79, 57, 92, 44, 89, 61, 73, 0, 84, 53, 96],
    #     [77, 82, 67, 97, 79, 91, 65, 100, 83, 98, 76, 100, 63, 100, 80, 92, 84, 0, 72, 100],
    #     [35, 39, 26, 65, 36, 49, 25, 72, 40, 66, 35, 86, 21, 77, 37, 60, 53, 72, 0, 88],
    #     [92, 95, 83, 100, 91, 100, 81, 100, 96, 100, 90, 100, 80, 100, 93, 99, 96, 100, 88, 0]
    # ]
    # #answer: 1232
    # #[0, 6, 14, 2, 10, 5, 4, 9, 15, 16, 17, 19, 11, 7, 13, 3, 1, 18, 8, 12, 0]

    start_city = 0
    # num_coordinate = 5
    # coordinates = coordinate.generate_coordinates(num_coordinate)

    coordinates = [
        (70, 42),
        (48, 40),
        (2, 58),
        (46, 12),
        (76, 15)
    ]

    alpha = 1
    beta = 1
    evaporation_rate = 0.5
    quality_factor = 100
    iterations = 1000

    min_cost, best_path, iteration_costs = aco.ant_colony_optimization(alpha, beta, evaporation_rate, quality_factor, iterations, start_city, coordinates)
    print('TSP using ACO result:')
    print("Min cost :", min_cost)
    print("Best path :", best_path)
    coordinate.draw_cities_best_path('Ant Colony Optimization', start_city, min_cost, best_path, coordinates)
    coordinate.draw_iteration_best_cost(iteration_costs)

    min_cost, best_path = dp.dynamic_programming(start_city, coordinates)
    print('TSP using Dynamic Programming result:')
    print("Min cost :", min_cost)
    print("Best path :", best_path)
    coordinate.draw_cities_best_path('Dynamic Programming', start_city, min_cost, best_path, coordinates)

    # compare.comparison_algorithm()