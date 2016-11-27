class Graph():        #Creates the graph strucure
        
        def add_vertex(graph,vertex):       #Function takes graph and new node
            if vertex in graph:
                print("Node already in graph")
                return True                     #First Conditional checks if node already exists
            elif type(vertex) != str :
                print("Node input needs to be of type string")   #Second conditional checks if node is the correct type
            else:
                graph[vertex] = []
                print("You added " + str(vertex) + " to the graph")
                print(graph)                                            #Third conditional adds the node to the graph if it does not exist

        

        def edge_connect(graph,vertex,connection):      #Function takes the graph and two nodes to make a connection
            new_connect = []                            #Empty variable contains new connwction
            if vertex in graph:                         
                new_connect = graph[vertex]
                graph[vertex] = new_connect + [connection]
                print(graph)                                    #First conditional checks to see if the node is in the graph and if so the new connection is added to the values list of the vertex
            else:
                print("You have called node " + str(vertex) + " which is not in the graph")
                return False                                                                    #Second conditional returns false and a message stating the input node isnt in the graph

        def Output_Nodes():
                print(sorted(graph))    #Outputs the just the nodes of the graph

        def Output_Graph():
                print(graph)            #Outputs the entire graph with nodes and connections

        def DFS(graph,start_node):
                stack = []              #Temporary stack to hold elements
                pathway = []            #Final path algorithm 
                stack.append(start_node) #Start node is added to the temporary stack
                while stack:
                        edge = stack.pop() #Conitional runs while stack is not empty 
                        if edge not in pathway:
                                pathway.extend(edge)    #Each time a new node is visited it is removed from the stack and appended to the pathway list 
                                stack = stack + graph[edge]                                                             #Until all nodes have been visited and the stack is empyu
                return pathway                                  #Returns the DFS route as a list of nodes

        def BFS(graph,start_node):
                stack = []
                pathway = []
                stack.append(start_node)
                while stack:
                        edge = stack.pop(0)
                        if edge not in pathway:
                                pathway.extend(edge)
                                stack = stack + graph[edge]
                return pathway
                                
                                 
                

        

graph = {"A": ["B","J"], "B": ["A","C","F"], "C":["B","D","H"], "D":["C","E"], "E":["D","F"], "F":["B","E","G"], "G":["F","H"],  "H":["C","G","I"], "I":["H","J"], "J":["I","A"]}
#print(Graph.add_vertex(graph,"L"))
#print(Graph.edge_connect(graph,"A","B"))
#print(Graph.Output_Nodes())
#print(Graph.Output_Graph())
#print(Graph.DPS(graph,"A"))
#print(Graph.BPS(graph,"A"))
