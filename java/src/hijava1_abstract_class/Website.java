package hijava1_abstract_class;

public class Website extends Software {

	@Override
	public void plan() {
		System.out.println("Web design");
	}

	@Override
	public void develope() {
		System.out.println("HTML + CSS + JS");
	}

	@Override
	public void release() {
		System.out.println("Open");
	}

}
