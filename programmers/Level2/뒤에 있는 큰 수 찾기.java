/*
버전1
*/

import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {

        int[] answer = new int[n];
        Arrays.fill(answer,-1);
        int n = numbers.length;
        
        Deque<int[]> stack = new LinkedList<>();
        stack.push(new int[]{0,numbers[0]});

        
        for (int idx = 1; idx < n ; idx++){
            int value = numbers[idx];

            int[] pre = stack.peek();
            int preValue = Integer.MAX_VALUE;

            if (pre != null){
                preValue = pre[1];
            }
            
            while(preValue<value){
                
                int[] idx_value = stack.pop();
                answer[idx_value[0]] = value;
                pre = stack.peek();
                
                if (pre == null){
                    preValue = Integer.MAX_VALUE;
                }
                else{
                    preValue = pre[1];
                }
            }
            
            stack.push(new int[]{idx,value});
        }
        
        return answer;
    }
}

/*
stack을 이용해서 풀었다. 
앞에서부터 {idx,value}를 stack 넣어주고 for문을 돌면서 현재 값과 stack에 저장되어 있는 값들을 비교해주었다.
현재 값이 더 크면 stack에서 꺼내 answer에 현재 값을 저장해주었다.


TIL
자바에서 stack을 구현할 때는 
Deque<Integer> stack = new ArrayDeque<>();
- 빠름 (push(), pop() 모두 O(1))
- null을 허용하지 않음 (버그 방지)

Deque<Integer> stack = new LinkedList<>();
1. push() / pop() 모두 O(1)
2. 메모리 절약 가능 (연결 리스트 기반)
3. peek() → 맨 위(Top) 값을 조회 (제거 X) -> 스택이 비어 있으면 null 반환

앞으로 stack은 LinkedList를 써야겠다.
*/



/*
버전2 -> 하나 시간초과
*/

import java.util.*;
class Solution {
    public int[] solution(int[] numbers) { 
        int n = numbers.length;
        int max_value = numbers[n-1];
        int max_idx = n-1;
        int value_idx = n-1;
        int[] answer = new int[n];
        answer[n-1] = -1;
        
        for(int idx = n-2; idx>=0; idx--){
            int value = numbers[idx];
            if (value>=max_value){
                answer[idx] = -1;
                max_value = value;
                max_idx = idx;
                continue;
            }
            
            for(int i = idx+1; i<=max_idx;i++){
                if (value<numbers[i]){
                    answer[idx] = numbers[i];
                    break;
                }
                if (value<answer[idx+1]){
                    answer[idx] = answer[i];
                    break;
                }
            }
           
        }
        
        
        return answer;
    }
}
