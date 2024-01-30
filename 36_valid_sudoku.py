class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_sets = [set(),set(),set(),set(),set(),set(),set(),set(),set() ]
        col_sets = [set(),set(),set(),set(),set(),set(),set(),set(),set() ]
        sub_box_sets = [[set(), set(), set()],[set(), set(), set()],[set(), set(), set()]]


        for row_num in range(9):
            for col_num in range(9):
                number = board[row_num][col_num] 
                if number == ".": 
                    continue

                if number in row_sets[row_num] or number in col_sets[col_num] or number in sub_box_sets[row_num // 3][col_num // 3]:
                    return False
                row_sets[row_num].add(number)
                col_sets[col_num].add(number)
                sub_box_sets[row_num // 3][col_num // 3].add(number)
                
        return True