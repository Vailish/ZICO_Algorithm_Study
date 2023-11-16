package baekjoon;

import java.util.Scanner;

public class Boj_9063_대지 {
    public static void main(String[] args) {
        // 각각의 점에서 각 축의 최소값과 최대값을 꼭지점으로 하는 직사각형의 넓이를 구하면 됨
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        if (n<=1) {
            System.out.println(0); return;
        }
        int[] r = {10001,-10001}; // 최소, 최대
        int[] c = {10001,-10001};
        int idx = 1;
        while (idx <= n) {
            int newR = sc.nextInt();
            int newC = sc.nextInt();

            if (newR < r[0]) {r[0] = newR;}
            if (newR > r[1]) {r[1] = newR;}
            if (newC < c[0]) {c[0] = newC;}
            if (newC > c[1]) {c[1] = newC;}

            idx ++;
        }
        System.out.println((r[1] - r[0]) * (c[1] - c[0]));
    }
}
