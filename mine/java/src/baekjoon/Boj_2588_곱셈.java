package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Boj_2588_곱셈 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int numA = Integer.parseInt(br.readLine());
        String numB = br.readLine();

        StringBuilder answer = new StringBuilder();
        char[] tmp = numB.toCharArray();
        answer.append(numA * (tmp[2]-'0'));
        answer.append('\n');
        answer.append(numA * (tmp[1]-'0'));
        answer.append('\n');
        answer.append(numA * (tmp[0]-'0'));
        answer.append('\n');
        answer.append(numA * Integer.parseInt(numB));
        System.out.println(answer);
    }
}
