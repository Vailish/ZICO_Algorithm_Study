package baekjoon;

import java.util.Scanner;

public class Boj_2563_색종이 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] paper = new int[101][101];

        // 필드 채우기
        for (int k=0; k<n; k++) {
            int r = sc.nextInt();
            int c = sc.nextInt();

            for (int i=c; i<c+10; i++) {
                for (int j=r; j<r+10; j++) {
                    paper[i][j] = 1;
                }
            }

        }
        int answer = 0;
        // 칠한 구역값 구하기
        for (int i=0; i<100; i++) {
            for (int j=0; j<100; j++) {
                answer += paper[i][j];
            }
        }
        System.out.println(answer);
    }
}
