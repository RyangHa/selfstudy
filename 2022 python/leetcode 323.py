class Solution:
    def countComponents(self,n,edges):
        count = 0
        graph = [[] for _ in range(n)]
        seen = [False for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            for adj in graph[node]:
                if not seen[adj]:
                    seen[adj] = True
                    dfs(adj)

        for i in range(n):
            if not seen[i]:
                count += 1
                seen[i] = True
                dfs(i)
        return count

s=Solution()
print(s.countComponents(5,[[0,1],[1,2],[3,4]])) #2
print(s.countComponents(5,[[0,1],[1,2],[2,3],[3,4]])) #1
print(s.countComponents(4,[[2,3],[1,2],[1,3]])) #2
print(s.countComponents(4,[[0,1],[2,3],[1,2]])) #1
print(s.countComponents(6,[[0,1],[0,2],[2,5],[3,4],[3,5]])) #1