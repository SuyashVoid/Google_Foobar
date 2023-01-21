package reIdLvl1;

public class Solution{
    // This is an O(n) solution since Sieve of atkin in itself is O(n), and stringBuilder
    // that ensures O(n) for n appeneds to get the ptime string. Then, finally 5 appends to build a string
    // Here, n is the guesstimated limit of what i could need, i.e (i+5)log(i+5) + (i+5)log(log(i+5)

    public static String solution(int i) {
        StringBuilder id = new StringBuilder();
        int toFindTill = i+5;
        // Guesstimated limit is nlogn + nlogLogn
        int estimatedLimit = (int) (toFindTill * Math.log(toFindTill) + toFindTill * Math.log(Math.log(toFindTill)));
        if(i<6) estimatedLimit = 40;
        String primeNums = sieveOfAtkin(estimatedLimit);
        for(int j=i;j<i+5;j++)id.append(primeNums.charAt(j));
        return id.toString();
    }
    // Standard sieve of atkin from geekforgeeks
    static String sieveOfAtkin(int limit)
    {
        StringBuilder primeNums = new StringBuilder();
        if (limit > 2)
            primeNums.append("2");

        if (limit > 3)
            primeNums.append("3");

        boolean sieve[] = new boolean[limit+1];

        for (int i = 0; i <= limit; i++)
            sieve[i] = false;

        for (int x = 1; x * x <= limit; x++) {
            for (int y = 1; y * y <= limit; y++) {

                // reIdLvl1.Main part of Sieve of Atkin
                int n = (4 * x * x) + (y * y);
                if (n <= limit
                        && (n % 12 == 1 || n % 12 == 5))

                    sieve[n] ^= true;

                n = (3 * x * x) + (y * y);
                if (n <= limit && n % 12 == 7)
                    sieve[n] ^= true;

                n = (3 * x * x) - (y * y);
                if (x > y && n <= limit
                        && n % 12 == 11)
                    sieve[n] ^= true;
            }
        }

        // Mark all multiples of squares as
        // non-prime
        for (int r = 5; r * r <= limit; r++) {
            if (sieve[r]) {
                for (int i = r * r; i <= limit;
                     i += r * r)
                    sieve[i] = false;
            }
        }

        // Print primes using sieve[]
        for (int a = 5; a <= limit; a++)
            if (sieve[a])
                primeNums.append(a);
        return primeNums.toString();
    }
}