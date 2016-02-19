"""__author__ = 'anyu'
Implement pow(x, n).

class Solution {
public:
    double pow(double x, int n) {
        if (x < 0) return (n % 2 == 0) ? pow(-x, n) : -pow(-x, n);
        if (x == 0 || x == 1) return x;
        if (n < 0) return 1.0 / pow(x, -n);
        if (n == 0) return 1.0;

        double half = pow(x, n / 2);
        if (n % 2 == 0) return half * half;
        else return x * half * half;
    }
};

class Solution {
public:
    double pow(double x, int n) {
        int sn = 1;
        if (n < 0) n = -n, sn = -sn;
        double res = pow1(x, n);
        return (sn > 0) ? res : 1.0 / res;
    }

    double pow1(double x, int n) {
        double res = 1.0, t = x;
        for (; n > 0; n /= 2) {
            if (n % 2) res *= t;
            t *= t;
        }
        return res;
    }

    double pow2(double x, int n) {
        if (n == 0) return 1.0;
        double t = pow2(x, n / 2);
        if (n % 2 == 0) return t*t;
        return x*t*t;
    }

    double pow3(double x, int n) {
        if (n == 0) return 1.0;
        if (n % 2) return x*pow(x, n - 1);
        double t = pow(x, n / 2);
        return t*t;
    }
};
"""


def pow(x,n):
    if x is 0: return 0
    elif n is 0: return 1
    else:
        if n%2 is 1:
            return x*pow(x,n/2)
        elif n%2 is 0:
            return pow(x,n/2)



def pow(x,n):
    if x is 0 or x is 1:
        return x
    if x<0:
        if n%2 is 0: return pow(-x,n)
        else: return -pow(-x,n)

    if n<0:
        return  1.0/pow(x,-n)

    if n is 0: return 1.0  # this is important to keep result float num

    t = pow(x,n/2)
    if n%2 is 0: return t*t
    else:
        return x*t*t

