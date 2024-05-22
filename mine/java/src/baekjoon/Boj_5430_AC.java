package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Boj_5430_AC {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int caseNum = Integer.parseInt(br.readLine());
        for (int c=0; c<caseNum; c++) {
            String p = br.readLine();
            int n = Integer.parseInt(br.readLine());
            String string = br.readLine();
            String[] rawArray = string.substring(1,string.length()-1).split(",");
            int[] array = new int[rawArray.length];
            boolean chk=false;
            for (int i=0; i<rawArray.length;i++) {
                if (rawArray[i].isEmpty()) {
                    chk=true; break;
                }
                array[i] = Integer.parseInt(rawArray[i]);
            }
            if (chk) {
                System.out.println("error");
                continue;
            }
            // AC 객체생성 및 명령어 주입
            AC obj = new AC(array);
            obj.commands(p);
            obj.print();
        }
    }
    private static class AC {
        private List<Integer> lst;

        private boolean isError;

        private boolean isReverse;

        public void print() {
            if (isError) {
                System.out.println("error");
            } else {
                if (isReverse && lst.size()>1) {
                    StringBuilder sb = new StringBuilder();
                    sb.append("[");
                    for (int i=lst.size()-1; i>=0; i--) {
                        sb.append(lst.get(i)).append(",");
                    }
                    sb.deleteCharAt(sb.length()-1).append("]");
                    System.out.println(sb);
                } else {
                    System.out.println(lst);
                }
            }
        }
        public AC(int[] array) {
            lst = new ArrayList<>();
            for (int val : array) {
                lst.add(val);
            }

            isError = false;
            isReverse = false;
        }

        public void commands(String commands) {
            for (int i=0; i<commands.length(); i++) {
                switch (commands.charAt(i)) {
                    case 'R':
                        if (isReverse) isReverse=false;
                        else isReverse = true;
                        break;
                    case 'D':
                        if (lst.size()<2) {
                            isError=true; break;
                        }
                        if (isReverse) {
                            lst.remove(lst.size()-1);
                        }
                        else {
                            lst.remove(0);
                        }
                }
                if (isError) return;
            }
        }
        public void drop() {
            if (lst.size()<2 || isError) {
                isError = true; return;
            }
            lst.remove(0);
        }
    }
}
