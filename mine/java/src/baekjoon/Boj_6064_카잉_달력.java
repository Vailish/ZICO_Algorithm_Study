package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj_6064_카잉_달력 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int caseNum = Integer.parseInt(br.readLine());
        StringTokenizer st;
        for (int c=0; c<caseNum; c++) {
            st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int answer=-1;

            // 카잉달력
            if (y==N) y=0;

            int index = 0;
            while(M*index+x<=M*N){
                if((M*index+x)%N==y){
                    answer = M*index +x;
                    break;
                }
                index++;
            }
            System.out.println(answer);
        }
    }
}