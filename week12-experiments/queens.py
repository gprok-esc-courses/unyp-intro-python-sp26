
class Queens:
    def __init__(self):
        self.queen_columns = [-1] * 8
        self.solutions = []

    def find_all_solutions(self):
        self.backtrack(0)
        return self.solutions

    def backtrack(self, row):
        if row == 8:        # We have a solution!
            self.solutions.append(self.queen_columns[:])
            return 
        else:
            for col in range(8):
                if self.safe_position(row, col):
                    self.queen_columns[row] = col 
                    self.backtrack(row + 1)
                    self.queen_columns[row] = -1

    def safe_position(self, row, col):
        for qrow in range(row):
            qcol = self.queen_columns[qrow]
            if qcol == col:
                return False 
            if qcol - row + qrow == col:
                return False 
            if qcol + row - qrow == col:
                return False
        return True
    
    def print_solution(self, pos):
        if pos >= len(self.solutions):
            print("Error: index out of range")
        else:
            solution = self.solutions[pos]
            for row in range(8):
                for col in range(8):
                    if solution[row] == col:
                        print('Q', end=' ')
                    else:
                        print('-', end=' ')
                print()


queens = Queens()
solutions = queens.find_all_solutions()
print(f"Solutions found: {len(solutions)}")
queens.print_solution(34)