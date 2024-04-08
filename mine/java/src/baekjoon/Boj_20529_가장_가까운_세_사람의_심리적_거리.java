package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Boj_20529_가장_가까운_세_사람의_심리적_거리 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int N;
        String[] mbtis;
        StringBuilder answer = new StringBuilder();
        for (int t = 0; t < T; t++) {
            PriorityQueue<Integer> heap = new PriorityQueue<>();
            N = Integer.parseInt(br.readLine());
            mbtis = br.readLine().split(" ");
            // 비둘기집 원리, MBTI가 16개 이므로 33개부터는 3개는 무조건 나옴
            // 즉, 비교군이 3개가 같으면 거리는 0이 되므로 0으로 처리할 수 있다.
            if (N > 32) {
                answer.append(0).append("\n");
                continue;
            }
            for (int i=0; i<N-2; i++) {
                for (int j=i+1; j<N-1; j++) {
                    for (int k=j+1; k<N; k++) {
                        int tmp = distance(mbtis[i], mbtis[j], mbtis[k]);
                        if (tmp != 0) heap.add(tmp);
                    }
                }
            }
            answer.append(heap.isEmpty() ? 0 : heap.poll()).append("\n");
        }
        System.out.println(answer);

    }
    static int distance(String mbti1, String mbti2, String mbti3) {
        int distance = 0;
        for (int i=0; i<4;i++) {
            distance += (mbti1.charAt(i)==mbti2.charAt(i)) ? 0 : 1;
            distance += (mbti1.charAt(i)==mbti3.charAt(i)) ? 0 : 1;
            distance += (mbti2.charAt(i)==mbti3.charAt(i)) ? 0 : 1;
        }
        return distance;
    }
}
