def bfs(graph,start_node):
    visited= []
    queue =[start_node]

    while queue :
        current_node =queue.pop(0)

        if current_node not in visited :
            print(f"exploring node : { current_node}")
            visited.append(current_node)

            # .get() prevent errors if a node has no outgoing edges 
            for neighbor in graph.get(current_node,[]):
                if neighbor not in visited and neighbor not in queue:
                      queue.append(neighbor)

    return visited

print("------user input section-------");
student_graph={}

num_edges=int(input("how many edges (connection) does your graph have "))
num_edges = int(input("How many edges (connections) does your graph have? "))

for i in range(num_edges):
    u = input(f"Enter starting node of edge {i+1}: ")
    v = input(f"Enter ending node of edge {i+1}: ")

    if u not in student_graph:
        student_graph[u]=[]
    if v not in student_graph :
        student_graph[v]=[] 
    student_graph[u].append(v)
    student_graph[v].append(u)

start =input("enter the starting node for bfs : ")
print(f"\n YOUR GRAPH DICTIONARY : {student_graph}")

print(f"\n Your graph dictionary : {student_graph}")
print("starting BFS Traversal....")

