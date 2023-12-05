package baekjoon;

import java.util.Scanner;

public class Boj_13241_최소공배수 {

    static long gcd(long a, long b) {
        long r;
        while (b != 0) {
            r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        System.out.println(a * b / gcd(a, b));
    }
}
