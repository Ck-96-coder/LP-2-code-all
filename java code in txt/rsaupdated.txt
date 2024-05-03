
import java.util.Scanner;

public class RSA {

    // Function to check if a number is prime
    static boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        if (n <= 3) {
            return true;
        }

        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }

        int i = 5;
        while (i * i <= n) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
            i += 6;
        }

        return true;
    }

    // Function to find GCD (Greatest Common Divisor)
    static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    // Function to generate public and private keys
    static int[][] generateKeys(int p, int q) {
        // Calculate n
        int n = p * q;

        // Calculate Euler's Totient Function
        int phi = (p - 1) * (q - 1);

        // Choose e such that 1 < e < phi and gcd(e, phi) = 1
        int e = 2;
        while (gcd(e, phi) != 1) {
            e++;
        }

        // Calculate d such that (d * e) % phi = 1
        int d = 2;
        while ((d * e) % phi != 1) {
            d++;
        }

        return new int[][] { { e, n }, { d, n } };
    }

    // Function to encrypt a message
    // Function to encrypt a message
    static String encrypt(String msg, int e, int n) {
        StringBuilder encryptedMsg = new StringBuilder();
        for (char c : msg.toCharArray()) {
            int encryptedChar = modPow((int) c, e, n);
            encryptedMsg.append((char) encryptedChar);
        }
        return encryptedMsg.toString();
    }

    // Function to decrypt an encrypted message
    static String decrypt(String encryptedMsg, int d, int n) {
        StringBuilder decryptedMsg = new StringBuilder();
        for (char c : encryptedMsg.toCharArray()) {
            int decryptedChar = modPow((int) c, d, n);
            decryptedMsg.append((char) decryptedChar);
        }
        return decryptedMsg.toString();
    }

    // Custom method for modular exponentiation
    static int modPow(int base, int exponent, int modulus) {
        int result = 1;
        base %= modulus;
        while (exponent > 0) {
            if (exponent % 2 == 1) {
                result = (result * base) % modulus;
            }
            base = (base * base) % modulus;
            exponent /= 2;
        }
        return result;
    }

    // Main function
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first prime number (p): ");
        int p = scanner.nextInt();
        System.out.print("Enter second prime number (q): ");
        int q = scanner.nextInt();

        if (!isPrime(p) || !isPrime(q)) {
            System.out.println("Both numbers must be prime.");
            return;
        }

        int[][] keys = generateKeys(p, q);
        System.out.println("Public Key (e, n): " + keys[0][0] + ", " + keys[0][1]);
        System.out.println("Private Key (d, n): " + keys[1][0] + ", " + keys[1][1]);

        System.out.print("Enter message to encrypt: ");
        scanner.nextLine(); // Consume newline character
        String msg = scanner.nextLine();

        String encryptedMsg = encrypt(msg, keys[0][0], keys[0][1]);
        System.out.println("Encrypted message: " + encryptedMsg);

        String decryptedMsg = decrypt(encryptedMsg, keys[1][0], keys[1][1]);
        System.out.println("Decrypted message: " + decryptedMsg);

        scanner.close();
    }
}
