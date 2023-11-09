package baekjoon;

import java.util.Scanner;

public class Boj_2720_세탁소_사장_동혁 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] coins = {25, 10, 5, 1};
        int len = sc.nextInt();
        for (int i=0; i<len; i++) {
            StringBuilder answer = new StringBuilder();
            int value = sc.nextInt();
            int remain;
            for (int n : coins) {
                remain = value % n;
                answer.append(value / n).append(" ");
                value = remain;
            }

            System.out.println(answer);
        }
    }
}
