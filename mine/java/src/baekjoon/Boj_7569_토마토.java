package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Boj_7569_토마토 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int answer = -1;

        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());

        int[][][] tomatos = new int[h][n][m];
        boolean[][][] visited = new boolean[h][n][m];
        Queue<int[]> queue = new LinkedList<>();
        int num = 0;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < m; k++) {
                    int value = Integer.parseInt(st.nextToken());
                    tomatos[i][j][k] = value;
                    if (value == 1) {
                        queue.add(new int[]{i, j, k, 0});
                    } else if (value == 0) {
                        num++;
                    }

                }
            }
        }
        if (num == 0) {System.out.println(num); return;}

        int[] dr = new int[]{-1, 1, 0, 0, 0, 0};
        int[] dc = new int[]{0, 0, -1, 1, 0, 0};
        int[] dz = new int[]{0, 0, 0, 0, 1, -1};

        // bfs
        int[] values;
        int cnt = 0;
        while (!queue.isEmpty()) {
            values = queue.poll();
            int z = values[0]; // h
            int r = values[1]; // n
            int c = values[2]; // m
            int d = values[3];
            visited[z][r][c] = true; // z, r, c

            for (int i = 0; i < 6; i++) {
                int nextZ = z + dz[i];
                int nextR = r + dr[i];
                int nextC = c + dc[i];
                if (
                        0 <= nextZ && nextZ < h && 0 <= nextR && nextR < n && 0 <= nextC && nextC < m &&
                                tomatos[nextZ][nextR][nextC] == 0 && !visited[nextZ][nextR][nextC]

                ) {
                    tomatos[nextZ][nextR][nextC] = 1;
                    queue.add(new int[]{nextZ, nextR, nextC, d + 1});
                    visited[nextZ][nextR][nextC] = true;
                    cnt++;
                    if (cnt == num) {
                        System.out.println(d+1);
                        return;
                    }
                }
            }
        }
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    if (tomatos[i][j][k] == 0) {
                        System.out.println(-1);
                        return;
                    }
                }
            }
        }
        System.out.println(answer);
    }
}
