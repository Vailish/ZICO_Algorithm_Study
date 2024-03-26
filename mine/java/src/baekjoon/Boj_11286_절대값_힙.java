package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Boj_11286_절대값_힙 {
    public static void main(String[] args) throws IOException {
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>((o1, o2) -> {
            int absO1 = Math.abs(o1);
            int absO2 = Math.abs(o2);

            if (absO1==absO2) return o1 > o2 ? 1 : -1;
            else return absO1 - absO2;
        });

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder answer = new StringBuilder();
        for (int i=0; i<n; i++) {
            int k = Integer.parseInt(br.readLine());
            if (k==0) {
                if (heap.isEmpty()) answer.append(0).append("\n");
                else answer.append(heap.poll()).append("\n");
            } else heap.add(k);
        }
        System.out.println(answer);
    }
}