import java.util.ArrayList;
import java.util.Dictionary;
import java.util.HashMap;
import java.util.List;

/**
 * Created with IntelliJ IDEA.
 * User: Christopher
 * Date: 10/03/13
 * Time: 4:46 PM
 * To change this template use File | Settings | File Templates.
 */
public class Random {
    public static void main(String args[]){
        HashMap dictionary = new HashMap<Integer, String>();
//        dictionary.put(0, "apple");
//        dictionary.put(1, "an");
//        dictionary.put(2, "pie");
//        dictionary.put(3, "a");
//        System.out.println(SpaceString("appleanpie", dictionary));

//        System.out.println(isPalindrome("asefa"));
//        System.out.println(isPalindrome("aba"));
//
//        System.out.println(removeChar("Booger", 'o'));
//
//        System.out.println(longestPalindrome("Polfeaabbaacccddccc"));

//        stringPermRecursive("abc");




    }

    public static String SpaceString(String s, HashMap<Integer, String> dict){
        for(int i = 0; i < dict.size(); i++){
            if(s.indexOf(dict.get(i)) == 0){
                String st = s.substring(0, dict.get(i).length());
                if(st.length() == s.length())
                    return st;
                else
                    return  st + " " + SpaceString(s.substring(st.length()), dict);
            }
        }
        return "";


    }

    public static boolean isPalindrome(String s){
        int i = 0,
            j = s.length()-1;
        while( i <= j){
            if(i == j ||s.charAt(i) != s.charAt(j))
                return false;
            i++;
            j--;
        }
        return true;
    }


    public static String removeChar(String s, char ch){
        String result = s;

        while(result.indexOf(ch)!= -1){
            int i = result.indexOf(ch);
            result = result.substring(0,i) + result.substring(i +1);
        }
        return result;

    }

    public static String longestPalindrome(String s){
        ArrayList palindromes = new ArrayList<String>();
        for(int i = 0; i < s.length(); i++){
            for(int j =i;j < s.length(); j++){
                if(isPalindrome(s.substring(i, j+1))){
                    palindromes.add(s.substring(i, j+1));
                }
            }
        }
        if(palindromes.size()>0){
            int longest = 0;
            for(int i = 0; i < palindromes.size(); i++){
                if(((String)palindromes.get(i)).length() > ((String)palindromes.get(longest)).length())
                    longest = i;
            }
            return (String)(palindromes.get(longest));
        }
        else
            return "";
    }

    public static String stringPermRecursive(String s){
        if(s.length() == 0){
            return "";
        }
        else {
            for(int i = 0; i < s.length(); i++){

            }

        }
        return "";

    }
}
