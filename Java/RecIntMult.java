package Java;
public class RecIntMult{
    public static void main(String[] args) {
        int x = 1234;
        int y = 5678;
        int n = 4;
        System.out.println(recIntMult(x, y, n));
    }
    // look at python implentation for explanation
    public static int recIntMult(int x, int y, int n){
        if(n == 1){
            return x * y;
        }
        int nHalved = n / 2;
        int a = x / (int)Math.pow(10, nHalved), b = x % (int)Math.pow(10, nHalved);
        int c = y / (int)Math.pow(10, nHalved), d = y % (int)Math.pow(10, nHalved);
        int ac = recIntMult(a, c, nHalved), ad = recIntMult(a, d, nHalved);
        int bc = recIntMult(b, c, nHalved), bd = recIntMult(b, d, nHalved);
        return (int)Math.pow(10, n) * ac + (int)Math.pow(10, nHalved) * (ad + bc) + bd;
    }
}