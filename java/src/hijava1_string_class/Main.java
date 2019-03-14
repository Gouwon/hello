package hijava1_string_class;

public class Main {
	
	public static void main(String[] argv) throws CloneNotSupportedException {
		Student s1 = new Student();
		s1.setInfo("홍길동", 921234);
		System.out.println(s1);
		
		Student s2 = new Student("김일수", 921233);
		System.out.println(s2);
		
		Student s3 = new Student("홍길동", 921234);
		System.out.println(s3);
		
		System.out.println(s2.equals(s1));	// false
		System.out.println(s3.equals(s1));	// true
		
		Student s4 = (Student) s1.clone();
		System.out.println(s4);
	}
}
