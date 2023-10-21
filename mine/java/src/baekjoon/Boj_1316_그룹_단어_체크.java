package baekjoon;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Boj_1316_그룹_단어_체크 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int answer = n;

        // 케이스별로 하나씩 진행
        for (int i=0; i<n; i++) {
            String word = sc.next();
            List<String> chks = new ArrayList<>();
            String exWord = "";

            boolean chk = false;
            // 한 글자씩 확인 aba
            for (int j=0; j<word.length(); j++) {
                String targetWord = String.valueOf(word.charAt(j));

                // 연속된 문자는 패스
                if (targetWord.equals(exWord)) {
                    continue;
                }

                // 기존에 나왔던 문자이면 그룹단어에서 제외하고 중지
                for (int k=0; k<chks.size(); k++) {
                    if (targetWord.equals(chks.get(k))){
                        answer -= 1;
                        chk = true;
                        break;
                    }
                }
                if (chk) {break;}

                chks.add(targetWord);
                exWord = targetWord;

            }

        }
        System.out.println(answer);
    }
}
