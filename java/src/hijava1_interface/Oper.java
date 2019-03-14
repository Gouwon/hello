package hijava1_interface;

public class Oper {
	public int add(int x, int y) {
		return (x + y);
	}
	
	public int sub(int x, int y) {
		return (x - y);
	}
	
	public int mul(int x, int y) {
//		int[] arr = new int[y];
//		int result = 0;
//		for (int i : arr) {
//			result = add(result, x);
//		}
//		
//		return result;
		
		int result = 0;
		for (int i = 0; i < y; i++) {
			result = add(result, x);
		}
		return result;
	}
	
	public int div(int x, int y) {
		if (y == 0) {
			System.out.println("Error");
			return 0;
		}
		else {
			int result = 0;
			while(x >= y)
			{
				x -= y;
				result++;
			}

			return result;
		}
	}
}
