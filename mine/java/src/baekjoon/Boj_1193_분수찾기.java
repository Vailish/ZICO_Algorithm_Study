package baekjoon;

import java.util.Scanner;

public class Boj_1193_분수찾기 {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        int i = 0;
        int k = 0;

        while (k < n) {
            i++;
            k+=i;
        }
        int l = n-(k-i);
        if (i % 2 == 1) {
            System.out.printf("%s/%s",i-l+1, l);
        } else {
            System.out.printf("%s/%s",l, i-l+1);
        }
    }
}
