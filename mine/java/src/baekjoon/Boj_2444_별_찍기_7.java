package baekjoon;

import java.util.Scanner;

public class Boj_2444_별_찍기_7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        StringBuilder answer = new StringBuilder();
        for (int i=1;i<n+1;i++) {
            int spaceNum = n-i;
            int starNum = 2*i - 1;
            StringBuilder space = new StringBuilder();
            for (int a=0;a<spaceNum;a++) {
                space.append(" ");
            }
            StringBuilder star = new StringBuilder();
            for (int b=0;b<starNum;b++) {
                star.append("*");
            }

            answer.append(space).append(star).append("\n");
        }

        for (int i=1;i<n;i++) {
            int spaceNum = i;
            int starNum = 2*(n-i) - 1;
            StringBuilder space = new StringBuilder();
            for (int a=0;a<spaceNum;a++) {
                space.append(" ");
            }
            StringBuilder star = new StringBuilder();
            for (int b=0;b<starNum;b++) {
                star.append("*");
            }

            answer.append(space).append(star).append("\n");
        }

        System.out.println(answer);
    }
}
