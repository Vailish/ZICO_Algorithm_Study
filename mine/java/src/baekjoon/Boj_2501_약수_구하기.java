package baekjoon;

import java.util.Scanner;

public class Boj_2501_약수_구하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        int cnt = 0;
        int i = 0;
        // 약수 구하기
        while (cnt < k && i < n) {
            i++;
            if (n % i == 0) {
                cnt ++;
            }
        }
        if (cnt < k) {System.out.println(0);}
        else {System.out.println(i);}
    }
}
