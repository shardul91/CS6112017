/**
 * @author Christelle
 * 
 */
public class ScannerDemo {

	private static String file1 = "prog2.jay";
	private static int counter = 1;

	public static void main(String args[]) {

		TokenStream ts = new TokenStream(file1);

		System.out.println("Scanning file :" + file1);

		while (!ts.isEndofFile()) {
			// TO BE COMPLETEDs
			Token t = ts.nextToken();
			System.out.println("Token "+ String.format("%02d", counter) +" - Type:" + t.getType() +" - Value:"+ t.getValue());
			counter = counter + 1;

		}
		
	}
}
