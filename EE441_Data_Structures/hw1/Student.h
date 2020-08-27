#include <iostream>
#include <string>

using namespace std;

class Student
{
private:
   int id,midterm1,midterm2,fina;
   string name, surname;
public:
    Student(int, string, string, int, int, int);            //Everything is straight forward here so I don't write any comments except overallScore
    void SetId(int i);
    int GetId(void) const;
    void SetName(string nm);
    string GetName(void) const;
    void SetSur(string snm);
    string GetSur(void) const;
    void SetMt1(int mt1);
    int GetMt1(void) const;
    void SetMt2(int mt2);
    int GetMt2(void) const;
    void SetFin(int fin);
    int GetFin(void) const;
    float overallScore(float, float, float);
};

Student::Student(int i=0, string nm="", string snm="", int mt1=0, int mt2=0, int fin=0)
{
    id=i;
    name=nm;
    surname=snm;
    midterm1=mt1;
    midterm2=mt2;
    fina=fin;
}

void Student::SetId(int x)
{
    id=x;
}

int Student::GetId() const
{
    return id;
}

void Student::SetName(string n)
{
    name=n;
}

string Student::GetName() const
{
    return name;
}

void Student::SetSur(string s)
{
    surname=s;
}

string Student::GetSur() const
{
    return surname;
}

void Student::SetMt1(int m1)
{
    midterm1=m1;
}

int Student::GetMt1() const
{
    return midterm1;
}

void Student::SetMt2(int m2)
{
    midterm2=m2;
}

int Student::GetMt2() const
{
    return midterm2;
}

void Student::SetFin(int f)
{
    fina=f;
}

int Student::GetFin() const
{
    return fina;
}

float Student::overallScore(float m1, float m2, float f)    //We take midterm weights as inputs here. Even though midterm weights are not supposed to be changed in the examples.
{                                                           //Just by creating a set function to weights, they can be changeable and useful as well with this implementation.
    float over;
    over=(midterm1*m1+midterm2*m2+fina*f);
    return over;
}
