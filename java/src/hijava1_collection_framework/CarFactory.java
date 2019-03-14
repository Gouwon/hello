package hijava1_collection_framework;

import java.util.HashMap;
import java.util.Map;

public class CarFactory {

	private static CarFactory _instance;
	
	// hashmap 선언 : 상위인 map을 이용하여 다형성을 고려하여 만듦.
	private Map<String, Car> mapCar = new HashMap<String, Car>();
	
	// default 생성자
	private CarFactory () {
		
	}
	
	public static CarFactory getInstance() {
		if (_instance == null ) _instance = new CarFactory();
		return _instance;
	}

	public Car createCar(String name) {
		// TODO Auto-generated method stub
		
//		1번 방법 
//		if (mapCar.containsKey(name)) {
//			return mapCar.get(name);
//		}
//		else {
//			Car car = new Car(name);
//			mapCar.put(name, car);
//			return car;
		
//		2번 방법 
		if (!mapCar.containsKey(name)) 
			mapCar.put(name,  new Car(name));
		
			return mapCar.get(name);
		
	}
}
