package baekjoon;

// 1 -> 0
// 1~4 -> 1
// 5~9 -> 2
// 10~16 -> 3

import java.util.Scanner;

public class Boj_13909_창문_닫기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int answer = 0;
        for (int i=1; i*i <= n; i++) {
            answer++;
        }
        System.out.println(answer);
    }
}
