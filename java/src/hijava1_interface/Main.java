package hijava1_interface;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		calc(4, 2);

		Total t = new TotalImpl();
		int[] nums = { 1, 2, 3, 4 };
		int r = t.sum(nums);
		System.out.println(r);

		calcoper();
	}

	private static void calcoper() {
		CalcOper o = new CalcOper();
		int x = 10;
		int y = 2;

		int a1 = o.add(x, y);
		int a2 = o.sub(x, y);
		int a3 = o.mul(x, y);
		int a4 = o.div(x, y);
		int[] arr = new int[] { a1, a2, a3, a4 };
		for (int i : arr)
			System.out.println(i);
	}

	private static void calc(int i, int j) {
		Calculator c = new CalculatorImpl();

		c.add(i, j);
		c.sub(i, j);
		c.mul(i, j);
		c.div(i, j);

		Scanner scan = new Scanner(System.in);
		String p = scan.next();
//		System.out.println(p);
		System.out.println("입력 메시지: \"" + p + "\"");

	}

}
