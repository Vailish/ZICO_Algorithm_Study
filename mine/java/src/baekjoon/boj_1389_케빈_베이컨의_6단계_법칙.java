package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_1389_케빈_베이컨의_6단계_법칙 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] answer = new int[2];
        answer[0] = 99999999;
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        //비용 배열 초기화
        int[][] dist = new int[n+1][n+1];
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=n; j++) {
                if (i==j)
                    dist[i][j] = 0;
                else
                    dist[i][j] = 99999999;
            }
        }

        // 비용 배열 간선 가중치 저장
        for (int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            dist[r][c] = 1;
            dist[c][r] = 1;
        }

        //floydwarshall
        // 얘가 먼가 잘못된듯 확인해보자
        for (int k=1; k<=n; k++) {
            for (int i=1; i<=n; i++) {
                for (int j=1; j<=n; j++) {
                    if(dist[i][j] > dist[i][k] + dist[k][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }

        //행별로 계산
        int tmp;
        for (int i=1; i<=n; i++) {
            tmp = 0;
            for (int j=1; j<=n; j++) {
                tmp += dist[i][j];
            }
            if (answer[0] > tmp) {
                answer[0] = tmp;
                answer[1] = i;
            }
        }
        // 결과 출력
        System.out.println(answer[1]);
    }
}
