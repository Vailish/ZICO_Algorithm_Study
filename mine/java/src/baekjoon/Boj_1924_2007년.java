package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj_1924_2007년 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] day = br.readLine().split(" ");
        System.out.println(getWeek(Integer.parseInt(day[0]), Integer.parseInt(day[1])));
    }

    public static String getWeek(int month, int day) {
        int[] dayOfMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String[] weekDays = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};

        // 요일로 합치기
        int totalDay = day;

        for (int i=0; i<month-1; i++) {
            totalDay += dayOfMonth[i];
        }
        return weekDays[totalDay%7];
    }

}
