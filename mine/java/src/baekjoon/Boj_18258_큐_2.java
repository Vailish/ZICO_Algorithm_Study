package baekjoon;

import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;

public class Boj_18258_큐_2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Deque<Integer> q = new LinkedList<>();
        int n = sc.nextInt();
        StringBuilder answer = new StringBuilder();
        for (int i=0; i<n; i++) {
            String v = sc.next();
            switch (v) {
                case "push":
                    q.offer(Integer.parseInt(sc.next())); break;
                case "pop":
                    if (q.isEmpty()) answer.append(-1).append("\n");
                    else answer.append(q.poll()).append("\n"); break;
                case "size":
                    answer.append(q.size()).append("\n"); break;
                case "empty":
                    if (q.isEmpty()) answer.append(1).append("\n");
                    else answer.append(0).append("\n");break;
                case "front":
                    if (!q.isEmpty()) answer.append(q.peekFirst()).append("\n");
                    else answer.append(-1).append("\n"); break;
                case "back":
                    if (!q.isEmpty()) answer.append(q.peekLast()).append("\n");
                    else answer.append(-1).append("\n"); break;
            }
        }
        System.out.println(answer);
    }
}
