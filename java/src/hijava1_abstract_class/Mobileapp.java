package hijava1_abstract_class;

public class Mobileapp extends Software{

	@Override
	public void plan() {
		System.out.println("App design");
	}

	@Override
	public void develope() {
		System.out.println("Android + iOS");
	}

	@Override
	public void release() {
		System.out.println("Google PlayStore + Apple AppStore");
	}

}
