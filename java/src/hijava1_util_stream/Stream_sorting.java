package hijava1_util_stream;

import java.util.Comparator;
import hijava.Student;

public class Stream_sorting implements Comparator<Student> {
	@Override
	public int compare(Student o1, Student o2) {
//		return o1.getStudentId() - o2.getStudentId();	// 학번으로 
		return o1.getName().compareTo(o2.getName());	// 이름으로 
	}
}

