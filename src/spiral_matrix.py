class SpiralMatrix:
    def traverse_spiral_matrix(self, matrix):
        traversed  = 0
        row  = 0
        column = 0
        column_seen = {}
        row_seen = {}
        row_matrix = len(matrix)
        column_matrix = len(matrix[0])
        result = []
        while traversed != row_matrix * column_matrix:
            ## move right
            while column <= column_matrix - 1 and not column_seen.get(column)\
                    and traversed != row_matrix * column_matrix:
                result.append(matrix[row][column])
                column += 1
                traversed += 1
            row_seen[row] = 1
            row += 1
            column -=1
            ## move down
            while row <= row_matrix - 1 and not row_seen.get(row) and traversed != row_matrix * column_matrix:
                result.append(matrix[row][column])
                row += 1
                traversed += 1
            column_seen[column] = 1
            column -=1
            row -=1
            ## move left
            while column >= 0 and not column_seen.get(column) \
                    and traversed != row_matrix * column_matrix:
                result.append(matrix[row][column])
                column -= 1
                traversed += 1
            row_seen[row] = 1
            row -=1
            column += 1
            ## move up
            while row >= 0 and not row_seen.get(row) and traversed != row_matrix * column_matrix:
                result.append(matrix[row][column])
                row -= 1
                traversed += 1
            column_seen[column] = 1
            column +=1
            row += 1
        return result

if __name__ == '__main__':
    spiral_matrix= SpiralMatrix()
    spiral_matrix.traverse_spiral_matrix(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9,10,11,12]
        ]
    )





[1,2,3,4,8,12,11,10,9,5,6,7]