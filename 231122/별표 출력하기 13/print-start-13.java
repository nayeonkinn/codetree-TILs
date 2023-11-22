import java.util.Scanner;

public class Main {
    static void printStars(int n) {
        for (int i = 0; i < n; i++)
            System.out.print("* ");
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n;

        n = sc.nextInt();

        int i = n, j = 1;

        while (i >= j) {
            printStars(i);
            
            if (i == j) {
                i--;
                j++;
                break;
            }

            printStars(j);

            i--;
            j++;
        }

        i++;
        j--;

        while (i < n + 1 & j > 0) {
            printStars(j);

            if (i == j) {
                i++;
                j--;
                continue;
            }

            printStars(i);

            i++;
            j--;
        }
    }
}