package hijava1_abstract_class;

public abstract class Software {
	public abstract void plan();
	public abstract void develope();
	public abstract void release();
	
	final void product() {
		plan();
		develope();
		release();
	}
}
