    # median of window size k
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]: 
        low_heap, high_heap = [], []
        for i in range(k):
            if len(low_heap) == len(high_heap):
                heapq.heappush(high_heap, -heapq.heappushpop(low_heap, -nums[i]))
            else:
                heapq.heappush(low_heap, -heapq.heappushpop(high_heap, nums[i]))
        
        ans = [high_heap[0]] if k % 2 else [(high_heap[0] - low_heap[0])/2]
        del_nums_map = defaultdict(int)
        for i in range(k, len(nums)):
            heapq.heappush(low_heap, -heapq.heappushpop(high_heap, nums[i]))
            del_num = nums[i-k]
            if del_num > -low_heap[0]:
                heapq.heappush(high_heap, -heapq.heappop(low_heap))
            del_nums_map[del_num] += 1
            while low_heap and -low_heap[0] in del_nums_map:
                n = heapq.heappop(low_heap)
                del_nums_map[-n] -= 1
                if del_nums_map[-n] == 0: del del_nums_map[-n]
            while high_heap and high_heap[0] in del_nums_map:
                n = heapq.heappop(high_heap)
                del_nums_map[n] -= 1
                if del_nums_map[n] == 0: del del_nums_map[n]
            ans.append(high_heap[0])
            else: ans.append((high_heap[0] - low_heap[0])/2)
        return ans    

    # cost to make all elements in the window equal to the median
    def medianCostSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        low_heap, high_heap = [], []
        sum_low, sum_high = 0, 0
        for i in range(k):
            if len(low_heap) == len(high_heap):
                heapq.heappush(low_heap, -nums[i])
                sum_low += nums[i]
                x = -heapq.heappop(low_heap)
                sum_low -= x
                heapq.heappush(high_heap, x)
                sum_high += x
            else:
                heapq.heappush(high_heap, nums[i])
                sum_high += nums[i]
                x = heapq.heappop(high_heap)
                sum_high -= x
                heapq.heappush(low_heap, -x)
                sum_low += x
        ans = []
        if k & 1:
            cost = sum_high - sum_low - high_heap[0]
        else:
            cost = sum_high - sum_low
        ans.append(cost)
        del_nums = defaultdict(int)
        for i in range(k, len(nums)):
            x = heapq.heappushpop(high_heap, nums[i])
            sum_high += nums[i] - x
            heapq.heappush(low_heap, -x)
            sum_low += x
            del_num = nums[i - k]
            if high_heap and del_num > -low_heap[0]:
                sum_high -= del_num
                y = -heapq.heappop(low_heap)
                sum_low -= y
                heapq.heappush(high_heap, y)
                sum_high += y
                del_nums[del_num] += 1
            else:
                sum_low -= del_num
                del_nums[del_num] += 1
            while low_heap and del_nums.get(-low_heap[0], 0) > 0:
                n = -heapq.heappop(low_heap)
                del_nums[n] -= 1
                if del_nums[n] == 0:
                    del del_nums[n]
            while high_heap and del_nums.get(high_heap[0], 0) > 0:
                n = heapq.heappop(high_heap)
                del_nums[n] -= 1
                if del_nums[n] == 0:
                    del del_nums[n]
            if k & 1:
                cost = sum_high - sum_low - high_heap[0]
            else:
                cost = sum_high - sum_low
            ans.append(cost)
        return ans