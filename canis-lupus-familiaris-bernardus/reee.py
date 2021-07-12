from pwn import *

conn = remote("canis-lupus-familiaris-bernardus.hsc.tf", 1337)

def validpeptide(peptide):
    for c in peptide:
        if c not in "ABCDEFGHIKLMNPQRSTVWYZ":
            return False
    return True

for i in range(100):
    conn.recvuntil("Is ")
    peptide = conn.recvuntil(" a", drop=True).decode()
    print(peptide)

    if validpeptide(peptide):
        conn.sendline("T")
    else:
        conn.sendline("F")
        conn.recvuntil(" IV:")
        IV = conn.recvline().decode().strip()
        print(IV)
        for i in range(len(peptide)):
            if peptide[i] not in "ABCDEFGHIKLMNPQRSTVWYZ":
                break
        chestie = hex(ord(peptide[i]) ^ ord("A") ^ int(IV[2*i:2*i+2],16))[2:]
        chestie = ("0" + chestie)[-2:]
        newIV = IV[:i*2] + chestie + IV[i*2+2:]
        print(newIV)
        conn.sendline(newIV)

conn.interactive()