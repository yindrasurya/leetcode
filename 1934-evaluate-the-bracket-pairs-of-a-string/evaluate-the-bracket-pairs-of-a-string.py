class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        kb = dict(knowledge)
        return  ''.join(
            s1 + ("" if not s2 else kb.get(s2, '?'))
            for ss in s.split(")")  for s1,_,s2 in [ss.partition("(")]
        )