package baekjoon;

import java.util.Scanner;

public class Boj_5086_배수와_약수 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            if (a == 0 && b == 0) {
                break;
            } else {
                if (a > b && a % b == 0) {
                    System.out.println("multiple");
                } else if (b > a && b % a == 0) {
                    System.out.println("factor");
                } else {
                    System.out.println("neither");
                }
            }
        }
    }
}
