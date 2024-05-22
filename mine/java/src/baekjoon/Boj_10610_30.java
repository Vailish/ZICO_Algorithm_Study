package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Boj_10610_30 {
    public static void main(String[] args) throws IOException {
        // 주어진 입력값을 문자열처럼 옮겨 붙여서 30의 배수를 만들고
        // 그 중에서 제일 큰 값을 출력하는 것
        // 30의 배수 판별법
        // 10의 배수이기때문에 0이 포함되어야함
        // 3의 배수이기 때문에 모든 합이 3의 배수여야함
        int answer = -1;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nums = br.readLine();
        if (nums.contains("0")) {
            int sum = 0;
            for (int i=0; i<nums.length(); i++) {
                sum += Integer.parseInt(String.valueOf(nums.charAt(i)));
            }
            if (sum % 3 == 0) {
                // 정렬
                List<Integer> tmp = new ArrayList<>();
                for (int i=0; i<nums.length(); i++) {
                    tmp.add(Integer.parseInt(String.valueOf(nums.charAt(i))));
                }
                tmp.sort(Collections.reverseOrder());
                for (int i=0; i<tmp.size(); i++) {
                    System.out.print(tmp.get(i));
                }
                return;
            }
        }
        System.out.println(-1);
    }
}
