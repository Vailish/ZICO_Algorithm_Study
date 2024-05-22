package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Boj_2752_세수정렬 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br. readLine());
        int[] nums = new int[3];
        nums[0] = Integer.parseInt(st.nextToken());
        nums[1] = Integer.parseInt(st.nextToken());
        nums[2] = Integer.parseInt(st.nextToken());
        Arrays.sort(nums);
        for (int num : nums) {
            System.out.print(num + " ");
        }
    }
}
