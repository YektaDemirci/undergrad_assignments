#include <iostream>
#include <string>
#include "Course.h"

using namespace std;

Course math;

void showByID()
{
                int id0;

                cout << "Enter ID \n";
                cin  >> id0;

                if(id0>=0)
                {
                    int cc=1;
                    for(int i=0;i<math.getNum();i++)    //We basically check all the students in the array. If the id is found it prints it out.
                    {
                        Student temp=math.getStudent(i);
                        if(id0==temp.GetId())
                        {

                            cout << temp.GetId() << " " << temp.GetName() << " " << temp.GetSur() << " " << temp.GetMt1() << " " << temp.GetMt2() << " " << temp.GetFin() << " " << temp.overallScore(math.Getx1(), math.Getx2(), math.GetF()) << "\n";
                            cc=0;
                            break;
                        }
                    }
                    if(cc==1)                       //If the given id is not found in the list.
                        cout << "Invalid ID \n";
                }

                else cout << "Invalid ID \n";      //It is the case when the input is negative integer.
}

void updateStudentScore()
{
            int idd, news;
            string examtype;
            Student temp;
            int id1,cont;
            string n1, n2;
            int m11, m22, ff;

            cout << "Enter ID,exam type and updated score \n";
            cin >> idd >> examtype >> news;

        if(-1<news && news<101)                     //Checks whether the new exam score is valid
        {
            int cntrl3=0;                           //cntrl3 checks whether there is a such a student with given ID.
            for(int i=0;i<math.getNum();i++)        //In this part we find the student in the array by checking all the id numbers.
            {
                temp=math.getStudent(i);
                if(idd==temp.GetId())
                {
                    cont=i;                         //cont controls the index number of the student.
                    cntrl3=1;
                    break;                          //When the student is found it gets out of the for loop.
                }
            }
            if(cntrl3==1)
            {
            id1=temp.GetId();                       //After finding the student we get its informations.
            n1=temp.GetName();
            n2=temp.GetName();
            m11=temp.GetMt1();
            m22=temp.GetMt2();
            ff=temp.GetFin();

                if(examtype=="mt1")                     //We update the new informations by checking which midterm should be updated. I send all the old informations with the new one to addStudent function
                {                                       //In order to not create a new student and not increase Num, we use a control input here which is the index number of the student.
                    math.addStudent(id1, n1, n2, news, m22, ff, cont);
                }                                       //Control input should be different from 321 since it shows the case of real addStudent function.
                else if(examtype=="mt2")
                {
                    math.addStudent(id1, n1, n2, m11, news, ff, cont);
                }
                else if(examtype=="final")
                {
                math.addStudent(id1, n1, n2, m11, m22, news, cont);
                }
                else cout << "Invalid exam type \n";
            }
            else cout <<"No student with such ID \n";
        }
        else cout << "Invalid exam score \n";
}

void showAbove()
{
        if(math.getNum())                           //It checks the case if there is not ant student registered yet.
        {
            float overs;
            int th;
            cout << "Enter threshold score \n";
            cin >> th;
            for(int i=0;i<math.getNum();i++)        //It checks the students 1 by 1 and directly then overall of a student is calculated and outputted directly if it is more than threshold voltage
            {
                Student temp;
                temp=math.getStudent(i);
                overs=temp.overallScore(math.Getx1(), math.Getx2(), math.GetF());
                if(overs>th)
                    cout << temp.GetId() << " " << temp.GetName() << " " << temp.GetSur() << " " << temp.GetMt1() << " " << temp.GetMt2() << " " << temp.GetFin() << " " << temp.overallScore(math.Getx1(), math.Getx2(), math.GetF()) << "\n";
            }
        }
        else
            cout <<"There is not any student registered yet \n";
}

void showBelow()
{
        if(math.getNum())
        {
            float overs;
            int th;
            cout << "Enter threshold score \n";
            cin >> th;

            for(int i=0;i<math.getNum();i++)    //It is almost the same except it checks the cases below the threshold
            {
                Student temp;
                temp=math.getStudent(i);
                overs=temp.overallScore(math.Getx1(), math.Getx2(), math.GetF());
                if(overs<th)
                    cout << temp.GetId() << " " << temp.GetName() << " " << temp.GetSur() << " " << temp.GetMt1() << " " << temp.GetMt2() << " " << temp.GetFin() << " " << temp.overallScore(math.Getx1(), math.Getx2(), math.GetF()) << "\n";
            }
        }
        else
            cout <<"There is not any student registered yet \n";
}

void showAverage()
{
                math.calcAverage(); //It is already  defined in the calcAverage function.
}

int main()
{
    int control;

    cout<< "Classroom information interface \n \n";
    cout << "Choose your option: \n 1) Add a student \n 2) Search a student by ID \n 3) Show students with overall score above a threshold \n";
    cout << " 4) Show students with overall score below a threshold \n 5) Show classroom average \n 6) Change a student's score \n 7) Exit \n \n";
    do{
        cout<< "Enter your option: \n";
        cin >> control;
        if(control==1)
        {
                int cntr=1;             //To check whether there is still enough space in the array. The total size 10.
                if(math.getNum()>9)
                {
                    cout << "Not enough space, maximum student number is reached \n";
                    cntr=0;
                }
                if(cntr)
                {
                cout << "Enter ID, name, surname, and exam scores(MT1, MT2, Final)\n";
                int id1;
                string n1, n2;
                int m11, m22, ff;
                cin >>id1 >> n1 >> n2 >> m11 >> m22 >> ff;
                int cntr2=1;                                // cntr2 checks whether the inputs are valid. If they are not it becomes 1 and student is not added
                    if(!(-1<id1))
                    {
                        cout << "Invalid ID \n";
                        cntr2=0;
                    }
                    if(!(-1<m11 && m11<101))
                    {
                        cout << "Invalid midterm1 score \n";
                        cntr2=0;
                    }
                    if(!(-1<m22 && m22<101))
                    {
                        cout << "Invalid midterm2 score \n";
                        cntr2=0;
                    }
                    if(!(-1<ff && ff<101))
                    {
                        cout << "Invalid final score \n";
                        cntr2=0;
                    }
                if(cntr2==1)
                math.addStudent(id1, n1, n2, m11, m22, ff, 321); //321 is explained in the addStudent function part. It checks whether there is a new student or an updated one.
                }

        }


        else if(control==2)
        {
            showByID();
        }

        else if(control==3)
        {
            showAbove();
        }

        else if(control==4)
        {
            showBelow();
        }

        else if(control==5)
        {
            showAverage();
        }

        else if(control==6)
        {
            updateStudentScore();
        }

        else
            cout << "Invalid option \n";
    }
    while(!(control==7));           //By using do-while the programme is run at least one time and it exits when 7 is used.
    return 0;
}
