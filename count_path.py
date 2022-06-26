def backwards_exploration(vinputs,reach_node,cicle_counter=0,cumlist=[]):
  
  idx_endpoints_list = []
  endpoints_list = []
  for vinput in vinputs:
    if vinput[1] == reach_node:
      idx_endpoints_list.append(vinputs.index(vinput)) 
      endpoints_list.append(vinput)
  
  for endpoint in endpoints_list:
    cumlist.append(endpoint)
    #debo seguir explorando?
    if endpoint[0] != 0:
      backwards_exploration(vinputs,endpoint[0],cicle_counter=cicle_counter+1,cumlist=cumlist)
  return cumlist

def calc(vinputs):

    max_node = 0
    for endpoint in vinputs:
        if endpoint[1] > max_node:
            max_node = endpoint[1]
    print('max_node: ',max_node)
    
    total_paths = []
    #se sobre entiende que el start_node = 0
    for reach_node in range(1,max_node+1):
      cumulative_list =  backwards_exploration(vinputs,reach_node,cicle_counter=0,cumlist=[])

      #fraccionamiento de la cumulative list
      ind_paths = {}
      individual_path = []
      origin = 0
      for node in cumulative_list:
        if node[0] != 0:
          individual_path.append(node)
        else:
          individual_path.append(node)
          ind_paths[origin] = individual_path
          origin += 1
          individual_path = []
      
      #complementación de cada camino
      for kpath,vpath in ind_paths.items():
        flat_vpath = [node for path in vpath for node in path[:2]] # se aplana el vector para detectar si el camino está completo
        while reach_node not in flat_vpath: #si el camino no está completo haga esto
          lf_value = ind_paths[kpath][0][1]
          last_path = kpath - 1
          for x_node in ind_paths[last_path]:
            if x_node[0] == lf_value:                
              ind_paths[kpath] = [x_node] + ind_paths[kpath]              
              flat_vpath = [node for path in ind_paths[kpath] for node in path[:2]]
      
      #clasificación del camino más largo y de mayor peso hacia el reach_node 
      path_length = {}
      path_weight = {}
      for k,v in ind_paths.items():
        path_length[k] = len(v)
        path_weight[k] = sum([i[2] for i in v])
      
      max_lenght = [key for key, value in path_length.items() if value == max(path_length.values())]
      for idx in max_lenght:
        max_idx = 0
        max_weight = 0
        if path_weight[idx] > max_weight:
          max_weight = path_weight[idx]
          max_idx = idx
      total_paths.append((reach_node,len(ind_paths[max_idx]), max_weight, ind_paths[max_idx]))
    
    #El vertice que es alcanzado a través del mayor número de caminos
    for path in total_paths:
      vertex_more_path = []
      max_lenght = 0
      if path[1] > max_lenght:
        max_lenght = path[1]
        vertex_more_path = path

    print(f'The vertex reachable by the greatest number of paths is: {vertex_more_path[0]}')

    #paths according their cost
    print('paths according to their cost')
    print(sorted(vertex_more_path[3], key = lambda x: x[2]))

    return total_paths

if __name__ == '__main__':
    
    vinputs = [(0,1,2),(0,2,4),(0,4,-2),(0,5,1),(0,6,5),(2,3,3),(2,4,2),(3,8,-4),(4,3,5),(4,8,1),(4,7,2),(5,7,-1),(5,8,-3),(6,7,6),(7,8,2)]
    total_paths =  calc(vinputs)
    #print(total_paths)

