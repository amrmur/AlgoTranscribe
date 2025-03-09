package Java;

import java.util.Arrays;

public class mergeSort{
    public static void main(String[] args){
        int[] nums = {7,4,5,7,8,9,35,76,33,1,34,88,32,11,12};
        nums = mergesort(nums);
        System.out.println(Arrays.toString(nums));
    }
    public static int[] mergesort(int[] nums){
        int n = nums.length;
        if(n <= 1) return nums;
        int half = n / 2;
        int[] first = mergesort(Arrays.copyOfRange(nums, 0, half)), second = mergesort(Arrays.copyOfRange(nums, half, n));

        int f = 0, s = 0, lenf = first.length, lens = second.length;

        for(int i = 0; i < n; i++){
            if(s >= lens || f < lenf && first[f] < second[s]){
                nums[i] = first[f];
                f += 1;
            } else {
                nums[i] = second[s];
                s += 1;
            }
        }
        return nums;
    }
}
