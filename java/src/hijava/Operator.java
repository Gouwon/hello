package hijava;

public class Operator {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i = 0;
		i += 1;	// i = i + 1 <==> i++
		System.out.println(i);
		i *= 10;	// i = 1 * 10
		System.out.println(i);
		
		int k = !(i > 0) ? 100 : 1000;
		System.out.println(k);
		
		i++;
		i--;
		int j = i++;
		System.out.println(i++ + ", j = " + j + " % " + (i % 2));
		
		
		int num1 = 10;
		int num2 = 20;
		boolean result;
		
		result = ((num1 > 10) && (num2 > 10));	// 거짓, 참 => 거짓
		System.out.println(result);
		result = ((num1 > 10) || (num2 > 10));	// 거짓, 참 => 참
		System.out.println(result);
		System.out.println(!result);	// !참 => 거짓
	}

}
