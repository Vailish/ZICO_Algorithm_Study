package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class Boj_1427_소트인사이드 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String stringNum = sc.next();
        int idx = 0;
        int[] nums = new int[stringNum.length()];
        while (idx < stringNum.length()) {
            nums[idx] = Integer.valueOf(stringNum.charAt(idx)-48);
            idx ++;
        }
        Arrays.sort(nums);
        StringBuilder answer = new StringBuilder();
        for (int i=nums.length-1; i>-1; i--) {
            answer.append(nums[i]);
        }
        System.out.println(answer);
    }
}
