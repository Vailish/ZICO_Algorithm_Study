package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj_11021 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder answer = new StringBuilder();

        for (int i=0;i<n;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            answer.append("Case #");
            answer.append(i+1);
            answer.append(": ");
            answer.append(Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken()));
            answer.append("\n");
        }

        System.out.println(answer);
    }
}
