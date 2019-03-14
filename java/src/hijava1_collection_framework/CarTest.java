package hijava1_collection_framework;

public class CarTest {
	
	public static void main(String[] args) {
		CarFactory factory = CarFactory.getInstance();
		Car sonata1 = factory.createCar("연수 차");
		Car sonata2 = factory.createCar("연수 차");
//		Car car1 = CarFactory.getInstance().createCar("실무용 코드")
//		같은 주소인지 확인.
		System.out.println(sonata1 == sonata2);
		
		Car avante1 = factory.createCar("승연 차");
		Car avante2 = factory.createCar("승연 차");
		System.out.println(avante1 == avante2);
		
		System.out.println(sonata1 == avante1);
	}
}
