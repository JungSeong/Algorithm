class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter

        for i in range(9) :
            cnt = Counter(board[i])
            for k, v in cnt.items() :
                if k.isdigit() and v >= 2 :
                    return False
        
        bT = list(map(list, zip(*board)))
        
        for i in range(9) :
            cnt = Counter(bT[i])
            for k, v in cnt.items() :
                if k.isdigit() and v >= 2 :
                    return False

        for i in range(3) :
            sr = 3*i
            for j in range(3) :
                sc = 3*j
                arr = []

                for r in range(sr, sr+3) :
                    for c in range(sc, sc+3) :
                        arr.append(board[r][c])
                
                cnt = Counter(arr)
                for k, v in cnt.items() :
                    if k.isdigit() and v >= 2 :
                        return False

        return True
