package baekjoon;

import java.util.Scanner;

public class Boj_11721_열_개씩_끊어_출력하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String strings = sc.next();
        int cnt = 0;
        while (cnt < strings.length()) {
            System.out.print(strings.charAt(cnt));
            cnt++;
            if (cnt % 10 == 0) {
                System.out.println();
            }
        }
    }
}
