class Solution {
    
    public long solution(int r1, int r2) {
        
        long answer = 0;
        
        double R1 = Math.pow(r1,2);
        double R2 = Math.pow(r2,2);
        
        for (int x = 1; x<=r2 ; x++){
            double X = Math.pow(x,2);
            
            double y1 = Math.sqrt(R1-X);
            double y2 = Math.sqrt(R2-X);
            
            if (Double.isNaN(y1)) {
                y1 = 0;
            }
            
            double Y1 = Math.ceil(y1);
            double Y2 = Math.floor(y2);

            answer += ((Y2-Y1)+1);
        }
        
        answer *= 4;
        return answer;
    }
}

/*
문제 https://school.programmers.co.kr/learn/courses/30/lessons/181187?language=java#

처음에는 이중 for문으로 최대한 효율적으로 해보려고 했는데 시간초과가 났다.

x 값을 for문으로 돌면서 그 때의 r1의 y1값, r2의 y2값을 구한다.
y1보다 큰 최소 정수, y2보다 작은 최대 정수를 구해서 그 사이 값들만 카운트해준다.

이렇게 해 주면 1사분면의 정수 좌표값을 구할 수 있으므로 최종적으로는 *4를 해 주면 된다.
*/
