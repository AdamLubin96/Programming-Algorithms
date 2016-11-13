class mat:
    def add_matrix():
        B = [[1,2],[1,2]]
        C = [[3,4],[5,6]]
        A = [[0,0],[0,0]]

        
        for i in range(len(B)):  # iterate through rows of X
          for j in range(len(C[0])):  # iterate through columns of Y
                   A[i][j] = (B[i][j] + C[i][j]) 

        for num1 in A:
           return(A)

    def sub_matrix():
        B = [[1,2],[1,2]]
        C = [[3,4],[5,6]]
        A = [[0,0],[0,0]]

        for i in range(len(B)):  # iterate through rows of X
          for j in range(len(C[0])):  # iterate through columns of Y
                   A[i][j] = (B[i][j] - C[i][j]) 

        for num2 in A:
           return(A)
        
    def mult_matrix():
        B = [[1,2],[1,2]]
        C = [[3,4],[5,6]]
        A = [[0,0],[0,0]]

        for i in range(len(B)):  # iterate through rows of X
            for j in range(len(C[0])):  # iterate through columns of Y
              for k in range(len(C)): # iterate through rows of Y
                   A[i][j] = (B[i][j] * C[i][j]) 

        for num3 in A:
           return(A)

    def Formula():
        sum1 = (mult_matrix) - ((add_matrix ) * (add_matrix))
        return sum1

