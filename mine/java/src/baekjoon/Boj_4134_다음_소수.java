package baekjoon;

import java.math.BigInteger;
import java.util.Scanner;

public class Boj_4134_다음_소수 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < n; i++) {
            BigInteger num = sc.nextBigInteger();
            answer.append(chk(num)).append("\n");
        }
        System.out.println(answer);
    }

    static BigInteger chk(BigInteger n) {
        if (n.isProbablePrime(10) == true) {
            return n;
        } else {return n.nextProbablePrime();}
    }
}
//    시간초과
//    static long chk(long k) {
//        long n = k;
//        if (n<3) {
//            return n+1;
//        }
//        while (true) {
//            long c = 1;
//            for (long idx=2; idx<n; idx++) {
//                if (n%idx==0) {
//                    break;
//                } else {
//                    c++;
//                }
//            }
//            if (c==n-1) {
//                return n;
//            } else {
//                n++;
//            }
//
//        }
//    }
//}
