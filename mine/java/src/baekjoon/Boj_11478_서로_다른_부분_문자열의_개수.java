package baekjoon;

import java.util.HashSet;
import java.util.Scanner;

public class Boj_11478_서로_다른_부분_문자열의_개수 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String st = sc.next();
        HashSet<String> stringSet = new HashSet<>();
        for (int i=0; i<=st.length(); i++) {
            for (int j=i; j<=st.length(); j++) {
                stringSet.add(st.substring(i,j));
            }
        }
        System.out.println(stringSet.size()-1);
    }
}
