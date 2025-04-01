package Java;

import java.util.Arrays;

public class countInv{
    public static void main(String[] args){
        int[] nums = {5,2,7,4,9,3,1,0};
        Object[] output = mergesort(nums);
        System.out.println(output[1]);
    }
    public static Object[] mergesort(int[] nums){
        int n = nums.length;
        if(n <= 1) return new Object[]{nums, 0};
        int half = n / 2;
        Object[] fout = mergesort(Arrays.copyOfRange(nums, 0, half));
        Object[] sout = mergesort(Arrays.copyOfRange(nums, half, n));
        int[] first = (int[])fout[0];
        int[] second = (int[])sout[0];

        int f = 0, s = 0, lenf = first.length, lens = second.length;
        int inv = (int)fout[1] + (int)sout[1];

        for(int i = 0; i < n; i++){
            if(s >= lens || f < lenf && first[f] < second[s]){
                nums[i] = first[f];
                f += 1;
            } else {
                inv = inv + lenf - f;
                nums[i] = second[s];
                s += 1;
            }
        }
        return new Object[]{nums, inv};
    }
}
