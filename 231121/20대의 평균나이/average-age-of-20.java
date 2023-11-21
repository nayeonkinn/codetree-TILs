import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int total = 0, cnt = 0;

        while (true) {
            int n;

            n = sc.nextInt();

            if (n < 20 || n > 29) {
                System.out.printf("%.2f", (double)total/cnt);
                break;
            }

            total += n;
            cnt++;
        }

    }
}