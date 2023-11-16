package baekjoon;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class Boj_2750_수_정렬하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Integer> nums = new ArrayList<>();
        for (int i=0;i<n;i++) {
            nums.add(sc.nextInt());
        }
        nums.sort(Comparator.naturalOrder());
        for (int i=0; i<n; i++) {
            System.out.println(nums.get(i));
        }
    }
}
