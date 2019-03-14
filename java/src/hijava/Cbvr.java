package hijava;

public class Cbvr {
	int m = 2;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i = 1;
		System.out.println("i(before function) = " + i);
		
		
		int r = change1(i);
		System.out.println("i(after function) = " + i);
		System.out.println("change1(i) = " + r);
		
		Cbvr cb = new Cbvr();
		System.out.println("Cbvr cb.m(before function) = " + cb.m);
		change2(cb);
		System.out.println("Cbvr cb.m(after function) = " + cb.m);
	}
	
	public static int change1(int x) {
		System.out.println("i(function input) = " + x);
		x = 100;
		System.out.println("in function " + x);
		return x;
	}

	public static void change2(Cbvr x) {
		x.m = 100;
	}
}
