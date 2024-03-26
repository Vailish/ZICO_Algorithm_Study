package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Boj_2178_미로_탐색 {
    static String[] field;
    static boolean[][] visited;
    static int bfs (int n, int m) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0, 1});
        int[] values;
        int r;
        int c;
        int d;
        int next_r;
        int next_c;
        int[] dr = new int[]{0, 0, -1, 1}; // 상 하 좌 우
        int[] dc = new int[]{-1, 1, 0, 0};
        while (!queue.isEmpty()) {
            values = queue.poll();
            r = values[0];
            c = values[1];
            d = values[2];
            visited[r][c] = true;

            // delta
            for (int i=0; i<4; i++) {
                next_r = r + dr[i];
                next_c = c + dc[i];

                if (next_r >= 0 && next_r < n && next_c >= 0 && next_c < m && field[next_r].charAt(next_c) == '1' && !visited[next_r][next_c]) {
                    visited[next_r][next_c] = true;
                    queue.add(new int[]{next_r, next_c, d+1});
                    if (next_r == n-1 && next_c == m-1) {
                        return d+1;
                    }
                }
            }
        }
        return -1;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        field = new String[n];
        visited = new boolean[n][m];
        for (int i=0; i<n; i++) {
            field[i] = br.readLine();
        }
        System.out.println(bfs(n,m));
    }
}
