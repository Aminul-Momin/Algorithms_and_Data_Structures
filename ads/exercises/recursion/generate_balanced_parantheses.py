from typing import Container
#==============================================================================
"""
Implement an algorithm to print all valid (i.e. properly opened and closed)
combinations of n-pairs of parentheses. - [CtCI: 9.6].
"""


def gen_parens(k: int) -> Container[str]:
    def _gen_parens(l, r, c, parens, result) -> None:

        # print(f'''{'_gen_parens('}{l}{', '}{r}{', '}{c}{', '}{parens}{')'}''')
        # print(f'''{'    '*c}{'_gen_parens('}{l}{', '}{r}{', '}{c}{', '}{parens}{')'}''')

        if l < 0 or r < l: return None
        if l == 0 and r == 0: result.append(''.join(parens))
        else:
            if l > 0:
                parens[c] = '('
                _gen_parens(l - 1, r, c + 1, parens, result)
            if r > l:
                parens[c] = ')'
                _gen_parens(l, r - 1, c + 1, parens, result)

    result = []
    parens = [None] * (2 * k)
    _gen_parens(k, k, 0, parens, result)
    return result


def gbp1(num_pairs: int) -> Container[str]:
    def _gbp1(l: int, r: int, valid_prefix: str, result=[]) -> Container[str]:

        # print(f'''{'_gbp1('}{l}{', '}{r}{', '}{valid_prefix}{')'}''')
        # l -> num_left_parens_needed
        # r -> num_right_parens_needed

        if l > 0:
            _gbp1(l - 1, r, valid_prefix + '(')  # able to insert '('.
        if l < r:
            _gbp1(l, r - 1, valid_prefix + ')')  # able to insert ')'.

        if not r:
            result.append(valid_prefix)
        return result

    return _gbp1(num_pairs, num_pairs, '')


def main():
    print(gen_parens(4))


if __name__ == '__main__':
    main()
