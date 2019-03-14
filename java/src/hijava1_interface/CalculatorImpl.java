package hijava1_interface;

public class CalculatorImpl implements Calculator {

	@Override
	public void add(int i, int j) {
		System.out.println(i + j);
	}

	@Override
	public void sub(int i, int j) {
		System.out.println(i - j);
	}

	@Override
	public void mul(int i, int j) {
		System.out.println(i * j);
	}

	@Override
	public void div(int i, int j) {
		if (j == 0) System.out.println("Cannot divide Zero!");
		else System.out.println(1 / j);
	}

}
