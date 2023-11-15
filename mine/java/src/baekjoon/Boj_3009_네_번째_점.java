package baekjoon;

import java.util.Scanner;

public class Boj_3009_네_번째_점 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a[] = sc.nextLine().split(" ");
        String b[] = sc.nextLine().split(" ");
        String c[] = sc.nextLine().split(" ");

        if (a[0].equals(b[0])) {
            System.out.print(c[0]);
        } else if (b[0].equals(c[0])) {
            System.out.print(a[0]);
        } else {
            System.out.print(b[0]);
        }
        System.out.print(" ");

        if (a[1].equals(b[1])) {
            System.out.print(c[1]);
        } else if (b[1].equals(c[1])) {
            System.out.print(a[1]);
        } else {
            System.out.print(b[1]);
        }
    }
}
