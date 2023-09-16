import java.util.Arrays;

public class test {

    static int[] myMethod(int[] arr){
        int[] array = arr;
        int a = 0;
        int b = 1;
        int tmp = arr[a];
        array[a] = array[b];
        array[b] = tmp;
        System.out.println(Arrays.toString(array));

        return array;
    }


    public static void main(String[] args) {
//        int[] yop = {1, 2};
//        ;
//        System.out.println(Arrays.toString(myMethod(yop)));


    }
}
