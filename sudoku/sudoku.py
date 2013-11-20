

def test(squares, unitlist, units, peers):
    "A set of unit test"
    assert len(squares) == 81
    assert len(unitlist) == 27
    assert all(len(units[s]) == 3 for s in squares)
    assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                           ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])
    print " ------ all pass ------- "


def cross(A, B):
    "Cross product of elements in A and elements in B"
    return [a + b for a in A for b in B]


def setup_sudoku():
    digits = '123456789'
    rows = 'ABCDEFGHI'
    cols = digits
    squares = cross(rows, digits)

    unit_list = ([cross(rows, c) for c in cols] +
                 [cross(r, cols) for r in rows] +
                 [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
    units = dict((s, [u for u in unit_list if s in u])
                 for s in squares)

    peers = dict((s, set(sum(units[s], [])) - set([s]))
                 for s in squares)
    return squares, unit_list, units, peers


def main():
    squares, unitlist, units, peers = setup_sudoku()
    test(squares, unitlist, units, peers)


if __name__ == '__main__':
    main()
