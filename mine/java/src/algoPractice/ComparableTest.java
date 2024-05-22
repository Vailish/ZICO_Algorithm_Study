package algoPractice;


import java.util.Arrays;

public class ComparableTest {
    static class Element implements Comparable<Element>{
        int value;
        int index;

        Element(int value, int index){
            this.value = value;
            this.index = index;
        }

        @Override
        public int compareTo(Element o) {
//            if (this.value == o.value) return this.index - o.index;
//            return this.value - o.value;
            if (this.value == o.value) return - this.index + o.index;
            return - this.value + o.value;
        }
    }
    public static void main(String[] args) {
        Element[] elements = {
                new Element(10, 0),
                new Element(11, 1),
                new Element(12, 2),
                new Element(13, 3),
                new Element(14, 4),
        };
        Arrays.sort(elements);
        for (Element element : elements) {
            System.out.printf("value = %s, index = %s \n", element.value, element.index);
        }
    }
}
