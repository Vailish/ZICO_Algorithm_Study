package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Boj_1026_보물 {
    public static void main(String[] args) throws IOException {
        // B를 오름차순으로 정렬한 후
        // A는 반대로 내림차수로 정렬한 다음에
        // 계산하면 최소값이 된다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        int[] arrA = new int[n];
        int[] arrB = new int[n];
        for (int i=0; i<n; i++) {
            arrA[i] = Integer.parseInt(st1.nextToken());
            arrB[i] = Integer.parseInt(st2.nextToken());
        }
        Arrays.sort(arrA);
        Arrays.sort(arrB);
        int answer = 0;
        for (int i=0; i<n; i++){
            answer += arrA[n-i-1] * arrB[i];
        }
        System.out.println(answer);
    }
}
