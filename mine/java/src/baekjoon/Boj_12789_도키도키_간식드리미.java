package baekjoon;

import java.util.Scanner;
import java.util.Stack;

public class Boj_12789_도키도키_간식드리미 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];

        for (int i=0; i<n; i++) {
            nums[i] = sc.nextInt();
        }
        Stack<Integer> stack = new Stack<>();
        int idx=1;
        for (int i=0; i<n; i++) {
            if (nums[i] != idx) {
                if (!stack.isEmpty() && stack.peek() == idx) {
                    stack.pop();
                    i--;
                    idx++;
                } else {
                    stack.push(nums[i]);
                }
            } else {
                idx++;
            }
        }
        while (idx <= n) {
            int k = stack.pop();
            if (idx != k) {
                System.out.println("Sad");
                return;
            }
            idx++;
        }
        System.out.println("Nice");
    }
}

