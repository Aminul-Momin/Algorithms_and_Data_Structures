from random import choices

def phone_mnemonics(pnum):
    
    def _phone_mnemonics(pnum, pnum_idx):

        if pnum_idx == len(pnum):
            phone_mnemonics.append(''.join(phone_mnemonic))
            return

        for char in look_up_tbl[int(pnum[pnum_idx])]:
            phone_mnemonic[pnum_idx] = char
            _phone_mnemonics(pnum, pnum_idx+1)

    phone_mnemonic = ['']*len(pnum)
    phone_mnemonics = []
    look_up_tbl = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')
    _phone_mnemonics(pnum, 0)

    return phone_mnemonics

def _test_phone_mnemonic():
    for _ in range(1):
        pnum = choices([*range(10)], k=11)
        res = phone_mnemonics(''.join([str(i) for i in pnum]))

        print(len(res))
# ==============================================================

if __name__ == "__main__":
    _test_phone_mnemonic()
