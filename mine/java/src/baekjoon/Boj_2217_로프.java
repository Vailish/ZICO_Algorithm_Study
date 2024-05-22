package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Boj_2217_로프 {
    public static void main(String[] args) throws IOException {
        // 로프를 선택적으로 사용하여 버틸 수 있는 최대 중량을 구하는 문제
        // 내림차순으로 로프 정렬 -> 누적합 / 개수로 값을 구함
        // 해당 값 중 가장 큰 경우를 출력하면 됨
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for (int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);
        int answer = 0;
        int tmp;
        for (int i=1; i<n+1; i++) {
            tmp = arr[n-i] * i;
            if (answer < tmp) {
                answer = tmp;
            }
        }
        System.out.println(answer);
    }
}
