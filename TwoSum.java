import java.util.Arrays;
import java.util.HashMap;

public class TwoSum {

    // brute force search
    public static int[] twosum(int[] arr, int target) {

        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] + arr[j] == target) {
                    return new int[] { i, j };
                }
            }
        }
        return new int[] {};// no solution

    }

    // optimized way
    public static int[] twosum_optimize(int[] arr, int target) {

        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            int complemnt = target - arr[i];
            if (map.containsKey(complemnt)) {
                return new int[] { map.get(complemnt), i };
            }
            map.put(arr[i], i);
        }
        return new int[] {};// no answer
    }

    public static char firstUniqueChar(String s) {
        for (int i = 0; i < s.length(); i++) {
            boolean isUnique = true;

            for (int j = 0; j < s.length(); j++) {
                if (i != j && s.charAt(i) == s.charAt(j)) {
                    isUnique = false;
                    break;
                }
            }

            if (isUnique) {
                return s.charAt(i);
            }
        }
        return '_';
    }

    public static void reverse(int[] arr) {

        int left = 0;
        int right = arr.length - 1;
        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            left++;
            right--;
        }
    }

    public static void main(String[] args) {
        int[] nums = { 2, 7, 11, 15 };
        int target = 22;

        int[] result = twosum_optimize(nums, target);
        System.out.println(Arrays.toString(result)); // [1, 3]
        System.out.println(firstUniqueChar("swiss")); // w

        int[] arr = { 1, 2, 3, 4, 5 };
        reverse(arr);

        for (int num : arr) {
            System.out.print(num + " ");
        }

    }
}
