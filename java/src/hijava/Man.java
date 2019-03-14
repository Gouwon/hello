package hijava;

public class Man {
	public static final int DOUGHNUT = 2500;
	public static final int COFFEE = 3000;
	private String name;
	private int amount = 10000;

	public Man() {

	}

//	public Man(String name) {
//		this.setName(name);
//	}
	
	public Man(String name) {
		this();
		this.setName(name);
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAmount() {
		return amount;
	}

	public void setAmount(int amount) {
		this.amount = amount;
	}

	public int buyCoffee(int count) {
//		this.amount -= COFFEE * count;
		this.subAmount(COFFEE, count);
		return this.amount;
	}

	public int buyDoughnut(int count) {
//		this.amount -= DOUGHNUT * count;
		this.subAmount(DOUGHNUT, count);
		return this.amount;
	}
	
	private void subAmount(int price, int count) {
		this.amount -= price * count;
	}
	
	@Override
	public String toString() {
		return "Man [name=" + name + ", amount=" + amount + "]";
	}

	public static void main(String argv[]) {

		Man hong = new Man("hong");
		hong.buyCoffee(1);
		hong.buyDoughnut(2);
		System.out.println(hong.toString());

		Man john = new Man("john");
		john.buyCoffee(2);
		john.buyDoughnut(1);
		System.out.println(john.toString());
	}

}
