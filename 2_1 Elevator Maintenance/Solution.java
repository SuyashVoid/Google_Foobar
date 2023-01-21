package ElevatorMaintenanceLvl2;
// This solution is O(nlogn) time and O(n) space since it uses mergeSort alongside a custom comparator (function) to sort the array.
public class Solution {
    public static String[] solution(String[] l) {
        mergeSort(l, l.length);
        return l;
    }
    public static int compareVersion(String version1, String version2)
    {
        // First split the string into tokens using the delimiter "."
        String[] arr1 = version1.split("\\.");
        String[] arr2 = version2.split("\\.");
        int actualLength1 = arr1.length;
        int actualLength2 = arr2.length;
        // Now make a fully qualified version of the version strings i.e they have the same number of tokens
        String[] fullyQualified1 = new String[]{"0", "0", "0"};
        String[] fullyQualified2 = new String[]{"0", "0", "0"};
        // Copy the tokens from the original array to the fully qualified array
        System.arraycopy(arr1, 0, fullyQualified1, 0, actualLength1);
        System.arraycopy(arr2, 0, fullyQualified2, 0, actualLength2);

        // Now compare the tokens
        for (int i = 0; i < fullyQualified1.length; i++)
        {
            if(Integer.parseInt(fullyQualified1[i]) < Integer.parseInt(fullyQualified2[i]))
                return -1;
            if(Integer.parseInt(fullyQualified1[i]) > Integer.parseInt(fullyQualified2[i]))
                return 1;
        }
        // If we reach here, it means that the versions are equal but their actual length may have been different
        // Which is why we do a final check here, Integer.compare will return 0 if the lengths are equal and -1 or 1 otherwise
        return Integer.compare(actualLength1, actualLength2);
    }

    // Slightly modified mergeSort algorithm to use the custom comparator
    public static void mergeSort(String[] a, int n) {
        if (n < 2) {
            return;
        }
        int mid = n / 2;
        String[] l = new String[mid];
        String[] r = new String[n - mid];

        System.arraycopy(a, 0, l, 0, mid);
        if (n - mid >= 0) System.arraycopy(a, mid, r, 0, n - mid);
        mergeSort(l, mid);
        mergeSort(r, n - mid);

        merge(a, l, r, mid, n - mid);
    }

    public static void merge(String[] a, String[] l, String[] r, int left, int right) {

        int i = 0, j = 0, k = 0;
        while (i < left && j < right) {
            // Here is the modification to use the custom comparator
            if (compareVersion(l[i], r[j]) <= 0) {
                a[k++] = l[i++];
            }
            else {
                a[k++] = r[j++];
            }
        }
        while (i < left) {
            a[k++] = l[i++];
        }
        while (j < right) {
            a[k++] = r[j++];
        }
    }
}
