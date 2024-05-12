package programmers;

import java.util.Arrays;
import java.util.List;

public class prog_258712_가장_많이_받은_선물 {
    public static void main(String[] args) {
        System.out.println(
            solution(
                    new String[]{"muzi", "ryan", "frodo", "neo"},
                    new String[]{"muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"}
            )
        );
    }
    public static int solution(String[] friends, String[] gifts) {
        int answer = 0;
        List<String> friendList = Arrays.asList(friends);
        System.out.println(friendList);
        // giftMap 생성
        int[][] giftMap = new int[friends.length][friends.length];
        for (String gift : gifts) {
            String[] tmp = gift.split(" ");
            giftMap[friendList.indexOf(tmp[0])][friendList.indexOf(tmp[1])]++;
        }
        System.out.println(Arrays.deepToString(giftMap));

        // 다음달 확인
        int[] result = new int[friends.length];
        for (int i=0; i<friends.length; i++) {
            for (int j=0; j<friends.length; j++) {
                if (i>j) {
                    if (giftMap[i][j] > giftMap[j][i]) {
                        result[i]++;
                    } else if (giftMap[i][j] < giftMap[j][i]) {
                        result[j]++;
                    } else {
                        int iSum=0; int jSum=0;
                        for (int k=0; k<friends.length; k++) {
                            iSum += giftMap[i][k] - giftMap[k][i];
                            jSum += giftMap[j][k] - giftMap[k][j];
                        }
                        if (iSum>jSum) {
                            result[i]++;
                        } else if (iSum<jSum) {
                            result[j]++;
                        }
                    }
                }
            }
        }
        for (int num : result) {
            if (num > answer) answer=num;
        }
        return answer;
    }
}
