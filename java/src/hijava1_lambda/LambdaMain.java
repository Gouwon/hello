package hijava1_lambda;

public class LambdaMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		calculator(10 , 0);
//		int i = 1;
//		System.out.println(i);
//		int x = i++;
//		System.out.println(x);
		
	}

	private static void calculator(int i, int j) {
		// TODO Auto-generated method stub
		Lambda add = (x, y) -> x + y;
		Lambda sub = (x, y) -> x - y;
		Lambda mul = (x, y) -> x * y;
		Lambda div = (x, y) -> (x == 0 || y == 0)? 0: x / y;
		
//		show(x, y);
		System.out.println(add.calc(i, j));
		System.out.println(sub.calc(i, j));
		System.out.println(mul.calc(i, j));
		System.out.println(div.calc(i, j));
	}		
	
}
