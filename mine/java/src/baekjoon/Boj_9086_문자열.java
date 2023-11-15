package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj_9086_문자열 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        StringBuilder answer = new StringBuilder();
        for (int i=0;i<num;i++){
            String chr = br.readLine();
            answer.append(chr.charAt(0)).append(chr.charAt(chr.length()-1)).append("\n");
        }
        System.out.println(answer);

    }
}
