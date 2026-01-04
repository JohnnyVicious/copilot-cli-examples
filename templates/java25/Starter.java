import java.util.Scanner;

/**
 * Starter template for Java 25
 * Entrypoint: Compile with `javac Starter.java` and run with `java Starter`
 * Sample I/O:
 *   Input: (via stdin or args)
 *   Output: (via stdout)
 */
public class Starter {
    public static void main(String[] args) {
        // Read input
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String input = scanner.nextLine();
        scanner.close();

        // Process
        String result = String.format("Hello, %s!", input);

        // Write output
        System.out.println(result);
    }
}
