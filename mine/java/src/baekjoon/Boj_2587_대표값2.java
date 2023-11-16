package baekjoon;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

public class Boj_2587_대표값2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> nums = new ArrayList<>();
        int sum=0;
        int num;
        for (int i=0;i<5;i++) {
            num = sc.nextInt();
            nums.add(num);
            sum += num;
        }
        nums.sort(Comparator.naturalOrder());
        System.out.println(sum/5);
        System.out.println(nums.get(2));
    }
}
