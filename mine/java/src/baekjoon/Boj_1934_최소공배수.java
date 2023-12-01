package baekjoon;

import java.util.Scanner;

public class Boj_1934_최소공배수 {
    static int gcd(int a, int b){
        int t;
        while (b!=0) {
            t = a%b;
            a = b;
            b = t;
        }
        return a;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder answer = new StringBuilder();
        int n = sc.nextInt();
        // 유클리드 호제법 활용
        for (int i=0; i<n; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            answer.append(a*b/gcd(a,b)).append("\n");
        }
        System.out.println(answer);
    }
}
