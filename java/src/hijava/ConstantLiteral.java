package hijava;

public class ConstantLiteral {
	public static final int STU_NUM = 10;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		final String s = "abc";
		String x = add1(s);
		System.out.println(s);
		System.out.println(x);
	}
	
	public static String add1(String x) {
		x = x + "1";
		System.out.println(">>>>>>>>>>>" + x);
		return x;
	}
}
