package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj_2525_오븐_시계 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");

        int hour = Integer.parseInt(inputs[0]);
        int min = Integer.parseInt(inputs[1]) + Integer.parseInt(br.readLine());

        // 분 처리
        if (min >= 60) {
            hour += min / 60;
            min = min % 60;
        }

        // 시 처리
        if (hour >= 24) {
            hour -= 24;
        }

        System.out.println(hour + " " + min);
    }
}
