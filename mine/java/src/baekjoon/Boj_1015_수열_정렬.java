package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Boj_1015_수열_정렬 {
    static class Element implements Comparable<Element> {
        int value;
        int index;

        Element(int value, int index) {
            this.value = value;
            this.index = index;
        }

        @Override
        public int compareTo(Element o) {
            if (this.value == o.value) {
                return this.index - o.index;
            }
            return this.value - o.value;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Element[] elements = new Element[n];
        int[] p = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            elements[i] = new Element(Integer.parseInt(st.nextToken()), i);
        }

        Arrays.sort(elements);

        for (int i=0; i<n; i++) {
            p[elements[i].index] = i;
        }

        // 결과 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(p[i]).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}