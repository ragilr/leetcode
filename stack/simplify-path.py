class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        ret = ''
        path = deque()
        for item in path_list:
            if item == '':
                continue
            if item == '..':
                if path:
                    path.pop()
            elif item != '.':
                path.append(item)
        # print(path)
        while path:
            ret=ret+'/'+path.popleft()
        if len(ret)==0:
            return '/'
        return ret        