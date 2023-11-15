package baekjoon;

import java.util.ArrayList;
import java.util.Scanner;

public class Boj_9506_약수들의_합 {
    static void chk(int num) {
        ArrayList result = new ArrayList<Integer>();

        for (int i=1; i<num; i++) {
            if (num%i == 0) {
                result.add(i);
            }
        }
        int cnt = 0;
        StringBuilder sb = new StringBuilder();
        sb.append(num);

        for (int i=0; i< result.size(); i++) {
            cnt += (int) result.get(i);
        }

        if (cnt == num) {
            sb.append(" = ").append(result.get(0));
            for(int i=1; i<result.size(); i++) {
                sb.append(" + ").append(result.get(i));
            }
        } else {
            sb.append(" is NOT perfect.");
        }
        System.out.println(sb);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int n = sc.nextInt();
            if (n==-1) {return;}
            chk(n);
        }
    }
}
