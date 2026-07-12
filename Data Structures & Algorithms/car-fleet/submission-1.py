class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return 0
        if len(position) != len(speed):
            raise Error
        n = len(position)
        fleet = n

        # 1 3! 1 4 7 10
        # 4 2! 4 6 8 10

        # 4 2! 4 6 8 10 distance / velocity 
        # 1 7! 1 8 9 10
        # 0 1! 1 2 3 4 5 6 7 8 9 10
        # 7 1! 7 8 9 10
        # 4 1
        # 
        stk = []
        for pos, spd in sorted(zip(position, speed), key=lambda x: x[0], reverse=True):
            time = (target - pos) / spd
            if stk and time <= stk[-1]:
                continue
            else:
                stk.append(time)
        #print(stk)
        return len(stk)
