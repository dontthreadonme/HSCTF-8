import random
import time

scramble = "QQ.ap(OOOaQa.a($/FF.F/ZOZ..aQaQ/aa(a(ZZaaF.Q^FaZ,S/..(^]aF.FF.pFF-(==SFa/aOo.=/aFM/,.,Z=/aF/aQ/*<Q(^-OSZOO=a]Q](Q<].a~/ao/aYZaF=aQa]Q^FOZFsQn/^FOh.*aZ.OaaO/(Q.SZ</ QQ,a(OFaFF((QQQaQQ/^/Q.O-F(Z(=gQQ=k,OSF=F.a/]Q=Z(Qa(ao=a:ZQ/QpJ]/QQF.=FZ]QkFS^=Q:QQZQFa=.\"OS(=^Q.^Ja/(/Z^]F: ]//./.Q=F=Ya/SO/]Oas=apS=(..)(.aF/(oZ(a/~., , ZZZ/Oq=(.QF\":.|O($FZ./(]]FO]FO.Oo\"F+QO/FqY/Z-(a.=/F/aa/.=OZOFQ(=Z./pOa((O]..Q/]Q((a(]/aaSZJ.Q(*F] < //Fa/|]QFQZ(=S.ZQQZOFQa: Q/aQO=(]..a/^(QOQoF////(^kF-a-"

x = ['t', 'Y', 'w', 'V', '|', ']', 'u', 'X', '_', '0', 'P', 'k', 'h', 'D', 'A', '4', 'K', '5', 'z',
     'Z', 'G', '7', ';', 'S', ' ', '/', '6', '%', '}', '\\', ',', ':', '>', '#', 'a', '$', '3', '`',
     '+', 'R', 'b', 'H', 'd', 's', '1', 'J', 'L', 'v', '9', '2', 'o', 'M', '<', 'e', '(', 'x', '-',
     'B', 'm', "'", 'y', 'Q', '"', 'W', 'l', '.', 'i', 'O', '^', 'p', '8', 'f', 'F', 'C', '?', 'g',
     '@', 'j', '[', 'r', '!', '=', 'E', '~', '*', 'T', '{', ')', 'U', 'N', 'c', '&', 'n', 'q', 'I']

# 2021-04-15 22: 21: 48
timp = 1618514508
step = 1


def unshuffle(mesaj, timp):
    random.seed(timp)
    a = list(range(len(mesaj)))
    random.shuffle(a)
    return [mesaj[a.index(i)] for i in range(len(mesaj))]


# Asa?
# text = x
# temp = []
# for _ in range(20):
#     for d in x:
#         temp.append(chr(x.index(d) + 32))
#     text = temp
#     temp = []
# aux = [text[x.index(i)] for i in scramble]


# Sau asa
# aux = scramble
# for _ in range(20):
#     aux2 = [0] * len(scramble)
#     for i in range(len(scramble)):
#         aux2[i] = chr(x.index(aux[i]) + 32)
#     aux = "".join(aux2)

# aux = list(aux)

# asa in plm
aux = list(scramble)
for _ in range(20):
    for i in range(len(aux)):
        number = x.index(aux[i]) + 32
        aux[i] = chr(number)


for i in range(0, len(aux), 2):
    aux[i], aux[i + 1] = aux[(i + 1)], aux[i]


for i in range(10000000):
    a = ''.join(unshuffle(aux, timp+i*step))
    if i % 1000 == 0:
        print(i)
    if "flag" in a:
        print(a)
        break
