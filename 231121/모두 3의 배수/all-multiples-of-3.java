import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        boolean flag = true;

        for (int i = 0; i < 5; i++) {
            int n = sc.nextInt();

            if (n % 3 != 0) {
                flag = false;
                break;
            }
        }

        System.out.println(flag ? 1 : 0);
    }
}