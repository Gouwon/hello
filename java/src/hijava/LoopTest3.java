package hijava;

public class LoopTest3 {
	public static void main(String[] args) {
		int total = 0;
		for(int i = 2; i <= 100; i++) {
			boolean isPrime = true;
			for(int j = 2; j <= (i - 1); j++) {
				if(i % j == 0) {
					isPrime = false;
					break;
				}
			}
			
			if(isPrime) {
				total += i;
			}
		}
		
		System.out.println(total);
	}
}
