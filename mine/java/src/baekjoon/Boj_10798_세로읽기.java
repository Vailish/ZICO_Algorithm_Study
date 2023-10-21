package baekjoon;

import java.util.Scanner;

public class Boj_10798_세로읽기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[][] field = new char[5][15];

        // 2차원 배열 채우기
        for (int i=0; i<5; i++) {
            String input = sc.nextLine();
            for (int j=0; j<input.length(); j++) {
                field[i][j] = input.charAt(j);
            }
        }

        // 세로로 읽기
        for (int j=0; j<15; j++) {
            for (int i=0; i<5; i++) {
                // 비어있다면 패스
                if (field[i][j] == '\0') {
                    continue;
                }
                System.out.print(field[i][j]);
            }
        }
    }
}
