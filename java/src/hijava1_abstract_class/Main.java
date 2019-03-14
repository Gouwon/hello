package hijava1_abstract_class;

public class Main {

	public static void main(String[] args) {
		
		Weight g = new Geun();
		Weight p = new Pound();
		
		int gg = g.getGram(1);
		int pp = p.getGram(1);
		
		System.out.println(gg + " " + pp);
		
		Animal c = new Cat();
		Animal d = new Dog();
		
		c.bark();
		d.bark();
		
		Software w = new Website();
		Software m = new Mobileapp();
		
		w.product();
		m.product();
		
	}

}
