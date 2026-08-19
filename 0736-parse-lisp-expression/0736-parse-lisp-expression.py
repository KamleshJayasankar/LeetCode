class Solution:
    def evaluate(self, expression: str) -> int:
        def parse_tokens(s: str) -> list[str]:
            tokens = []
            buf = []
            bal = 0
            for char in s:
                if char == '(':
                    bal += 1
                elif char == ')':
                    bal -= 1
                
                if char == ' ' and bal == 0:
                    if buf:
                        tokens.append(''.join(buf))
                        buf = []
                else:
                    buf.append(char)
            if buf:
                tokens.append(''.join(buf))
            return tokens

        def eval_expr(expr: str, scope: list[dict[str, int]]) -> int:
            
            if expr[0].isdigit() or expr[0] == '-':
                return int(expr)
            
            
            if expr[0] != '(':
                for layer in reversed(scope):
                    if expr in layer:
                        return layer[expr]
            
            inner = expr[1:-1]
            space_idx = inner.find(' ')
            op = inner[:space_idx]
            rest = inner[space_idx + 1:]
            
            tokens = parse_tokens(rest)
            
            if op == 'add':
                return eval_expr(tokens[0], scope) + eval_expr(tokens[1], scope)
            elif op == 'mult':
                return eval_expr(tokens[0], scope) * eval_expr(tokens[1], scope)
            else:  
                scope.append({})
                for i in range(0, len(tokens) - 1, 2):
                    var = tokens[i]
                    val = eval_expr(tokens[i + 1], scope)
                    scope[-1][var] = val
                
                
                res = eval_expr(tokens[-1], scope)
                scope.pop()
                return res

        return eval_expr(expression, [])