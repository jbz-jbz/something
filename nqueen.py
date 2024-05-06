def nqueens(n):
    
    board = [['.']*n for i in range(n)]
    result = []
    
    col = set()
    positiveD = set() #r+c
    negativeD = set() #r-c
    
    def Backtracking(r):
        if r==n:
            sol = [''.join(row) for row in board]
            result.append(sol)
            return 
        
        for c in range(n):
            if c in col or (r+c) in positiveD or (r-c) in negativeD:
                continue
            
            col.add(c)
            positiveD.add(r+c)
            negativeD.add(r-c)
            board[r][c] = 'Q'
            
            Backtracking(r+1)
            
            col.remove(c)
            positiveD.remove(r+c)
            negativeD.remove(r-c)
            board[r][c] = '.'
            
    Backtracking(0)
    return result[0]
    
arr = nqueens(4)
for i in range(4):
    print(arr[i])
            
            
            
            
