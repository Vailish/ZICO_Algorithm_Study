package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Boj_5525_IOIOI_3 {
    public static void main(String[] args) throws IOException { // 시간초과, 문자열을 기준으로 하지말자
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        String s = br.readLine();

        Map<Integer, Integer> countingMap = new HashMap<>();
        char word;
        int cnt=0; // IOIOIOIOI순으로만 들어감, last도 cnt 수로 알 수 있음, 홀수 = 'I', 짝수 = 'O'
        for (int i=0; i<m; i++) {
            word = s.charAt(i);
            if (cnt == 0) { // cnt는 IOIOIOI... 순으로 쌓이는 문자의 수 -> 무조건 맞는 경우만 세고, 나머지는 예외처리하겠다
                if (word == 'I') {
                    cnt = 1;
                }
            } else {
                if (cnt%2 == 1) { // ...I
                    if (word == 'I') {
                        // I IOI IOIOI
                        // 3->1 5->2 7->3 n->n/2
                        if (!countingMap.containsKey(cnt/2)) countingMap.put(cnt/2, 0);
                        countingMap.put(cnt/2,countingMap.get(cnt/2)+1);
                        cnt = 1;
                    } else { // word가 "O"인경우
                        ++cnt;
                    }
                } else { // ...O
                    if (word == 'I') {
                        ++cnt;
                    } else { //...O가 나옴
                        // IO, IOIO, IOIOIO
                        // 2->0, 4->1 6->2, n->(n-1)/2
                        --cnt;
                        if (!countingMap.containsKey(cnt/2)) countingMap.put(cnt/2, 0);
                        countingMap.put(cnt/2,countingMap.get(cnt/2)+1);
                        cnt = 0;
                    }
                }
            }
        }
        if (cnt !=0) {
            if (cnt%2==0)--cnt;
            if (!countingMap.containsKey(cnt/2)) countingMap.put(cnt/2, 0);
            countingMap.put(cnt/2,countingMap.get(cnt/2)+1);
        }
        int answer = 0;
        for (int key:countingMap.keySet()) {
            if (key >= n) {
                answer += (key-n+1) * countingMap.get(key);
            }
        }
        System.out.println(answer);
    }
}