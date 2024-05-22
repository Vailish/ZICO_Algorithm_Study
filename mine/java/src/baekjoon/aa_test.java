package baekjoon;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Iterator;
import java.util.regex.Pattern;

public class aa_test {
    public static void main(String[] args) {
        System.out.println("테스트 시작!");
        convertTest();
        System.out.println("테스트 종료!");
    }
    public static void convertTest() {
//        String dateString = "2024-04-09 15:58:44.0";
        String dateString = "2024-04-09T06:58:44.000+00:00";
//        String pattern = "\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}\\.\\d";
        String pattern = "\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}\\+\\d{2}:\\d{2}";

        if (Pattern.matches(pattern, dateString)) {
            System.out.println("주어진 문자열은 날짜 형식을 따릅니다.");
        } else {
            System.out.println("주어진 문자열은 날짜 형식을 따르지 않습니다.");
        }
    }
    public static void cal() {
        Calendar wNow = Calendar.getInstance();
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyyMMdd");
        String today = simpleDateFormat.format(wNow.getTime());
        today = "20241230";


        int unavailablePeriod = 2;
        int[] last = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        String unavailableLastDay = today.substring(0,6) + (Integer.parseInt(today.substring(6))+unavailablePeriod);
        int wYear = Integer.parseInt(unavailableLastDay.substring(0,4));

        if((wYear%4 == 0 && wYear%100 != 0) || wYear%400 == 0) {
            last[1] = 29;
        }
        // 변수할당
        int cYear = Integer.parseInt(unavailableLastDay.substring(0,4));
        int cMonth = Integer.parseInt(unavailableLastDay.substring(4,6));
        int cDay = Integer.parseInt(unavailableLastDay.substring(6));
        // 확인
        if (cDay > last[cMonth-1]) {
            int tmp = cMonth;
            cMonth = cMonth + cDay/last[cMonth-1];
            cDay = cDay%last[tmp-1];

            if (cMonth > 12) {
                cYear = cYear + cMonth/12;
                cMonth = cMonth%12;
            }
        }
        unavailableLastDay = cYear
                + (cMonth < 10 ? "0" : "")+ cMonth
                + (cDay < 10 ? "0" : "") + cDay;

        System.out.println(unavailableLastDay);
    }

    public static void testForCalendar() {
        SimpleDateFormat currDay = new SimpleDateFormat("yyyyMMdd");
        Calendar c1 = Calendar.getInstance();
        System.out.println(currDay.format(c1.getTime()).substring(4,6));
//        System.out.println("owo");
//        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyyMMdd");
//        Calendar calendar = Calendar.getInstance();
//
//        String str = simpleDateFormat.format(calendar.getTime());
//        System.out.println(str);
//        System.out.println("ㅇㅅㅇ");
//        System.out.println(Calendar.DAY_OF_WEEK);
//        System.out.println("ㅇㅅㅇ");
//        System.out.println(calendar.getTime());
//        System.out.println(Calendar.YEAR);
    }

    public static void a() {
        System.out.println(10/12);
        ArrayList<Integer> a = new ArrayList<>();
        a.add(1);
        a.add(2);
        Iterator<Integer> b = a.iterator();

        while(b.hasNext()){
            System.out.println(b.next());
            int s = b.next();
        }
    }
}
