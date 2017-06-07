import graph_search_manhattan_cross_path
file = open('output0.txt', 'a')
g = graph_search_manhattan_cross_path.GridMap('./map0.txt')
[[path, action_path],visited]=graph_search_manhattan_cross_path.a_star_search(g.init_pos ,g.goal, g.transition , g.is_goal, graph_search_manhattan_cross_path._ACTIONS_2)
print(path)
print(action_path)
print(visited)
file.write("A*- Hearsitic as Manhattan on map0: path        = "+str(path) + "\n")
file.write("A*- Hearsitic as Manhattan on map0: action_path = "+str(action_path) + "\n")
file.write("A*- Hearsitic as Manhattan on map0: visited     = "+str(visited) + "\n")
g.display_map(path,visited,"Project-1_4_4.2/4.3_A*- A*- Hearsitic as Manhattan on map0")
file.close()

import graph_search_manhattan_cross_path
file = open('output1.txt', 'a')
g = graph_search_manhattan_cross_path.GridMap('./map1.txt')
[[path, action_path],visited]=graph_search_manhattan_cross_path.a_star_search(g.init_pos ,g.goal, g.transition , g.is_goal, graph_search_manhattan_cross_path._ACTIONS_2)
print(path)
print(action_path)
print(visited)
file.write("A*- Hearsitic as Manhattan on map1: path        = "+str(path) + "\n")
file.write("A*- Hearsitic as Manhattan on map1: action_path = "+str(action_path) + "\n")
file.write("A*- Hearsitic as Manhattan on map1: visited     = "+str(visited) + "\n")
g.display_map(path,visited,"Project-1_4_4.2/4.3_A*- A*- Hearsitic as Manhattan on map0")
file.close()

import graph_search_manhattan_cross_path
file = open('output2.txt', 'a')
g = graph_search_manhattan_cross_path.GridMap('./map2.txt')
[[path, action_path],visited]=graph_search_manhattan_cross_path.a_star_search(g.init_pos ,g.goal, g.transition , g.is_goal, graph_search_manhattan_cross_path._ACTIONS_2)
print(path)
print(action_path)
print(visited)
file.write("A*- Hearsitic as Manhattan on map2: path        = "+str(path) + "\n")
file.write("A*- Hearsitic as Manhattan on map2: action_path = "+str(action_path) + "\n")
file.write("A*- Hearsitic as Manhattan on map2: visited     = "+str(visited) + "\n")
g.display_map(path,visited,"Project-1_4_4.2/4.3_A*- A*- Hearsitic as Manhattan on map0")
file.close()
