package baekjoon;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Boj_2581_소수 {
    static ArrayList<Integer> answer;
    static void chk(int n) {
        int cnt = 0;
        for (int i=1; i<n+1; i++) {
            if(cnt > 2) {
                return;
            }
            if(n%i == 0) {
                cnt ++;
            }
        }
        if (cnt == 2) {
            answer.add(n);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        answer = new ArrayList<>();

        for (int i=m; i<n+1; i++) {
            chk(i);
        }

        Collections.sort(answer);
        int sum = 0;
        for (int i=0; i<answer.size(); i++) {
            sum += answer.get(i);
        }
        if (answer.size() == 0) {
            System.out.println(-1);
        } else {System.out.printf("%s\n%s\n",sum ,answer.get(0));}
    }
}
