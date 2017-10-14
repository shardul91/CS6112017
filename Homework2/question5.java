package recursion;

import java.util.Scanner;

public class question5 {

		public static void main(String[] args) {
		
		int base = 2;
		float result;
				
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter the power : ");
		int n = scanner.nextInt();

		result = recPow(base,n);
		
		System.out.println("2 ^ "+ n + " = " + result);
	
	}
		
		public static float recPow (int base, int n) {
			
			if(n > 0)		// when power is positive
			{
				return (base*recPow(base,n -1));
			}
			else if (n<0) 	// when power is negative	
			{
				return 1/ (base *recPow(base,-n-1));
			}
			else			// when power is zero
				return 1;
		}

}
