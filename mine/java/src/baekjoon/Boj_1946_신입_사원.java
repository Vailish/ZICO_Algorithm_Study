package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj_1946_신입_사원 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cs = Integer.parseInt(br.readLine());
        StringBuilder answer = new StringBuilder();
        for (int c=0; c<cs; c++) {
            int n = Integer.parseInt(br.readLine());
            int[][] scores = new int[n][2];
            int result = 0;
            for (int i=0; i<n; i++) {
                String[] val = br.readLine().split(" ");
                scores[i][0] = Integer.parseInt(val[0]);
                scores[i][1] = Integer.parseInt(val[1]);
            }
            // 두 과목 모두 다른 사람들 보다 낮으면 탈락 하나라도 높으면 통과
            for (int i=0; i<n-1; i++) {
                boolean chk = true;
                for (int j=i+1; j<n; j++) {
                    if (scores[i][0] < scores[j][0] && scores[i][1] < scores[j][1]) {
                        chk = false;
                    }
                }
                if (chk) result++;
            }
            answer.append(result).append("\n");
        }
        System.out.println(answer);
    }
}
