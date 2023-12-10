package baekjoon;

import java.util.Scanner;

public class Boj_2485_가로수 {
    static int doGcd(int a, int b) {
        int r;
        while (b != 0) {
            r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] trees = new int[n];
        for (int i=0; i<n; i++) {
            trees[i] = sc.nextInt();
        }
        int gcd = trees[1] - trees[0];
        for (int i=1; i<n-1; i++) {
            gcd = doGcd(trees[i+1] - trees[i], gcd);
        }
        System.out.println((trees[n-1] - trees[0])/gcd - n + 1);
    }
}
