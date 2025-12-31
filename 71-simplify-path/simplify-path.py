class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        pathstack = []
        
        for name in path:
            match name:
                case '..':
                    if pathstack:
                        pathstack.pop()
                case '.':
                    pass
                case [*rest] if all(x=='/' for x in rest):
                    pass
                case '':
                    pass
                case _:
                    pathstack.append(name)
        
        return "/" + "/".join(pathstack)
                    