class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [(prime, 0, prime) for prime in primes]
        heapq.heapify(heap)
        
        ugly_numbers = [1]
        seen = set(ugly_numbers) 

        while len(ugly_numbers) < n:
            next_ugly, prime_index, prime_value = heapq.heappop(heap)
            
            if next_ugly not in seen:
                ugly_numbers.append(next_ugly)
                seen.add(next_ugly)
            
            # to make the size of the heap doesn't increase more than
            # the length of the heap
            while next_ugly in seen:
                prime_index += 1
                next_ugly = ugly_numbers[prime_index] * prime_value

            heapq.heappush(heap, (next_ugly, prime_index, prime_value))
      
        return ugly_numbers[-1]