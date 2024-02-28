package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj_2805_나무자르기_풀이2 { // 시간초과 -> 카운트리스트로 변경 -> 메모리초과

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());  // 나무수
        int m = Integer.parseInt(st.nextToken());  // 필요한 나무길이
        st = new StringTokenizer(br.readLine());
        int[] trees = new int[1000000000];
        int highLv = 0;
        int tree;
        for (int i = 0; i < n; i++) {
            tree = Integer.parseInt(st.nextToken());
            trees[tree] += 1;
            if (highLv < tree) highLv = tree;
        }
        int numberOfTrees = 0;
        for (int i = highLv; i > 0; i--) {
            numberOfTrees += trees[i];
            if (numberOfTrees > m) {
                System.out.println(i);
                break;
            }
        }
    }
}
