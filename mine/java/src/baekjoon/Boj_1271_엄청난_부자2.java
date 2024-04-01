package baekjoon;

import java.math.BigInteger;
import java.util.Scanner;

public class Boj_1271_엄청난_부자2 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        BigInteger a = sc.nextBigInteger();
        BigInteger b = sc.nextBigInteger();
        System.out.println(a.divide(b));
        System.out.println(a.remainder(b));
    }
}
