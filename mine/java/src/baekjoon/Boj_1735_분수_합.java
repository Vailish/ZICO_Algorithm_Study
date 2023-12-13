package baekjoon;

import java.util.Scanner;

public class Boj_1735_분수_합 {
    static int gcd(int a, int b) {
        int r;
        while (b!=0) {
            r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // a / b
        // c / d
        // (ad + bc) / bd
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        StringBuilder answer = new StringBuilder();
        answer.append((a*d + b*c)/gcd((a*d + b*c),b*d)).append(" ").append(b*d / gcd((a*d + b*c),b*d));

        System.out.println(answer);
    }
}
