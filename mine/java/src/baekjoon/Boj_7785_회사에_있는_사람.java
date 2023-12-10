package baekjoon;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

public class Boj_7785_회사에_있는_사람 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        HashMap<String, Boolean> attendance = new HashMap<>();
        for (int i=0; i<n; i++) {
            String name = sc.next();
            String status = sc.next();
            if (!attendance.containsKey(name)) {
                attendance.put(name, true);
            } else {
                if (attendance.get(name)) {
                    attendance.put(name,false);
                } else {attendance.put(name,true);}
            }
        }
        Object[] keys = attendance.keySet().toArray();
        Arrays.sort(keys, Collections.reverseOrder());
        StringBuilder answer = new StringBuilder();
        for (Object key : keys) {
            if (attendance.get(key)) {
                answer.append(key).append("\n");
            }
        }
        System.out.println(answer);
    }
}
