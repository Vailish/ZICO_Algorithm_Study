package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_1107_리모컨 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int now = 100;
        int target = Integer.parseInt(br.readLine());

        boolean[] brokenNum = new boolean[10];
        String[] brokenNums = br.readLine().split(" ");
        for (String bNum : brokenNums) {
            brokenNum[Integer.parseInt(bNum)]= true;
        }
        //
        for (int i=0; i<99999 ; i++) {
            String channel = String.valueOf(i);
            boolean isBroken = false;
            for (int j=0; j<channel.length();j++){
//                if (brokenNum[channel.charAt(j)]) {

//                }
            }
        }

    }
}
