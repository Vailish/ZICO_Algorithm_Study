import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        String helloStr = "1";
        String[] helloStrArr = helloStr.split("");
        System.out.println(Arrays.toString(helloStrArr));
        int[] resultIntArr = new int[helloStrArr.length];

        for (int i = 0; i < helloStrArr.length; i++) {
            int helloItemNum = helloStrArr[i].charAt(0);
            resultIntArr[i] = helloItemNum;
        }
        System.out.println("resultIntArr :: " + Arrays.toString(resultIntArr));  // [104, 101, 108, 108, 111]
    }
}
