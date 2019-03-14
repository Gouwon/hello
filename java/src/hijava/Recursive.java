package hijava;

public class Recursive {
	public static void main(String[] argv) {
		int inum = 10;
		for(int i = 0; i <= inum; i++) {
			System.out.print("result = " + fibo(i) + " ");			
		}
	}

//	private static int fibo(int num) {
//
//		if (num == 1)
//			return 1;
//		if (num == 0)
//			return 0;
//		int result = fibo(num - 1) + fibo(num - 2);
//
//		return result;
//	}

	private static int fibo(int num) {
		if(num <= 1) return num;
		
		return fibo(num - 1) + fibo(num - 2);
		
//		if (num > 1)
//			return fibo(num - 1) + fibo(num - 2);
//		else
//			return num;
	}
}
