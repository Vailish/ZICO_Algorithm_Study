package baekjoon;

import java.util.Scanner;

public class Boj_킹_퀸_룩_비숍_나이트_폰 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] chk = {1, 1, 2, 2, 2, 8};

        StringBuilder answer = new StringBuilder();
        for (int i=0; i<6; i++) {

            int n = sc.nextInt();
            answer.append(chk[i] - n).append(" ");
        }

        System.out.println(answer);

    }
}
