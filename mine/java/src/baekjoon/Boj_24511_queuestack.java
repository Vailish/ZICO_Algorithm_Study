package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Boj_24511_queuestack {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        Deque<Integer> dq = new ArrayDeque<>();
        int[] idx = new int[N];
        for (int i=0; i<N; i++) {
            idx[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            if (idx[i]==0) dq.offer(Integer.parseInt(st.nextToken()));
            else st.nextToken();
        }
        StringBuilder answer = new StringBuilder();
        int k = 0;
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        while (k<m) {
            dq.offerFirst(Integer.parseInt(st.nextToken()));
            answer.append(dq.pollLast()).append(" ");
            k++;
        }
        System.out.println(answer);
    }
}
