public class Karatsuba{
    public static void main(String[] args){
        System.out.println(karatsuba(1234, 5678));
        System.out.println(karatsuba(123,567));
    }

    public static int karatsuba(int x, int y){
        if(x < 10 && y < 10){
            return x * y;
        }
        int nHalved = Math.max(String.valueOf(x).length(), String.valueOf(y).length())/2;
        int a = x / (int)Math.pow(10, nHalved);
        int b = x % (int)Math.pow(10, nHalved);
        int c = y / (int)Math.pow(10, nHalved);
        int d = y % (int)Math.pow(10, nHalved);
        int p = a + b, q = c + d;
        int ac = karatsuba(a, c), bd = karatsuba(b, d);
        int pq = karatsuba(p, q);
        return ac * (int)Math.pow(10, nHalved*2) + (pq - ac - bd) * (int)Math.pow(10, nHalved) + bd;
    }
}