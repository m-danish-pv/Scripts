package TNG;

import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

public class testNG {

				
	@Test
	public void Demo()
	{
		System.out.println("1");
		
	}
	
	@BeforeTest
	public void second() {
		
		System.out.println("1.2");
	}

}
