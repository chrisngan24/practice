/**
 * Created with IntelliJ IDEA.
 * User: Christopher
 * Date: 11/03/13
 * Time: 2:54 PM
 * To change this template use File | Settings | File Templates.
 */
public class ArrayPractice {
    public static void main(String args[]){
        int[] array = {10,2,3,5,7,6,4,1,8, 10};
        int[] sortedArray = {1,1,2,3,4,5};
//        System.out.println(missingNumber(array));
        System.out.println(duplicateNumber(array));

        printArray(RemoveDuplicates(sortedArray));

    }

    public static void printArray(int[] array){
        for(int i = 0; i< array.length; i++){
            System.out.println(array[i]);
        }
    }

    public static int[] RemoveDuplicates(int[] array){
        int[] x = new int[array.length];
        for (int i = 1; i < n; i++) {




        }

    public static int missingNumber(int[] array){
        for(int i =1; i <= array.length+1; i++){
            boolean isFound = false;
            for(int j =0; j < array.length; j++){
                if(i == array[j])
                    isFound = true;
            }
            if(!isFound)
                return i;
        }
        return -1;
    }

    public static int duplicateNumber(int[] array){
        for(int i = 0; i < array.length; i++){
            for(int j = i; j < array.length; j++){
                if(array[j] == array[i])
                    return array[i];
            }
        }
        return -1;
    }


}
