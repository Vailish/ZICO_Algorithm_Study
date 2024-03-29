package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Boj_5525_IOIOI_2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        String s = br.readLine();

        Map<Integer, Integer> pArray = new HashMap<>();
        String now = "";
        int o = 0;
        char word;
        char last;
        for (int i=0; i<m; i++) {
            word = s.charAt(i);
            if (now.isEmpty()) {
                if (word == 'I') {
                    now += "I";
                }
            } else {
                last = now.charAt(now.length()-1);
                if (last == 'I') {
                    if (word == 'I') {
                        if (o != 0) {
                            if (pArray.containsKey(o)) pArray.put(o, pArray.get(o)+1);
                            else pArray.put(o, 1);
                            o = 0;
                        }
                        now = "I";
                    } else { // word가 "O"인경우
                        now += "O"; o++;
                    }
                } else { // last가 "O"인경우
                    if (word == 'I') {
                        now += "I";
                    } else {
                        if (o > 1) {
                            if (pArray.containsKey(o-1)) pArray.put(o-1, pArray.get(o-1)+1);
                            else pArray.put(o-1, 1);
                        }
                        o = 0;
                        now = "";
                    }
                }
            }
        }
        if (o !=0) {
            last = now.charAt(now.length()-1);
            if (last == 'I') {
                if (pArray.containsKey(o)) pArray.put(o, pArray.get(o)+1);
                else pArray.put(o, 1);
            } else {
                if (pArray.containsKey(o-1)) pArray.put(o-1, pArray.get(o-1)+1);
                else pArray.put(o-1, 1);
            }
        }
        int answer = 0;
        for (int key:pArray.keySet()) {
            if (key >= n) {
                answer += (key-n+1) * pArray.get(key);
            }
        }
        System.out.println(answer);
    }
}
