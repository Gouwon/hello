package hijava;

public class LoopTest2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		show99dan();
//		showStair(10);
//		showReverseStair(10);
//		showPyramid(10);
		getPrimeNumber();
		
	}

	private static void getPrimeNumber() {
		// TODO Auto-generated method stub
		int sum = 0;
		
		for(int i = 0; i <= 100; i++) {
			
			if(i == 2) {
				sum += i;
				continue;
			}
			
			else if(i % 2 == 0) continue;
			
			else {
				
				for(int j = 2; j <= (i - 1); j++) {
					
					if( i % j == 0) break;
					
					else if(j == i - 1) 
		                sum += i;
				}
			}
		}
		
		System.out.println("Prime Number total = " + sum);
	}

	private static void showPyramid(int line) {
		// TODO Auto-generated method stub
		for(int i = 1; i <= line; i++) {
			
			for(int j = 1; j <= (line - i); j++) {
				System.out.print(" ");
			}
			
			for(int j = 1; j <= (i * 2 - 1); j++) {
				System.out.print("*");
			}
			
			System.out.println("");
		}
	}

	private static void showReverseStair(int line) {
		// TODO Auto-generated method stub
		for(int i = 1; i <= line; i++) {
			
			for (int j = line; j > i; j--) {
				System.out.print(" ");
			}
			
			for(int k = 1; k <= i; k++) {
				System.out.print("*");
			}
			
			System.out.println("");
		}
	}

	private static void showStair(int line) {
		// TODO Auto-generated method stub
		for(int i = 1; i <= line; i++) {
			
			for (int j = 1; j <= i; j++) {
				System.out.print('*');
			}
			
			System.out.println("");
		}
	}

	private static void show99dan() {
		// TODO Auto-generated method stub
		for(int i = 2; i <= 9; i++) {
			System.out.println("----- " + i + "단 -----");
			
			for(int j = 1; j <= 9; j++) {
				System.out.println(i + " * " + j + " = " + (i * j));
			}
		}
	}
}
