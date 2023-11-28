def power_mod(base, exponent, modulus):
    return pow(base, exponent, modulus)
def diffie_hellman(prime, primitive_root, private_key):
    public_key = power_mod(primitive_root, private_key, prime)
    return public_key
def main():
    prime = int(input("Enter the prime number (p): "))
    primitive_root = int(input("Enter the primitive root (g): "))
    private_key_alice = int(input("Alice's private key: "))
    private_key_bob = int(input("Bob's private key: "))
    public_key_alice = diffie_hellman(prime, primitive_root, private_key_alice)
    public_key_bob = diffie_hellman(prime, primitive_root, private_key_bob)
    shared_secret_alice = power_mod(public_key_bob, private_key_alice, prime)
    shared_secret_bob = power_mod(public_key_alice, private_key_bob, prime)
    print(f"Alice's shared secret: {shared_secret_alice}")
    print(f"Bob's shared secret: {shared_secret_bob}")
if __name__ == "__main__":
    main()