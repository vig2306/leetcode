class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
                            
        def oppositeSigns(x, y): 
            return ((x ^ y) < 0); 

        stack = []
        for i in range(len(asteroids)):
            curr = asteroids[i]

            while True:
                if len(stack) == 0:
                    stack.append(curr)
                    break
                else:
                    # print(stack)
                    top = stack.pop()
                    curr = asteroids[i]
                    if not oppositeSigns(top, curr):
                        stack.append(top)
                        stack.append(curr)
                        break
                    else:
                        if curr > 0 and top < 0:
                            stack.append(top)
                            stack.append(curr)
                            break
                        if abs(curr) > abs(top):
                            continue
                        elif abs(curr) < abs(top):
                            stack.append(top)
                            break
                        else:
                            break
             
        return stack


        