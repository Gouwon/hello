package hijava;

public class Number {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		byte b = 1;
		short s = 1;
		int i = 1;
		long l = 2345678901111l;
		
		System.out.println("Byte range : " + Byte.MIN_VALUE + " ~ " + Byte.MAX_VALUE);
		System.out.println("Short range : " + Short.MIN_VALUE + " ~ "  + Short.MAX_VALUE);
		System.out.println("Integer range : " + Integer.MIN_VALUE + " ~ "  + Integer.MAX_VALUE);
		System.out.println("Long range : " + Long.MIN_VALUE + " ~ "  + Long.MAX_VALUE);
		
		int x = 10;
		float y = 2.0f;
		int r1 = (int)(x + y);
		int r2 = (int)(x - y);
		int r3 = (int)(x * y);
		int r4 = (int)(x / y);

		System.out.println(r1 + " / " + r2 + " / " + r3 + " / " + r4);
		
		int z = (int)(12.4 % 3);
		System.out.println(z);
		
	}

}
