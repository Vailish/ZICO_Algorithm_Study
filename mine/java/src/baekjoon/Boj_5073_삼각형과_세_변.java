package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class Boj_5073_삼각형과_세_변 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int[] v = {sc.nextInt(), sc.nextInt(), sc.nextInt()};
            Arrays.sort(v);
            if (v[0]==0 && v[1]==0 && v[2]==0) {
                return;
            } else if (v[0]==v[1] && v[1]==v[2] && v[0]==v[2]) {
                System.out.println("Equilateral");
            } else if (v[2] < v[0] + v[1] && v[1] < v[0] + v[2] && v[0] < v[1] + v[2]) {
                if (v[0]==v[1] || v[1]==v[2] || v[0]==v[2]) {
                    System.out.println("Isosceles");
                } else {
                    System.out.println("Scalene");
                }
            } else {
                System.out.println("Invalid");
            }
        }
    }
}
