#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;

int factorial(int i)
{
    if(i == 0) return 1;
    else return i *factorial(i - 1);
}

int main(){
    double x_strart, x_end, dx, e;
    cin >> x_start, x_end, dx, e;
    double f = x_start;

    int k = 1;

    while ( e < 1 ){
    e*=10;
    k++;
    }

    int i = 0;
    k *=10;
    while (f <= x_end) {
    cout << f << ' ' << round(pow(f,i) / factorial(i) * k)/k << endl;
    i++;
    f += dx;
    }
    return 0;

}