import heapq


class Solution:
    def longest_diverse_string(self, a, b, c):
        pq = []

        for (count, char) in (-a, 'a'), (-b, 'b'), (-c, 'c'):
            if count != 0:
                heapq.heappush(pq, (count, char))

        res = []

        while pq:
            count, char = heapq.heappop(pq)

            if len(res) > 1 and res[-1] == res[-2] == char:
                if len(pq) == 0:
                    break

                count2, char2 = heapq.heappop(pq)

                res.append(char2)

                count2 += 1
                if count2 != 0:
                    heapq.heappush(pq, (count2, char2))
            else:
                res.append(char)

                count += 1

            if count != 0:
                heapq.heappush(pq, (count, char))

        return ''.join(res)
