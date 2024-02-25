package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj_1010_다리_놓기 {

    static int[][] dp = new int[30][30];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());
        StringTokenizer st;

        for (int i=0; i<testCase; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            //nCm을 구하면 됨
            System.out.println(comb(m, n));
        }
    }

    public static int comb(int n, int r) {
        if(dp[n][r] > 0) return dp[n][r];

        if(n==r || r==0) return dp[n][r] = 1;

        return dp[n][r] = comb(n-1, r-1) + comb(n-1, r);
    }
}
