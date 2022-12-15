#include <bits/stdc++.h>
using namespace std;

class Student
{
protected:
    int roll_no;

public:
    void set_roll_no(int a)
    {
        roll_no = a;
    }
    void get_roll_no()
    {
        cout << "your roll number is: " << roll_no << endl;
    }
};

class Test : virtual public Student
{
protected:
    float maths, physics;

public:
    void set_marks(int m1, int m2)
    {
        maths = m1;
        physics = m2;
    }

    void get_marks()
    {
        cout << "Your maths marks are: " << maths << " and physics marks are: " << physics << ". The total is: " << maths + physics << endl;
    }
};

int main()
{

    return 0;
}