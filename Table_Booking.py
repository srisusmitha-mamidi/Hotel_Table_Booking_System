class Table_Booking:
    def __init__(self,tables):
        self.tables=tables 
    def allocate_sequentially_clubbed_tables(self,c): # Best possible table/sequential clubbing of tables is allowed as per the needs
        n=len(self.tables)
        current_sum=0
        idx1=1
        best_sum = float('inf')
        start=0
        for end in range(n):
            if self.tables[end]==-1:
                current_sum=0
                start=end+1
            else:
                current_sum += self.tables[end]   # Only sequential clubbing of tables is allowed as per the needs
                while current_sum >= c:
                    if current_sum < best_sum:
                        best_sum = current_sum
                        idx1 = start
                        idx2 = end
                    current_sum -= self.tables[start]
                    start += 1
                
        if best_sum==float('inf'):
            return False
        return [idx1+1,idx2+1]
    
    def allocate_possible_tables(self,c):
        n=len(self.tables)
        lst=[]
        summ=0
        for i in range(n):
            if self.tables[i]!=-1:
                summ+=self.tables[i]
                lst.append(i)
                if summ>=c:
                    return lst
        return False
