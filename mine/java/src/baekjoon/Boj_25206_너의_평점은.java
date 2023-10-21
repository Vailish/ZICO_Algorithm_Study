package baekjoon;

import java.util.Scanner;

public class Boj_25206_너의_평점은 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double result = 0;
        int numberOfSubject = 20;
        double totalNum = 0;
        for (int i=0; i<20; i++) {
            String[] score = sc.nextLine().split(" ");
            // 점수들을 받아서 P인지 확인
            if (score[2].equals("P")) {
                numberOfSubject -= 1; continue;
            }
            double num = Double.parseDouble(score[1]);
            totalNum += num;
            // P가 아니면 계산값에 넣어줌
            double points;
            switch (score[2]) {
                case "A+":
                    points = 4.5; break;
                case "A0":
                    points = 4.0; break;
                case "B+":
                    points = 3.5; break;
                case "B0":
                    points = 3.0; break;
                case "C+":
                    points = 2.5; break;
                case "C0":
                    points = 2.0; break;
                case "D+":
                    points = 1.5; break;
                case "D0":
                    points = 1.0; break;
                default: // "F"
                    points = 0; break;
            }
            result += num * points;
        }

        Double avgScore = result / totalNum;
        // 답출력
        System.out.println(avgScore);

    }
}
