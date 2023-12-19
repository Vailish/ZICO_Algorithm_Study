package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;

public interface Boj_28278_스택_2 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Integer> stack = new Stack<>();
        StringBuilder answer = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        int[] inputs;
        for (int i=0; i<n; i++) {
            inputs = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            switch (inputs[0]) {
                case 1:
                    stack.push(inputs[1]); break;
                case 2:
                    if (stack.empty()) answer.append(-1).append("\n");
                    else answer.append(stack.pop()).append("\n"); break;
                case 3:
                    answer.append(stack.size()).append("\n"); break;
                case 4:
                    if (stack.empty()) answer.append(1).append("\n");
                    else answer.append(0).append("\n"); break;
                case 5:
                    if (!stack.empty()) answer.append(stack.peek()).append("\n");
                    else answer.append(-1).append("\n");
            }
        }
        System.out.println(answer);
    }
}
