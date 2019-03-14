package hijava;

public class LoopTest1 {

	public static void main(String[] args) {
		// 1 ~ 100 사이의 합
		int i = 0;
		int sum = 0;
		
		// i는 0부터 들어가서 비교 후에 1 증가한다. ++i <= 100 이 이 것과 같은 경우임.
		while(i++ < 100) {
			sum += i;
		}
		System.out.println("sum = " + sum);
		
		// 1 ~ 100 사이의 홀수의 합
		i = 0;
		sum = 0;

		while(i++ < 100) {
			if ((i % 2) == 0) continue;
			
			sum += i;
		}
		System.out.println("sum = " + sum);
		
	}
}
