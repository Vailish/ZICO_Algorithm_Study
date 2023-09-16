package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj_10811_바구니뒤집기 {

    static int[] myMethod(int[] array, int a, int b){
        int[] myArr = array;

        // b부터 a까지
        int pointA = a-1;
        int pointB = b-1;
        int tmp;

        while (pointA < pointB) {
            tmp = myArr[pointA];
            myArr[pointA] = myArr[pointB];
            myArr[pointB] = tmp;

            pointA += 1;
            pointB -= 1;
        }

        return myArr;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        for (int i=0 ; i<n; i++){
            arr[i] = i+1;
        }

        for (int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            arr = myMethod(arr, start, end);
        }

        StringBuilder answer = new StringBuilder();
        for (int num: arr) {
            answer.append(num).append(" ");
        }

        System.out.println(answer);
    }
}
