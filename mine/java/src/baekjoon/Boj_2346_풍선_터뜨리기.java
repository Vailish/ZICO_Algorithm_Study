package baekjoon;

import java.util.*;

public class Boj_2346_풍선_터뜨리기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Integer> value = new ArrayList<>();
        List<Integer> num = new ArrayList<>();
        for (int i=0; i<n; i++) {
            value.add(sc.nextInt());
            num.add(i+1);
        }
        StringBuilder answer = new StringBuilder();
        int i = 0;
        while (!value.isEmpty()) {
            answer.append(num.get(i)).append(" ");
            int v = value.get(i); // 종이 안의 수 구하기
            value.remove(i); // 터친 풍선 처리
            num.remove(i);
            if (value.isEmpty()) break;
            if (v>0) i = (i+v-1)%value.size();
            else {
                i = (i+v)%value.size();
                if (i<0) i+=value.size();
            }
        }
        System.out.println(answer);
    }
}
