class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pair = sorted(zip(position, speed), reverse=True)

        stack = deque()

        sorted_positions, sorted_speed = zip(*sorted_pair)

        for pos, spd in sorted_pair:
            time_i = (target - pos)/spd
            stack.append(time_i)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        