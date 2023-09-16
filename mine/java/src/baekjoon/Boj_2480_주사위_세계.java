package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj_2480_주사위_세계 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] val = br.readLine().split(" ");
        StringBuilder answer = new StringBuilder();

        int numA = Integer.parseInt(val[0]);
        int numB = Integer.parseInt(val[1]);
        int numC = Integer.parseInt(val[2]);
        int[] nums = {numA, numB, numC};

        // 최대값 구하기
        int max = numA;

        for (int num : nums) {
            if (max < num){
                max = num;
            }
        }

        // 같은 개수 확인하기
        // 3개가 같은 경우
        if (numA == numB && numB == numC){
            answer.append(10000 + 1000 * max);
            // 모두 다른 경우
        } else if(
                (numA != numB && numB != numC && numA != numC)
        ) {
            answer.append(100 * max);
            // 2개가 같은 경우
        } else {
            int dupNum;
            if (numA == numB) {
                dupNum = numA;
            } else if (numB == numC) {
                dupNum = numB;
                // numA == numC
            } else {
                dupNum = numC;
            }
            answer.append(1000 + 100*dupNum);

        }

        System.out.println(answer);

    }
}
