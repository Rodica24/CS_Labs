def des_round(Lk_minus_1, S_box_output):

    def permutation(P_table, data):
        return ''.join(data[i - 1] for i in P_table)

    P_table = [
        16, 7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        2, 8, 24, 14,
        32, 27, 3, 9,
        19, 13, 30, 6,
        22, 11, 4, 25
    ]

    permutated_output = permutation(P_table, S_box_output)

    Ri = ''.join('0' if bit1 == bit2 else '1' for bit1, bit2 in zip(Lk_minus_1, permutated_output))

    return Ri

Lk_minus_1 = '11001100000000001100110011111111'
S_box_output = '01011100100000101011010110010111'

Ri = des_round(Lk_minus_1, S_box_output)
print(f"Ri: {Ri}")