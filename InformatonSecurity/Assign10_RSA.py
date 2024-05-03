import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

# Function to find GCD (Greatest Common Divisor)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Function to generate public and private keys
def generate_keys(p, q):
    # Calculate n
    n = p * q

    # Calculate Euler's Totient Function
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = 2
    while gcd(e, phi) != 1:
        e += 1

    # Calculate d such that (d * e) % phi = 1
    d = 2
    while (d * e) % phi != 1:
        d += 1

    return (e, n), (d, n)

# Function to encrypt a message
def encrypt(msg, e, n):
    encrypted_msg = ""
    for char in msg:
        encrypted_char = pow(ord(char), e, n)
        encrypted_msg += chr(encrypted_char)
    return encrypted_msg

# Function to decrypt an encrypted message
def decrypt(encrypted_msg, d, n):
    decrypted_msg = ""
    for char in encrypted_msg:
        decrypted_char = pow(ord(char), d, n)
        decrypted_msg += chr(decrypted_char)
    return decrypted_msg

# Main function
def main():
    p = int(input("Enter first prime number (p): "))
    q = int(input("Enter second prime number (q): "))

    if not is_prime(p) or not is_prime(q):
        print("Both numbers must be prime.")
        return

    public_key, private_key = generate_keys(p, q)
    print("Public Key (e, n):", public_key)
    print("Private Key (d, n):", private_key)

    msg = input("Enter message to encrypt: ")

    encrypted_msg = encrypt(msg, public_key[0], public_key[1])
    print("Encrypted message:", encrypted_msg)

    decrypted_msg = decrypt(encrypted_msg, private_key[0], private_key[1])
    print("Decrypted message:", decrypted_msg)

if __name__ == "__main__":
    main()


# Enter first prime number (p): 61
# Enter second prime number (q): 53
# Enter message to encrypt: Hello, World!
