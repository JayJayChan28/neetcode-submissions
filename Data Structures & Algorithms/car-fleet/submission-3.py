class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #zip posititon and speed into a tuple
        #sort position based on descending order so that cars dont pass
        #intitilize stack then iterate each car:
        #calculate the time to reach end, if that time is < the top of the stack
        #then we want to just not add anyhting to stack since that wil
        #represent the speed of the car since the faster car will combine into one fleet of the slower car in front
        #if the time is greater then the top stack, that means it will never reach the car in front, then we add the car into the top of the stack

        tuple_cars = [(p, s) for p, s in zip(position, speed)] #store tuple of each respective car position and speed
        stack = [] #stack
        tuple_cars = sorted(tuple_cars, reverse = True)
        print(tuple_cars)

        for car in tuple_cars:
            time_to_end = float((target - car[0]))/ float(car[1]) #calculate the time to reach end
            print(time_to_end)
            if not stack or time_to_end > stack[-1]: #accounts for edge case when stack is empty 
                stack.append(time_to_end) 
            elif time_to_end <= stack[-1]:
                continue
        return len(stack)
            
            
