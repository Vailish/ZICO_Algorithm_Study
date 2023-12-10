package baekjoon;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class Boj_18870_좌표_압축 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];

        for (int i=0; i<n; i++) {
            nums[i] = sc.nextInt();
        }
        int[] sortedNums = nums.clone();
        Arrays.sort(sortedNums);

        HashMap<Integer, Integer> chk = new HashMap<>();
        int k = 0;
        for (int num : sortedNums) {
            if (!chk.containsKey(num)) {
                chk.put(num,k);
                k++;
            }
        }

        StringBuilder answer = new StringBuilder();
        for (int num : nums) {
            answer.append(chk.get(num)).append(" ");
        }

        System.out.println(answer);
    }
}
