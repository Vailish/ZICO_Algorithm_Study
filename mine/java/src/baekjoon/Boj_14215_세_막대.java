package baekjoon;

import java.util.*;

public class Boj_14215_세_막대 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> nums = new ArrayList<>(List.of(sc.nextInt(), sc.nextInt(), sc.nextInt()));
        nums.sort(Comparator.naturalOrder());
        int a = nums.get(0);
        int b = nums.get(1);
        int c = nums.get(2);

        if (c >= a + b) {
            System.out.println((a+b) * 2 - 1);
        } else {
            System.out.println(a+b+c);
        }
    }
}

