class Solution:
    def trap(self, height):
        if len(height) < 3:
            return []
        my_trap = []
        start_step = 0
        while start_step <= len(height) - 3:
            if height[start_step] > height[start_step + 1]:
                j = start_step + 1
                trap_sequence = []
                trap_sequence.append(height[start_step])
                while j < len(height) -1 and height[j] < height[start_step]:
                    trap_sequence.append(height[j])
                    j += 1
                if height[j] >= height[start_step]:
                    trap_sequence.append(height[j])
                else:
                    trap_sequence = []
                if len(trap_sequence) > 0:
                    my_trap.append(trap_sequence)
                start_step = j
            else:
                start_step +=1
        return self.calculate(my_trap)


    def calculate(self, trap):
        trapped_water = 0
        for trap_sequence in trap:
            sum  = 0
            mark_heigh = trap_sequence[0]
            for j in trap_sequence:
                sum += max(mark_heigh - j, 0)
            trapped_water += sum
        return trapped_water
if __name__ == '__main__':

    s = Solution()
    print(s.trap([0, 2, 1, 0, 1, 2]))

