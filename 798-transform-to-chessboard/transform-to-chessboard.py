class Solution:
    def check_even(self, count) : 
        if len(count) != 2 or sorted(count.values()) != self.balanced : 
            return -1 
        return 1

    def all_opposite(self, line1, line2) : 
        if not all (line1_value ^ line2_value for line1_value, line2_value in zip(line1, line2)) : 
            return -1 
        return 1 
    
    def set_sums_of_lists_of_values(self) : 
        self.sums_of_lists_of_values = [sum(list_of_values) for list_of_values in self.lists_of_values]

    def update_number_of_swaps(self) : 
        self.number_of_swaps += min(self.sums_of_lists_of_values) // 2

    def set_lists_of_values(self, line1) : 
        self.lists_of_values = []
        for start in self.starts : 
            new_list = []
            for index, value in enumerate(line1, start) : 
                new_list.append((index-value) % 2)
            self.lists_of_values.append(new_list)

    def set_starting_values(self, line1) : 
        self.starts = [+(line1.count(1) * 2 > self.n)] if self.n & 1 else [0, 1]

    def process_line(self, line1) : 
        self.set_starting_values(line1)
        self.set_lists_of_values(line1) 
        self.set_sums_of_lists_of_values()
        self.update_number_of_swaps()

    def process_board(self, board) : 
        for count in (collections.Counter(map(tuple, board)), collections.Counter(zip(*board))) :  
            if self.check_even(count) == -1 : 
                return -1 
            line1, line2 = count
            if self.all_opposite(line1, line2) == -1 : 
                return -1 
            self.process_line(line1)
        return self.number_of_swaps

    def set_up_for_processing_board(self, n) : 
        self.n = n 
        self.number_of_swaps = 0
        self.balanced = [n//2, (n+1)//2]
            
    def movesToChessboard(self, board: List[List[int]]) -> int:
        self.set_up_for_processing_board(len(board))
        return self.process_board(board)