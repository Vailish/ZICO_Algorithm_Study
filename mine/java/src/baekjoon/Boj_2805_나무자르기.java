package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj_2805_나무자르기 { // 시간초과

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());  // 나무수
        int m = Integer.parseInt(st.nextToken());  // 필요한 나무길이
        st = new StringTokenizer(br.readLine());
        int[] trees = new int[n];
        int highLv = 0;
        int tree;
        for (int i=0; i<n; i++) {
            tree = Integer.parseInt(st.nextToken());
            trees[i] = tree;
            if (highLv < tree) highLv = tree;
        }

        int numberOfTrees = 0;
        int tmp;
        // highLv > 0이고 요구치를 채우지 못했을 경우
        highLv ++;
        while (highLv > 0 && numberOfTrees < m) {
            highLv--;
            // 순회하면서 나무자르기
            for (int i=0; i<n; i++) {
                if (trees[i] > highLv) {
                   tmp = trees[i] - highLv;
                   trees[i] = highLv;
                   numberOfTrees += tmp;
               }
            }
        }
        System.out.println(highLv);
    }
}
