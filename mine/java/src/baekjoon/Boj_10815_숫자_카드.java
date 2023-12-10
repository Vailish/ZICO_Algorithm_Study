package baekjoon;

import java.util.HashMap;
import java.util.Scanner;

public class Boj_10815_숫자_카드 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nLst = new int[n];
        HashMap<Integer, Integer> nMap = new HashMap<>();
        for (int i=0; i<n; i++) {
            nLst[i] = sc.nextInt();
            nMap.put(nLst[i], 1);
        }
        StringBuilder answer = new StringBuilder();
        int m = sc.nextInt();
        for (int i=0; i<m; i++) {
            int chk = sc.nextInt();
            if (nMap.containsKey(chk)) {
                answer.append(1).append(" ");
            } else {answer.append(0).append(" ");}
        }
        System.out.println(answer);
    }
}
