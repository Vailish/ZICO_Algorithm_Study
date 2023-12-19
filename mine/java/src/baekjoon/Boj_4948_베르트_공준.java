package baekjoon;

import java.util.Scanner;

public class Boj_4948_베르트_공준 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int n = sc.nextInt();
            if (n==0) {
                return;
            } else {
                System.out.println(checkPrimeNumber(n));
            }

        }
    }
    static int checkPrimeNumber(int n) {
        boolean[] primeNum = new boolean[2*n+1];
        primeNum[0] = true;
        // 소수가 아닌 수는 true로 변경
        for (int i=2; i<2*n+1; i++) {
            if (!primeNum[i]) {
                for (int j = 2 * i; j < 2 * n + 1; j += i) {
                    primeNum[j] = true;
                }
            }
        }
        int cnt = 0;
        for (int i=n+1; i<=2*n; i++) {
            if (!primeNum[i]) {
                cnt++;
            }
        }
        return cnt;
    }
}
