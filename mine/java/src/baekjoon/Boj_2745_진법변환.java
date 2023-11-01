package baekjoon;

import java.util.Scanner;

public class Boj_2745_진법변환 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] rawNums = sc.next().split("");

        int n = sc.nextInt();
        int answer = 0;
        int val = 1;

        for (int i=rawNums.length-1; i>-1; i--) {
            if (rawNums[i].charAt(0)<58) {
                answer += (rawNums[i].charAt(0)-48) * val;
            } else {
                answer += (rawNums[i].charAt(0) - 55) * val;
            }
            val *= n;
        }

        System.out.println(answer);
    }
}
