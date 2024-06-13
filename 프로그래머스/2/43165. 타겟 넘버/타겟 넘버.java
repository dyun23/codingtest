import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int result = 0;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        for (int num : numbers){
            int size = queue.size();
            for (int i = 0; i <= size-1; i++){
                int value = queue.poll();
                queue.add(value + num);
                queue.add(value - num);
            }
        }
        for (int q : queue){
            if (q == target) result++;
        }
        return result;
    }
}