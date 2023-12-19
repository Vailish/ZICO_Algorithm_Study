package baekjoon;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Boj_28279_덱_2 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Deque<Integer> dq = new ArrayDeque<>();
        StringBuilder answer = new StringBuilder();
        for (int i=0; i<N; i++) {
            int num = sc.nextInt();
            switch (num) {
                case 1:
                    dq.offerFirst(sc.nextInt()); break;
                case 2:
                    dq.offer(sc.nextInt()); break;
                case 3:
                    if (dq.isEmpty()) answer.append(-1).append("\n");
                    else answer.append(dq.pollFirst()).append("\n"); break;
                case 4:
                    if (dq.isEmpty()) answer.append(-1).append("\n");
                    else answer.append(dq.pollLast()).append("\n"); break;
                case 5:
                    answer.append(dq.size()).append("\n"); break;
                case 6:
                    if (dq.isEmpty()) answer.append(1).append("\n");
                    else answer.append(0).append("\n"); break;
                case 7:
                    if (!dq.isEmpty()) answer.append(dq.peekFirst()).append("\n");
                    else answer.append(-1).append("\n");break;
                case 8:
                    if (!dq.isEmpty()) answer.append(dq.peekLast()).append("\n");
                    else answer.append(-1).append("\n");break;
            }
        }
        System.out.print(answer);
    }
}
