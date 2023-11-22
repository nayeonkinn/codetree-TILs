import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n;

        n = sc.nextInt();

        for (int i = 1; i < n + 1; i++) {
            for (int j = n; j > 0; j--) {
                System.out.print(i * j + " ");
            }
            System.out.println();
        }
    }
}