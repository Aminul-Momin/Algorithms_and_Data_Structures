from typing import Container

def gen_parens(k: int) -> Container[str]:
    
    def _gen_parens(l, r, c, parens, result) -> None:
        
        # print(f"""{'_gen_parens('}{l}{', '}{r}{', '}{c}{', '}{parens}{')'}""")
        print(f"""{'    '*c}{'_gen_parens('}{l}{', '}{r}{', '}{c}{', '}{parens}{')'}""")

        if l < 0 or r < l: return None
        if l == 0 and r == 0: result.append(''.join(parens))
        else:
            if l > 0:
                parens[c] = '('
                _gen_parens(l-1, r, c+1, parens, result)
            if r > l:
                parens[c] = ')'
                _gen_parens(l, r-1, c+1, parens, result)

    result = []
    parens = [None]*(2*k)
    _gen_parens(k, k, 0, parens, result)
    return result


def gbp1(num_pairs: int) -> Container[str]:
    def _gbp1(l: int, r: int, valid_prefix: str, result=[]) -> Container[str]:
        
        # print(f"""{'_gbp1('}{l}{', '}{r}{', '}{valid_prefix}{')'}""")
        # l -> num_left_parens_needed
        # r -> num_right_parens_needed

        if l > 0: _gbp1(l - 1, r, valid_prefix + '(')  # able to insert '('.
        if l < r: _gbp1(l, r - 1, valid_prefix + ')')  # able to insert ')'.

        if not r: result.append(valid_prefix)
        return result

    return _gbp1(num_pairs, num_pairs, '')


# Generate Balanced Parentheses
def gbp(num_pairs, num_left_open=0):
    if not num_pairs: return [')' * num_left_open]
    if not num_left_open:
        return ['(' + p for p in gbp(num_pairs - 1, num_left_open + 1)]
    else:
        L1 = ['(' + p for p in gbp(num_pairs - 1, num_left_open + 1)]
        L2 = [')' + p for p in gbp(num_pairs - 1, num_left_open - 1)]
        return (L1 + L2)




if __name__ == '__main__':
    # print(len(gen_parens(5)))
    res1 = gen_parens(3)
    res2 = gbp1(3)
    assert len(res1) == len(res2)
