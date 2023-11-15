package baekjoon;

import java.util.Scanner;

public class Boj_11653_소인수분해 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int num = 1;

        while (n > 1) {
            num++;
            if (n % num==0) {
                System.out.println(num);
                n /= num;
                num = 1;
            }
        }
    }
}
