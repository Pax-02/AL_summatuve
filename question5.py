
graph={

    '1/s': {'2':24,'3':3,'4':20},
    '2': {'1/s':24},
    '3': {'4':12},
    '4': {'3':12}

}
# The function that takes in the graph, the starting node and the end node and determine the shortest path
def shortestReach(graph,start,end):
    # dictionary that stores the shortest path to the node
    shortest_distance={}
    # keep the track to the node
    track_predeccessor={}
    # This will help us to iterate in the graph
    unvisited_nodes=graph
    # The value of infinity that other nodes except the starting node will be having at the start
    infinity=999999

    track_path=[]

    # giving all the nodes the value of infinity except the starting
    for node in unvisited_nodes:
        shortest_distance[node]=infinity
    shortest_distance[start]=0

        # A while loop to loop through all graph vertices
    while unvisited_nodes:
        # a variable to check the minimim distance, starting not knowm
        min_distance_node=None
        for node in unvisited_nodes:
            if min_distance_node is None:
                min_distance_node=node
            elif shortest_distance[node]<shortest_distance[min_distance_node]:
                min_distance_node=node
        # the way to see all the nodes that has a connection
        path_options=graph[min_distance_node].items()
        # now moving to the child paths and also updating the route if it is more optimal
        for child_node,weight in path_options:
            if weight+shortest_distance[min_distance_node]< shortest_distance[child_node]:
                shortest_distance[child_node]=weight+shortest_distance[min_distance_node]
                track_predeccessor[child_node]=min_distance_node
        # Removing the visited node to ensure that it doesn't continue to loop to the ones it has visited
        unvisited_nodes.pop(min_distance_node)

    # Tracing it back
    current_node=end

    while current_node!=start:
        try:
            track_path.insert(0,current_node)
            current_node=track_predeccessor[current_node]

        except keyError:
            print("No path from the node")
            break

    track_path.insert(0,start)

    if shortest_distance!=infinity:
        print("The shortest path from " +start+" to "+end+" is "+str(track_path)+" : "+str(shortest_distance[end]))


shortestReach(graph,'1/s','2')
# shortestReach(graph,'1/s','4')
# shortestReach(graph,'1/s','3')