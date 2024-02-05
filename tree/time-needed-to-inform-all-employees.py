class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        reportees = {}
        # print(manager)
        for i,m in enumerate(manager):
            if m in reportees:
                reportees[m].append(i)
            else:
                reportees[m] = [i]
        informed = set()
        informed.add(headID)
        q = deque()
        q.append((headID,0))
        # print(reportees)
        mt = float('-inf')
        # print(reportees)
        while q:
                emp,time = q.popleft()
                # print(emp,time)
                time+=informTime[emp]
                mt = max(mt,time)
                if emp in reportees:
                    for e in reportees[emp]:
                        q.append((e,time))
            # print(q,time)
        return mt