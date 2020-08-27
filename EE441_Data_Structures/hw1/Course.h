#include <iostream>
#include <string>
#include "Student.h"

using namespace std;

class Course
{
private:
    Student entries[10];
    int Num;
    float ex1, ex2, exf;
public:
    Course (Student[10], int, float, float, float);
    int getNum(void) const;
    void addStudent(int, string, string, int, int, int, int);
    Student getStudent(int);
    void calcAverage();
    void changeWeights(float, float, float);
    float Getx1();
    float Getx2();
    float GetF();
};

Course::Course(Student stud[10]=NULL, int ogsay=0, float weig1=0.25, float weig2=0.25, float weigf=0.5)
{

    Num=ogsay;
    ex1=weig1;
    ex2=weig2;
    exf=weigf;
}

int Course::getNum() const
{
    return Num;
}

Student Course::getStudent(int k)
{

    return entries[k];
}

void Course::addStudent(int id, string name, string sname, int m1, int m2, int fi,int cntrl)
{
    Student temp;       //In this function, basically we set information of the students by using Student class functions. The tricky point here is, there is a control input named as cntrl.
    temp.SetId(id);     //Cntrl input controls whether we set a new student or update the midterm result. I choose 321 for creating a new student option. We could have used any number excepts [0-10]
    temp.SetName(name); //Because these integers can be index number. We can not change midterm result of a student directly from the main function since midterm results are private members of Student.
    temp.SetSur(sname); //So I used this control input trick.
    temp.SetMt1(m1);
    temp.SetMt2(m2);
    temp.SetFin(fi);
    if(cntrl==321)
    {
        entries[Num++]=temp;
    }
    else
    {
        entries[cntrl]=temp;
    }
}


void Course::calcAverage()
{

                float mt1o=0, mt2o=0, fino=0, oo=0;
                for(int i=0;i<Num;i++)
                {
                mt1o+=entries[i].GetMt1();
                mt2o+=entries[i].GetMt2();
                fino+=entries[i].GetFin();
                }
                mt1o=mt1o/Num;
                mt2o=mt2o/Num;
                fino=fino/Num;
                oo=(mt1o*ex1+mt2o*ex2+fino*exf);
                cout << "MT1 average: " << mt1o <<"\n" << "MT2 average: " << mt2o << "\n" << "Final average: " << fino << "\n" << "Overall average: " << oo << "\n";

}

void Course::changeWeights(float newex1, float newex2, float newexf)
{
    ex1=newex1;
    ex2=newex2;
    exf=newexf;
}

float Course::Getx1()
{
    return ex1;
}

float Course::Getx2()
{
    return ex2;
}

float Course::GetF()
{
    return exf;
}

