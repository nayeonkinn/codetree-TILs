import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int total = 0, cnt = 0;

        while (true) {
            int age = sc.nextInt();

            if (age < 20 || age > 29)
                break;
            total += age;
            cnt++;
        }

        System.out.printf("%.2f", (float)total/cnt);
    }
}