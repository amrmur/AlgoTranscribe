package Java;

import java.util.Arrays;

public class sort{
    public static void main(String[] args){
        int[] nums = {7,3,1,2,7,98,4,2,4,5,7,3,24,5};
        bubbleSort(nums);
        System.out.println(Arrays.toString(nums));
    }
    public static void selectionSort(int[] nums){
        int n = nums.length;
        for(int i = 0; i < n; i++){
            int low = i;
            for(int j = i+1; j < n; j++){
                if(nums[j] < nums[low]){
                    low = j;
                }
            }
            int temp = nums[i];
            nums[i] = nums[low];
            nums[low] = temp;
        }
    }
    public static void insertionSort(int[] nums){
        int n = nums.length;
        for(int i = 1; i < n; i++){
            int j = i;
            while(j > 0 && nums[j] < nums[j-1]){
                int temp = nums[j];
                nums[j] = nums[j-1];
                nums[j-1] = temp;
                j -= 1;
            }
        }
    }
    public static void bubbleSort(int[] nums){
        for(int i = 0; i < nums.length; i++){
            boolean swapped = false;
            for(int j = 1; j < nums.length - i; j++){
                if(nums[j] < nums[j-1]){
                    int temp = nums[j];
                    nums[j] = nums[j-1];
                    nums[j-1] = temp;
                    swapped = true;
                }
            }
            if(swapped == false){
                break;
            }
        }
    }
}