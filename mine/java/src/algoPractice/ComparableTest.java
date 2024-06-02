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

//            if (this.value == o.value) return - this.index + o.index;
//            return + this.value - o.value;

            if (this.index == o.index) return - this.value + o.value;
            return - this.index + o.index;
        }
    }
    public static void main(String[] args) {
        Element[] elements = {
                new Element(10000, 0),
                new Element(1000, 1),
                new Element(100, 2),
                new Element(10, 3),
                new Element(1, 4),
        };
        Arrays.sort(elements);
        for (Element element : elements) {
            System.out.printf("value = %s, index = %s \n", element.value, element.index);
        }
    }
}
