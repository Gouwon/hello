package hijava1_util_stream;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.IntStream;

import hijava.Student;

public class Main {
	public static void main(String[] args) {
//		test1();
//		test2();
		
		try_this();
	}

	private static void try_this() {
		// TODO Auto-generated method stub
//		아래 학생들의 이름을 출력하시오.
//		성적의 총점과 평균을 구하시오.(sum, average)
//		학생중 성적이 90점 이상인 학생의 이름을 정렬하여 출력하시오.
		
		List<Student> students = new ArrayList<>();
		students.add(new Student(100, "Hong100", 80));
		students.add(new Student(20, "Lim20", 100));
		students.add(new Student(5, "Lee5", 70));
		
		students.stream().map(s -> s.getName()).forEach(n -> System.out.println(n));
		students.forEach(s -> System.out.println("name=" + s.getName()));
		
		int sum = students.stream().map(s -> s.getScore()).reduce(0, (p, n) -> p + n);
		System.out.println("sum=" + sum);
		
		Student[] arr = new Student[students.size()];
		students.toArray(arr);
		IntStream ids = Arrays.stream(arr).mapToInt(s -> s.getScore());
		
		int sum1 = Arrays.stream(arr).mapToInt(s -> s.getScore()).sum();
		System.out.println("sum1=" + sum1);
		
		double avg = Arrays.stream(arr).mapToInt(s -> s.getScore()).average().getAsDouble();
		System.out.println(students.stream().map(s -> s.getScore()));
		System.out.println("avg=" + avg);
		
		Arrays.stream(arr).filter(s -> s.getScore()>=90).sorted().forEach(s ->System.out.println(s.getName()));		

	}

	private static void test2() {
		// TODO Auto-generated method stub
		int[] arr = new int[] { 2, 3, 1, 5, 3, 2 };
		System.out.println("avg=" + Arrays.stream(arr).average().getAsDouble());
		Arrays.stream(arr).sorted().forEach(n -> System.out.println(n));
		Arrays.stream(arr).distinct().forEach(n -> System.out.println("distinct=" + n));
		Arrays.stream(arr).filter(n -> n > 2).forEach(n -> System.out.println(n));
		Arrays.stream(arr).reduce(0, (p, n) -> p + n);

	}

	private static void test1() {
		List<Student> students = new ArrayList<>();
		students.add(new Student(100, "Hong100"));
		students.add(new Student(20, "Lim20"));
		students.add(new Student(5, "Lee5"));
		
		System.out.println(students);
		System.out.println("----------------------------");
		Collections.sort(students, new Stream_sorting());
		System.out.println(students);
		
		students.stream().map(s -> s.getName()).forEach(n -> System.out.println(n));
		students.stream().mapToInt(s -> s.getStudentId()).sum();
	}
}