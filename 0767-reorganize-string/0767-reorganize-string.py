import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Max heap
        heap = []
        for ch in freq:
            heapq.heappush(heap, (-freq[ch], ch))

        result = []
        prev_count = 0
        prev_char = ""

        while heap:
            count, ch = heapq.heappop(heap)

            result.append(ch)
            count += 1 

           
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            prev_count = count
            prev_char = ch

        return "".join(result) if len(result) == len(s) else ""
        