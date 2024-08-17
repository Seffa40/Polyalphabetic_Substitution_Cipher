import random
import string

def generate_mappings(key, N=1000):
    random.seed(key)
    s = "abcdefghijklmnopqrstuvwxyz"
    trantab_enc = [None] * N
    trantab_dec = [None] * N

    for i in range(N):
        mapping = random.sample(s, len(s))
        trantab_enc[i] = str.maketrans(s, ''.join(mapping))
        trantab_dec[i] = str.maketrans(''.join(mapping), s)

    return trantab_enc, trantab_dec

def Alice_encrypt(text, key):
    trantab_enc, _ = generate_mappings(key)
    ciphertext = [None] * len(text)
    for i in range(len(text)):
        if text[i].isalpha():
            lower = text[i].lower()
            cipher_char = lower.translate(trantab_enc[i % 1000])
            if text[i].isupper():
                cipher_char = cipher_char.upper()
            ciphertext[i] = cipher_char
        else:
            ciphertext[i] = text[i]
    return ''.join(ciphertext)

def Bob_decrypt(ciphertext, key):
    _, trantab_dec = generate_mappings(key)
    plaintext = [None] * len(ciphertext)
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            lower = ciphertext[i].lower()
            plain_char = lower.translate(trantab_dec[i % 1000])
            if ciphertext[i].isupper():
                plain_char = plain_char.upper()
            plaintext[i] = plain_char
        else:
            plaintext[i] = ciphertext[i]
    return ''.join(plaintext)


text = """I remember as a child, and as a young budding naturalist, spending
all my time observing and testing the world around me moving
pieces, altering the flow of things, and documenting ways the world
responded to me. Now, as an adult and a professional naturalist, I’ve
approached language in the same way, not from an academic point
of view but as a curious child still building little mud dams in creeks
and chasing after frogs. So this book is an odd thing: it is a
naturalist’s walk through the language-making landscape of the
English language, and following in the naturalist’s tradition it
combines observation, experimentation, speculation, and
documentation activities we don’t normally associate with language. This book is about testing, experimenting, and playing with
language. It is a handbook of tools and techniques for taking words
apart and putting them back together again in ways that I hope are
meaningful and legitimate (or even illegitimate). This book is about
peeling back layers in search of the language-making energy of the
human spirit. It is about the gaps in meaning that we urgently need to
notice and name the places where our dreams and ideals are no
longer fulfilled by a society that has become fast-paced and hyper-
commercialized.
Language is meant to be a playful, ever-shifting creation but we have
been taught, and most of us continue to believe, that language must
obediently follow precisely prescribed rules that govern clear
sentence structures, specific word orders, correct spellings, and
proper pronunciations. If you make a mistake or step out of bounds
there are countless, self-appointed language experts who will
promptly push you back into safe terrain and scold you for your
errors. And in case you need reminding, there are hundreds of
dictionaries and grammar books to ensure that you remember the
“right” way to use English."""

key = "e"
ciphertext = Alice_encrypt(text, key)
print()
print("Alice sent encrypted text:")
print(ciphertext)
print()

print()
decrypted_text = Bob_decrypt(ciphertext, key)
print("\n Bob got Decrypted text:")
print(decrypted_text)
print()

print()

print("Oscar Attempt to Hack the Ciphered Text With Brute Force ....")

print()
def brute_force_attack(ciphertext):
    for potential_key in string.ascii_lowercase:
        try:
            decrypted_attempt = Bob_decrypt(ciphertext, potential_key)
            print("\nOscar's Potential decrypted text with key '{}':".format(potential_key))
            print(decrypted_attempt)
        except Exception as e:
            continue
print()

brute_force_attack(ciphertext)