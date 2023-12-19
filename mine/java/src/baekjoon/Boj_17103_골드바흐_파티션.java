package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Boj_17103_골드바흐_파티션 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int c = Integer.parseInt(br.readLine());
        StringBuilder answer = new StringBuilder();
        // 소수를 구한다
        boolean[] nums = getPrimeNums(1000001);
        for (int t = 0; t < c; t++) {
            int n = Integer.parseInt(br.readLine());
            // 해당 소수들로 조합의 경우의 수를 구한다
            int cnt=0;
            for (int i=1; i<=n/2; i++) {
                if (!nums[i] && !nums[n-i]) {
                    cnt++;
                }
            }
            answer.append(cnt).append("\n");
        }
        System.out.println(answer);
        br.close();
    }

    static boolean[] getPrimeNums(int n) {
        boolean[] nums = new boolean[n];
        nums[0] = true;
        nums[1] = true;
        for (int i = 2; i < n + 1; i++) {
            for (int j = 2 * i; j < n; j += i) {
                if (!nums[j]) {
                    nums[j] = true;
                }
            }
        }
        return nums;
    }
}
