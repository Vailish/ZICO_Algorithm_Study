package baekjoon;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj_1389_케빈_베이컨의_6단계_법칙2 {
    static int n, m;				// 유저(노드) 수 n, 친구 관계(간선)의 수 m
    static int minNode = 1;			// 출력, 비용 합이 최소인 노드 번호

    static final int INF = 9;
    static int[][] dist;			// 비용 배열
    static int[] numbers;			// 각 유저의 케빈 베이컨 수

    static void solution() {
        // 각 유저의 케빈 베이컨 수 계산 및 최소인 유저 찾기
        numbers = new int[n + 1];		// 각 유저의 케빈 베이컨 수 계산
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++)
                numbers[i] += dist[i][j];

            if (numbers[minNode] > numbers[i])
                minNode = i;
        }
    }

    static void floyd() {
        // 3) 3중 for문 - 중간 경유 노드, 시작 노드, 끝 노드
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    // 중간 경유 노드를 거쳐갈 때, 비용 값이 더 작은 경우 갱신
                    if (dist[i][j] > dist[i][k] + dist[k][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in)
        );
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        // 1) 비용 배열 초기화
        dist = new int[n + 1][n + 1];			// [1][1] ~ [n][n] 사용
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == j)
                    dist[i][j] = 0;
                else
                    dist[i][j] = INF;
            }
        }
        System.out.println("ㅇㅅㅇ");
        System.out.println(Arrays.deepToString(dist));

        // 2) 비용 배열에 간선 가중치 저장
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int startV = Integer.parseInt(st.nextToken());
            int destV = Integer.parseInt(st.nextToken());

            dist[startV][destV] = 1;	// 친구 관계: 양방향
            dist[destV][startV] = 1;
        }
        System.out.println("ㅇㅁㅇ");
        System.out.println(Arrays.deepToString(dist));

        floyd();
        System.out.println("ㅇㅂㅇ");
        System.out.println(Arrays.deepToString(dist));
        solution();
        System.out.println(minNode);
    }
}