import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n, i = 1;

        n = sc.nextInt();

        while (n > 1) {
            n /= i;
            i++;
        }

        System.out.println(i - 1);
    }
}