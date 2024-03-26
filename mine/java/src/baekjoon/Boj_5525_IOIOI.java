package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj_5525_IOIOI { // 50점 시간초과
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        String s = br.readLine();

        int[] pArray = new int[1000001];

        String now = "";
        int o = 0;
        String word = "";
        String last = "";
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
                        if (o != 0) {
                            pArray[o]++;
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
                        if (o > 1) pArray[o-1]++;
                        o = 0;
                        now = "";
                    }
                }
            }
        }
        if (o !=0) {
            last = String.valueOf(now.charAt(now.length()-1));
            if (last.equals("I")) {
                pArray[o]++;
            } else {
                pArray[o-1]++;
            }
        }
        int answer = 0;
        for (int i=n; i<1000001; i++) {
            answer += (i-n+1) * pArray[i];
        }
        System.out.println(answer);
    }
}
