from collections import defaultdict
class TimeMap:

    def __init__(self):
        # Create a dict and initialize it with lists
        self.ds = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Adding the (timestamp, value) tuple in the list of 'key'
        self.ds[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Initializa the final result with empty, this will be returned in case
        # no solution is found
        result = ""

        # Initialize the left and right pointers
        l, r = 0, len(self.ds[key]) - 1

        # As long as l is less than or equal to r continue the search
        # making it '<=' makes sure that we are inspecting the last item as well
        while l <= r:

            # Calculate the mid pointer
            # Usign offset with the left pointer ensures we are not overflowing
            # in case the subtraction result becomes too long
            m = l + (r - l)//2

            # If there is a matching timestamp, return the value associated with it
            if self.ds[key][m][0] == timestamp:
                return self.ds[key][m][1]
            
            # Else if the timestamp is less than timestamp we are looking for,
            # store that as a potential result and keep searching for lower timestamp
            # that still makes the given timestamp bigger
            elif self.ds[key][m][0] < timestamp:
                result = self.ds[key][m][1]
                l = m + 1

            # If the timestamp is not less than the given timestamp, look for
            # smaller timestamps. 
            else:
                r = m - 1
        
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)