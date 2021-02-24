public class Test {

    public static void main(String[] args) {
        String tempStr;
        String test = "n";
        char temp = 'a';
        for (int i = 0; i < 26; i++) {
            tempStr = Character.toString(temp);
            temp++;

            System.out.println(tempStr.compareTo(test) > 0);
        }

    }

}
