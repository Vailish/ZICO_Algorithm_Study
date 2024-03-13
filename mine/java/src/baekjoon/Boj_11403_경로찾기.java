package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj_11403_경로찾기 {  // 플로이드 와샬 알고리즘
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;

        // 이차원 배열 만들기
        int[][] arr = new int[n][n];
        for (int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j<n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 갈수 있는지 여부 확인하기
        // 플로이드 와샬 알고리즘
        // i 에서 j로 j에서 k로 갈수 있는가
        for (int k=0; k<n; k++) {
            for (int i=0; i<n; i++) {
                for (int j = 0; j < n; j++) {
                    if (arr[i][k] == 1 && arr[k][j] == 1) arr[i][j] = 1;
                }
            }
        }
        // 출력하기
        StringBuilder answer = new StringBuilder();
        for (int i =0; i<n; i++) {
            for (int j=0; j<n; j++) {
                answer.append(arr[i][j] + " ");
            }
            answer.append("\n");
        }
        System.out.println(answer);
    }
}
