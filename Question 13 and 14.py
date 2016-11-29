class Graph():        #Creates the graph strucure
        
        def add_vertex(graph,vertex):       #Function takes graph and new node
            if vertex in graph:
                print("Node already in graph")
                return True                     #First Conditional checks if node already exists
            elif type(vertex) != str :
                raise TypeError("Node entered needs to be of type string") #Second conditional checks if node is the correct type
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
                raise KeyError("You have called node " + str(vertex) + " which is not in the graph")
                return False                                                                    #Second conditional returns false and a message stating the input node isnt in the graph

        def Output_Nodes():
                print(sorted(graph))    #Outputs the just the nodes of the graph

        def Output_Graph():
                print(graph)            #Outputs the entire graph with nodes and connections

        def DFS(graph,start_node):
                stack = []
                global DFS_pathway      #Temporary stack to hold elements
                DFS_pathway = []            #List contains the final path of elements 
                stack.append(start_node) #Start node is added to the temporary stack
                while stack:
                        edge = stack.pop() #Conitional runs while stack is not empty 
                        if edge not in DFS_pathway:
                                DFS_pathway.extend(edge)    #Each time a new node is visited it is removed from the stack and appended to the pathway list 
                                stack = stack + graph[edge]                                                             #Until all nodes have been visited and the stack is empyu
                                f = open("dfsFile.txt","w")
                                f.write("DFS list " + repr(DFS_pathway))                #Repr converts the list of nodes to a string for the text file
                                f.close()
     
                return DFS_pathway  #Returns the DFS route as a list of nodes
                
        

        def BFS(graph,start_node):
                stack = []
                global BFS_pathway
                BFS_pathway = []
                stack.append(start_node)
                while stack:
                        edge = stack.pop(0)                     #Checks first element in the temporary stack has any more neighbours before appending to the pathway
                        if edge not in BFS_pathway:
                                BFS_pathway.extend(edge)
                                stack = stack + graph[edge]
                                f = open("bfsFile.txt","w")
                                f.write("BFS list " + repr(BFS_pathway))                #Repr converts the list of nodes to a string for the text file
                                f.close()
                return BFS_pathway
                
     
                
                
                                 
                

        

graph = {"A": ["B","J"], "B": ["A","C","F"], "C":["B","D","H"], "D":["C","E"], "E":["D","F"], "F":["B","E","G"], "G":["F","H"],  "H":["C","G","I"], "I":["H","J"], "J":["I","A"]}
weighted_graph = {"A":{"B":1,"J":2}, "B": {"A":1,"C":4,"F":3}, "C": {"B":4, "D":2,"H":4}, "D":{"C":2,"E":3}, "E":{"D":3,"F":2}, "F":{"B":3,"E":2,"G":1}, "G":{"F":1,"H":5}, "H":{"C":4,"G":5,"I":2}, "I":{"H":2, "I":3}, "J":{"I":3,"A":2}}
#print(Graph.add_vertex(graph,"L"))
#print(Graph.edge_connect(graph,"A","B"))
#print(Graph.Output_Nodes())
#print(Graph.Output_Graph())
#print(Graph.DPS(graph,"A"))
#print(Graph.BPS(graph,"A"))
#print (Graph.DJK(graph,"A"))
#print (Graph.shortest(graph,"A","I"))
