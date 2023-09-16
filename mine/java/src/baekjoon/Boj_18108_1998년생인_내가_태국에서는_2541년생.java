package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj_18108_1998년생인_내가_태국에서는_2541년생 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String tmp = br.readLine();
        int num = Integer.parseInt(tmp);

        System.out.println(num-(2541-1998));
    }

}
