package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Boj_16298_뱀과_사다리_게임 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Map<Integer, Integer> events = new HashMap<>();
        for (int i=0; i<n+m; i++) {
            st = new StringTokenizer(br.readLine());
            events.put(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }
        System.out.println(bfs(events));
    }
    private static int bfs(Map<Integer, Integer> events) {

        boolean[] visited = new boolean[101];

        Queue<Integer[]> queue = new LinkedList<>();
        queue.add(new Integer[]{1, 1}); // 위치, 횟수

        visited[1] = true; // 1번 시작
        int l;
        int d;
        while (!queue.isEmpty()) {
            Integer[] values = queue.poll();
            l = values[0];
            d = values[1];

            for (int i=1; i<=6; i++) {
                int nextL = l + i;
                while (events.containsKey(nextL)) { // 이벤트 반영
                    nextL = events.get(nextL);
                }
                if (nextL == 100) {
                    return d;
                } else if (nextL < 100 && !visited[nextL]) {
                    queue.add(new Integer[]{nextL,d+1});
                    visited[nextL] = true;
                }
            }

        }
        return -1;
    }
}
