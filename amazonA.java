package Amazon_A;

import java.time.Duration;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class amazonA {

	public static void main(String[] args) throws InterruptedException {
		System.setProperty("webdriver.chrome.driver", "D:\\Selenium\\chromedriver_win32\\chromedriver.exe");
		String[] names = { "Cucumber", "Brocolli" ,"Brinjal"};
		WebDriver driver = new ChromeDriver();
		
		
		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
		
		
		String baseUrl = "https://rahulshettyacademy.com/seleniumPractise/#/";
		driver.get(baseUrl);
		driver.manage().window().maximize();
		Thread.sleep(3000);
		amazonA obj = new amazonA();
		obj.itemsNeeded(driver, names);
		driver.findElement(By.xpath("//img[@alt='Cart']")).click();
		driver.findElement(By.xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]")).click();
		driver.findElement(By.cssSelector("input.promoCode")).sendKeys("rahulshett academy");
		driver.findElement(By.cssSelector("button.promoBtn")).click();

		WebDriverWait w = new WebDriverWait(driver, Duration.ofSeconds(5));
		w.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector("span.promoInfo")));
		
		String Code = driver.findElement(By.cssSelector("span.promoInfo")).getText();
		
		
		if(Code.equals("Invalid code ..!"))
		{
			System.out.println("Matched");
		}
		else {System.out.println("Not Matched");}
	}
	
public void itemsNeeded(WebDriver driver,String[] names)
{
	
	List<WebElement> products = driver.findElements(By.cssSelector("h4.product-name"));
	int j=0;
	for (int i = 0; i < products.size(); i++) {
		String[] productName = products.get(i).getText().split("-");
		String formatName = productName[0].trim();

		List<String> itemsNeeded = Arrays.asList(names);
		
		if (itemsNeeded.contains(formatName))
		{
			driver.findElements(By.xpath("//div[@class='product-action']/button")).get(i).click();
			j++;
			if(j==names.length)
			{
				break;
			}
		}
	}

}

}
