import graph_search
g = graph_search.GridMap('./map0.txt')
file = open('output0.txt', 'a')
[[path, action_path],visited]=graph_search.dfs(g.init_pos , g.transition , g.is_goal, graph_search._ACTIONS)
print(path)
print(action_path)
print(visited)
file.write("BFS on map0: path        = "+str(path) + "\n")
file.write("BFS on map0: action_path = "+str(action_path) + "\n")
file.write("BFS on map0: visited     = "+str(visited) + "\n")
g.display_map(path,visited,"Project-1_1.1_DFS on map0")
file.close()

import graph_search
g = graph_search.GridMap('./map1.txt')
file = open('output1.txt', 'a')
[[path, action_path],visited]=graph_search.dfs(g.init_pos , g.transition , g.is_goal, graph_search._ACTIONS)
print(path)
print(action_path)
print(visited)
file.write("BFS on map1: path        = "+str(path) + "\n")
file.write("BFS on map1: action_path = "+str(action_path) + "\n")
file.write("BFS on map2: visited     = "+str(visited) + "\n")
g.display_map(path,visited,"Project-1_1_1.2_DFS on map1")
file.close()


import graph_search
g = graph_search.GridMap('./map2.txt')
file = open('output2.txt', 'a')
[[path, action_path],visited]=graph_search.dfs(g.init_pos , g.transition , g.is_goal, graph_search._ACTIONS)
print(path)
print(action_path)
print(visited)
file.write("BFS on map2: path        = "+str(path) + "\n")
file.write("BFS on map2: action_path = "+str(action_path) + "\n")
file.write("BFS on map2: visited     = "+str(visited) + "\n")
g.display_map(path,visited,"Project-1_1_1.3_DFS on map2")
file.close()
