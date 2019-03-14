package hijava1_interface;

public class CalcImpl implements Calc {

	@Override
	public void add(int x, int y) {
		System.out.println(x + y);
	}

	@Override
	public void sub(int x, int y) {
		System.out.println(x - y);		
	}

	@Override
	public int mul(int x, int y) {
		System.out.println(x * y);
		return 0;
	}

	@Override
	public int div(int x, int y) {
		System.out.println(x / y);		
		return 0;
	}

}
