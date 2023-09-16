package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj_25304_영수증 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int totalPrice = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());
        int price = 0;

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            price += Integer.parseInt(st.nextToken()) * Integer.parseInt(st.nextToken());
        }

        if (totalPrice==price){
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
    }
}
