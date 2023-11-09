package baekjoon;

import java.util.Scanner;

public class Boj_11005_진법_전환_2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        int k = sc.nextInt();
        StringBuilder answer = new StringBuilder();
        while (number >= 1) {
            int remain = number % k;
            if (number % k < 10) {
                answer.append(remain);
            } else {
                char chr = Character.forDigit(remain, k);
                answer.append(String.valueOf(chr).toUpperCase());
            }
            number = number / k;
        }
        answer.reverse();
        System.out.println(answer);
    }
}
