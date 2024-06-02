package algoPractice;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class ComparatorTest {
    public static void main(String[] args) {
        List<Integer> lst = new ArrayList<>(List.of(1, 10, 2, 9, 3, 7, 4, 6, 5));
        lst.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return - o1 + o2;
            }
        });
        System.out.println(lst);
    }
}
