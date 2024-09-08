package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Boj_1439_뒤집기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nums = br.readLine();

        // 0 -> 0으로 변환 횟수, 1 -> 1으로 변환 횟수
        int[] result = new int[2];

        char exNum = nums.charAt(0);
        char nowNum;


        // 연속된 녀석들을 하나로 묶어서 카운트
        for (int i=0; i<nums.length(); i++) {
            nowNum = nums.charAt(i);
            System.out.println(exNum + " " +nowNum);
            if (exNum != nowNum) {
                exNum = nowNum;
                // result 채워넣기
                result[exNum=='0' ? 1 : 0]++;
            }
        }
        System.out.println("답");
        System.out.println(Math.min(result[0],result[1]));
    }
}
//0001100