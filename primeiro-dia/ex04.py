pointer = []
pointer = input()

P = pointer[0]
R = pointer[2]

if P == "0":
    print('C')

elif (P == "1") and (R == "0"):
    print('B')

elif (P == "1") and (R == "1"):
    print('A')

elif P != "1" or P != "0" or R != "1" or R != "0":
    print('Jogada Inválida')