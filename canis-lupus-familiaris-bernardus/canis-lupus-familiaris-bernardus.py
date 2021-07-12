from Crypto.Cipher import AES
from Crypto.Random import *
from Crypto.Util.Padding import *
import random
print("Hello, I'm Bernard the biologist!")
print()
print("My friends love to keyboard spam at me, and my favorite hobby is to tell them whether or not their spam is a valid peptide or not. Could you help me with this?")
print("Your job is to identify if a string is a valid peptide.")
print()
print("If it is, type the letter T. If it's not, type F. Then, I'd like for you to return a valid IV that changes the ciphertext such that it is a valid peptide!")
print()
print("You only have to get 100 correct. Good luck!")
print()
print("Oh yeah, I almost forgot. Here's the list of valid amino acids:")
print("""
alanine: A
asparagine or aspartic acid: B
cysteine: C
aspartic acid: D
glutamic acid: E
phenylalanine: F
histidine: H
isoleucine: I
glycine: G
lysine: K
leucine: L
methionine: M
asparagine: N
proline: P
glutamine: Q
arginine: R
serine: S
threonine: T
valine: V
tryptophan: W
glutamine or glutamic acid: Z
tyrosine: Y
""")

# J O U X


def spam():
    r = ""
    for i in range(16):
        r += random.choice(list("ABCDEFGHIKLMNPQRSTVWYZ"))
    if random.randint(0, 1) == 0:
        ra = random.randint(0, 15)
        return [(r[:ra]+random.choice(list("JOUX"))+r[ra+1:]).encode("utf-8"), True]
    return [r.encode('utf-8'), False]


def valid(str1):
    v = list("ABCDEFGHIKLMNPQRSTVWYZ")
    for i in str1:
        if i not in v:
            return False
    return True


def enc(key, iv, pt):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(pt, AES.block_size))


def dec(key, iv, ct):
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ct), AES.block_size)
    except (ValueError, KeyError):
        print("THAT IS NOT A VALID PEPTIDE.")
        exit(1)


for i in range(100):
    key = get_random_bytes(16)
    iv = get_random_bytes(16)
    spammmmm = spam()
    changed = spammmmm[1]
    spammmmm = spammmmm[0]
    guess1 = input("Is "+spammmmm.decode('utf-8')+" a valid peptide? ")
    if (guess1 == "T" and not changed) or (guess1 == "F" and changed):
        print("Correct!")
        if guess1 == "F":
            print("Here's the IV: "+iv.hex())
            # NOUA peptida decriptate tre sa fie valida
            # se decripteaza din (key, INPUTU MEU, enc(key,iv,peptida))
            #                      ^                    ^
            if not valid(dec(key, bytes.fromhex(input("Now, give me an IV to use: ").strip()), enc(key, iv, spammmmm)).decode('utf-8')):
                print("WRONG.")
                exit(0)
            else:
                print("The peptide is now valid!")
    else:
        print("WRONG.")
        exit(0)

print("Thank you for your service in peptidology. Here's your flag:")
