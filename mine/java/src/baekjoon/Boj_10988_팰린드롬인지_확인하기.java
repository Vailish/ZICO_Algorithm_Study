package baekjoon;

import java.util.Scanner;

public class Boj_10988_팰린드롬인지_확인하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int strSize = str.length();

        for (int i=0; i<strSize/2; i++) {
            if (str.charAt(i) != str.charAt(strSize-i-1)) {
                System.out.println(0);
                return;
            }
        }

        System.out.println(1);

    }
}
