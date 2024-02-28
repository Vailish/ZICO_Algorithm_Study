package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Boj_2805_나무자르기_풀이3 { // 이분탐색

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());  // 나무수
        int m = Integer.parseInt(st.nextToken());  // 필요한 나무길이
        st = new StringTokenizer(br.readLine());
        int[] trees = new int[n];
        int min = 0;
        int max = 0;

        for (int i = 0; i < n; i++) {
            trees[i] = Integer.parseInt(st.nextToken());
            if (trees[i] > max) max = trees[i];
        }

        // 이분 탐색(upper bound)
        while (min < max) {
            int mid = (min + max) / 2;
            long sum = 0;
            for (int tree : trees) {
                if (tree - mid > 0) sum += tree - mid;
            }
            if (sum < m) max = mid;
            else min = mid + 1;
        }
        System.out.println(min - 1);

    }
}
