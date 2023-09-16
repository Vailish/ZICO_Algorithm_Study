package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj_10813_공_바꾸기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        for (int i=0; i<n; i++) {
            arr[i] = i+1;
        }

        for (int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) -1;
            int b = Integer.parseInt(st.nextToken()) -1;

            int tmp = arr[a];
            arr[a] = arr[b];
            arr[b] = tmp;
        }

        StringBuilder answer = new StringBuilder();
        for (int val : arr) {
            answer.append(val).append(" ");
        }

        System.out.println(answer);
    }
}
