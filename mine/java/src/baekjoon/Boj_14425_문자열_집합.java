package baekjoon;

import java.util.HashMap;
import java.util.Scanner;

public class Boj_14425_문자열_집합 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        HashMap<String, Boolean> myDict = new HashMap<>();
        for (int i=0; i<n; i++) {
            myDict.put(sc.next(), true);
        }
        int cnt = 0;

        for (int i=0; i<m; i++) {
            if (myDict.containsKey(sc.next())) {
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
