package baekjoon;

import java.util.HashMap;
import java.util.Scanner;

public class Boj_1269_대칭_차집합 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        HashMap<Integer, Boolean> mapN = new HashMap<>();
        for (int i=0; i<n; i++) {
            mapN.put(sc.nextInt(), true);
        }
        int cnt = 0;
        for (int i=0; i<m; i++) {
            if (mapN.containsKey(sc.nextInt())) {
                cnt++;
            }
        }
        System.out.println(n+m-cnt*2);
    }
}
