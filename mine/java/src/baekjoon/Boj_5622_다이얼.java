package baekjoon;

import java.util.*;

public class Boj_5622_다이얼 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char[] word = sc.next().toCharArray();

        List<String> dial = new ArrayList<>(Arrays.asList("","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"));
        StringBuilder result = new StringBuilder();

        for (int i=0;i<word.length;i++){
            String targetWord = String.valueOf(word[i]);

            boolean chk = false;
            for (int j=0; j<dial.size();j++){
                char[] st = dial.get(j).toCharArray();
                if (chk == false) {
                    for(int k=0;k<dial.get(j).length();k++){
                        String chr = String.valueOf(st[k]);

                        if (chr.equals(targetWord)){
                            result.append(j);
                            break;
                        }
                    }
                } else {
                    break;
                }
            }
        }

        int answer = 0;
        for (int i=0; i<result.length();i++) {
            answer += Integer.parseInt(String.valueOf(result.charAt(i))) + 1;
        }

        System.out.println(answer);

    }
}
