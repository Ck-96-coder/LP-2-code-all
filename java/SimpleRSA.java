import java.math.BigInteger;
import java.util.Scanner;

public class SimpleRSA {

    public static boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int c = 2; c <= Math.sqrt(n); c++) {
            if (n % c == 0) {
                return false;
            }
        }
        return true;
    }

    public static BigInteger gcd(BigInteger a, BigInteger b) {
        if (b.equals(BigInteger.ZERO)) {
            return a;
        }
        return gcd(b, a.mod(b));
    }

    public static BigInteger[] generateKeys(int p, int q) {
        BigInteger n = BigInteger.valueOf(p).multiply(BigInteger.valueOf(q));
        BigInteger phi = BigInteger.valueOf(p - 1).multiply(BigInteger.valueOf(q - 1));

        BigInteger e = new BigInteger("2");
        while (!gcd(e, phi).equals(BigInteger.ONE)) {
            e = e.add(BigInteger.ONE);
        }

        BigInteger d = new BigInteger("2");
        while (!d.multiply(e).mod(phi).equals(BigInteger.ONE)) {
            d = d.add(BigInteger.ONE);
        }

        return new BigInteger[]{e, n, d};
    }

    public static String encrypt(String msg, BigInteger e, BigInteger n) {
        StringBuilder encryptedMsg = new StringBuilder();
        for (char ch : msg.toCharArray()) {
            BigInteger encryptedChar = BigInteger.valueOf((int) ch).modPow(e, n);
            encryptedMsg.append((char) encryptedChar.intValue());
        }
        return encryptedMsg.toString();
    }

    public static String decrypt(String encryptedMsg, BigInteger d, BigInteger n) {
        StringBuilder decryptedMsg = new StringBuilder();
        for (char ch : encryptedMsg.toCharArray()) {
            BigInteger decryptedChar = BigInteger.valueOf((int) ch).modPow(d, n);
            decryptedMsg.append((char) decryptedChar.intValue());
        }
        return decryptedMsg.toString();
    }

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

        BigInteger[] keys = generateKeys(p, q);
        BigInteger e = keys[0];
        BigInteger n = keys[1];
        BigInteger d = keys[2];

        System.out.println("Public Key (e, n): " + e + ", " + n);
        System.out.println("Private Key (d, n): " + d + ", " + n);

        scanner.nextLine(); // Consume the remaining newline
        System.out.print("Enter message to encrypt: ");
        String msg = scanner.nextLine();

        String encryptedMsg = encrypt(msg, e, n);
        System.out.println("Encrypted message: " + encryptedMsg);

        String decryptedMsg = decrypt(encryptedMsg, d, n);
        System.out.println("Decrypted message: " + decryptedMsg);

        scanner.close();
    }
}
