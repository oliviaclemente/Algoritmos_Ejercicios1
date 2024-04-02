import time
from IPython.display import clear_output

class TowerOfHanoi():
    def __init__(self, n=4):
        self._n = n
        self._array = [[], [], list(reversed(range(n)))]
        self._lengths = [0, 0, n]
        
    def draw_towers(self):
        rows = []
        rows.append(['\t  1\t', '\t  2\t', '\t  3\t'])
        rows.append(['\t_____\t', '\t_____\t', '\t_____\t'])
        for i in range(max(self._lengths)):
            row = []
            for j in range(3):
                if i<self._lengths[j]:
                    row.append('\t  ' + str(self._array[j][i]) + '\t')
                else:
                    row.append('\t  \t')
            rows.append(row)
        
        
        for r in reversed(rows):
            print(''.join(r))
            
    def __getitem__(self, index):
        return self._array[index]
    
    def pop(self, index):
        self._lengths[index] -= 1
        return self[index].pop()
    
    
    def getlen(self):
        return self._lengths
    
    
    def __setitem__(self, index, value):
        if self[index] and self[index][-1] < value:
            raise ValueError (f'Illegal move.  Cannot place block with size {value} on block {self[index][-1]}')
        else: 
            self[index].append(value)
            self._lengths[index] += 1
    
    def _move_stack(self, n_disks, start_peg, help_peg, target_peg):
        time.sleep(0.5)
        clear_output()
        self.draw_towers()
        
        if n_disks == 1:
            self._count += 1
            value = self.pop(start_peg)
            try:
                self[target_peg] = value
            except Exception as e:
                print(e)
                self[start_peg]
        
        else:
            #Move the upper stack to the helper peg
            self._move_stack(n_disks-1, start_peg, target_peg, help_peg)
            #Move the lowest item to the target peg
            self._move_stack(1, start_peg, help_peg, target_peg)
            #Move the upper stack to the target peg
            self._move_stack(n_disks-1, help_peg, start_peg, target_peg)
            
    
    def solve_hanoi(self):
        self._count = 0
        self._move_stack(self.getlen()[2], 2, 1, 0)
        
        time.sleep(0.5)
        clear_output()
        self.draw_towers()
        
        print(f'\nThis took a total of {self._count} moves!')
        
        
            
t = TowerOfHanoi(3)
t.solve_hanoi()