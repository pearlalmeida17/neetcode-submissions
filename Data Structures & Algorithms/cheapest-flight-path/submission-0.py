class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n

        prices[src] = 0

        for _ in range(k + 1):

            temp_prices = prices.copy()

            for u, v, price in flights:

                if prices[u] == float('inf'):
                    continue
                
                temp_prices[v] = min(temp_prices[v], prices[u] + price)
                
            prices = temp_prices
        
        if prices[dst] != float('inf'):
            return prices[dst]
        else:
            return -1