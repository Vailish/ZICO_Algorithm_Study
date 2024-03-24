package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj_5525_IOIOI_2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        String s = br.readLine();

        int answer = 0;

        String now = "";
        int o = 0;
        String word;
        String last;
        for (int i=0; i<m; i++) {
            word = String.valueOf(s.charAt(i));
            if (now.equals("")) {
                if (word.equals("I")) {
                    now += "I";
                }
            } else {
                last = String.valueOf(now.charAt(now.length()-1));
                if (last.equals("I")) {
                    if (word.equals("I")) {
                        if (o > 0) {
                            answer += o - n + 1;
                            o = 0;
                        }
                        now = "I";
                    } else { // word가 "O"인경우
                        now += "O"; o++;
                    }
                } else { // last가 "O"인경우
                    if (word.equals("I")) {
                        now += "I";
                    } else {
                        if (o > 1) answer += o - n;
                        o = 0;
                        now = "";
                    }
                }
            }
        }
        if (o !=0) {
            last = String.valueOf(now.charAt(now.length()-1));
            if (last.equals("I")) {
                answer += o - n + 1;
            } else {
                answer += o - n;
            }
        }

        System.out.println(answer);
    }
}
