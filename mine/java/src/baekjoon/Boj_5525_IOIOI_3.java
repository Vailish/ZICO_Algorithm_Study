//package baekjoon;
//
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.HashMap;
//import java.util.Map;
//
//public class Boj_5525_IOIOI_3 {
//    public static void main(String[] args) throws IOException { // 시간초과, 문자열을 기준으로 하지말자
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int n = Integer.parseInt(br.readLine());
//        int m = Integer.parseInt(br.readLine());
//        String s = br.readLine();
//
//        Map<Integer, Integer> pArray = new HashMap<>();
//        char word;
//        int cnt=0; // IOIOIOIOI순으로만 들어감, last도 cnt 수로 알 수 있음,홀수 = 'I', 짝수 = 'O'
//        for (int i=0; i<m; i++) {
//            word = s.charAt(i);
//            if (cnt == 0) { //
//                if (word == 'I') {
//                    ++cnt;
//                }
//            } else {
//                if (cnt%2 == 1) { // ...I
//                    if (word == 'I') {
//                       // O으로 끝날 경우만 피해주면 됨
//                       // MAP에 IOIOIOI에서 O의 개수로 계산
//
//                        if (o != 0) {
//                            if (pArray.containsKey(o)) pArray.put(o, pArray.get(o)+1);
//                            else pArray.put(o, 1);
//                            o = 0;
//                        }
//                        cnt = 0;
//                    } else { // word가 "O"인경우
//                        ++cnt;
//                    }
//                } else { // ...O
//                    if (word == 'I') {
//                        now += "I";
//                    } else {
//                        if (o > 1) {
//                            if (pArray.containsKey(o-1)) pArray.put(o-1, pArray.get(o-1)+1);
//                            else pArray.put(o-1, 1);
//                        }
//                        cnt =0;
//                    }
//                }
//            }
//        }
//        if (o !=0) {
//            last = now.charAt(now.length()-1);
//            if (last == 'I') {
//                if (pArray.containsKey(o)) pArray.put(o, pArray.get(o)+1);
//                else pArray.put(o, 1);
//            } else {
//                if (pArray.containsKey(o-1)) pArray.put(o-1, pArray.get(o-1)+1);
//                else pArray.put(o-1, 1);
//            }
//        }
//        int answer = 0;
//        for (int key:pArray.keySet()) {
//            if (key >= n) {
//                answer += (key-n+1) * pArray.get(key);
//            }
//        }
//        System.out.println(answer);
//    }
//}
