class Hanoi:
    f = open("hanoi.txt","w")
    
    def __init__(self, n):
        self.disks_no = n
        self.towers = (
            list(range(2*n, 1 , -2)),
            [],
            []
        )
    
    def move(self, source, destination):
        disk = self.towers[source].pop()
        self.towers[destination].append(disk)
    
    def print_tower_row(self, tower, index):
        try:
            return ("=" * tower[index]).center(20)
        except:
            return "||".center(20)
    
    def print_hanoi(self):
        tower_empty = 2
        tower_width = 20
    
        for i in range(tower_empty):
            print(
                "||".center(tower_width),
                "||".center(tower_width),
                "||".center(tower_width))
            self.f.write("||".center(tower_width)+" "+"||".center(tower_width)+" "+"||".center(tower_width))
            
        for i in range(self.disks_no, 0, -1):
            print(
                self.print_tower_row( self.towers[0], i - 1 ),
                self.print_tower_row( self.towers[1], i - 1 ),
                self.print_tower_row( self.towers[2], i - 1 )
            )
            # self.f.writelines(
            #     (
            #         self.print_tower_row( self.towers[0], i - 1 ),
            #         self.print_tower_row( self.towers[1], i - 1 ),
            #         self.print_tower_row( self.towers[2], i - 1 )
            #     )
            # )
        print(
                '-' * tower_width,
                '-' * tower_width,
                '-' * tower_width
            )
        # self.f.writelines(
        #         (
        #             '-' * tower_width,
        #             '-' * tower_width,
        #             '-' * tower_width
        #         )
        #     )
        
        print(
            "Tower #0".center(tower_width),
            "Tower #1".center(tower_width),
            "Tower #2".center(tower_width)
        )
        # self.f.writelines(
        #     (
        #         "Tower #0".center(tower_width),
        #         "Tower #1".center(tower_width),
        #         "Tower #2".center(tower_width)
        #     )
        # )
        print("#"*70)
        self.f.writelines("#"*70)
       
        
    def solve_helper(self, n, src, aux, dst):
        if n > 0 :
            self.solve_helper(n-1, src, dst, aux)
            self.move(src, dst)
            self.print_hanoi()
            self.solve_helper(n-1, aux, src, dst)
        
    def solve(self):
        self.solve_helper(self.disks_no, 0, 1, 2)
        self.f.close()

hanoi1 = Hanoi(6)
hanoi1.solve()