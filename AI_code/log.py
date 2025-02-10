def log_coordinate_data(coordinates):
    f = open('./data/coordinates.txt', 'w')
    for coordinate in coordinates:
        f.write(f'({coordinate[0]}, {coordinate[1]})\n')
    f.close()

def log_coordinate_cost(distance_cost):
    f = open('./data/distance_matrix.txt', 'w')
    for row in distance_cost:
        f.write(f'{row}\n')
    f.close()