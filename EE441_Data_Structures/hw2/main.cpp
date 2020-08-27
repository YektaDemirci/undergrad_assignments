#include <iostream>
#include <string>
#include<math.h>
#include "Queue.h"
#include "Stack.h"

using namespace std;

Stack<int> dum;                         //Only 1 stack is defined in the whole code as it is said the hw2 template.

int charcontroller(char x)              //It controls whether there is an undeserved input by sending 0
{
    if(x=='1')
        return 1;
    else if(x=='2')
        return 1;
    else if(x=='3')
        return 1;
    else if(x=='4')
        return 1;
    else if(x=='5')
        return 1;
    else if(x=='6')
        return 1;
    else if(x=='7')
        return 1;
    else if(x=='8')
        return 1;
    else if(x=='9')
        return 1;
    else if(x=='0')
        return 1;
    else if(x=='^')
        return 1;
    else if(x=='*')
        return 1;
    else if(x=='/')
        return 1;
    else if(x=='%')
        return 1;
    else if(x=='+')
        return 1;
    else if(x=='-')
        return 1;
    else if(x=='[')
        return 1;
    else if(x=='(')
        return 1;
    else if(x==']')
        return 1;
    else if(x==')')
        return 1;
    else return 0;
}

int operatorcont(char x)                //It is to control if there are operations next to each other.
{
    if(x=='^')
        return 1;
    else if(x=='*')
        return 1;
    else if(x=='/')
        return 1;
    else if(x=='%')
        return 1;
    else if(x=='+')
        return 1;
    else if(x=='-')
        return 1;
    else
        return 0;
}

int validity(string sLi)                //This is overall validity function that uses the above 3 ones.
{
    string test;
    int a=sLi.length();
    int k1=0;
    int k2=0;
    int i1=0;
    int i2=0;

    for(int i=0;i<a;i++)
    {
        test[i]=operatorcont(sLi[i]);
    }
    for(int i=0;i<a-1;i++)
    {
        if(test[i]==1 && test[i+1]==1)
            return 0;
    }
    if(test[0]==1 || test[a-1]==1)
        return 0;

    for(int i=0;i<a;i++)
    {
        if(!charcontroller(sLi[i]))
           return 0;

        if(sLi[i]=='[')
        {
            if(i1==i2)
            {
            k1++;
            }
        }
        else if(sLi[i]=='(')
            i1++;
        else if(sLi[i]==')')
        {
                i2++;
                if(i2>i1)
                    return 0;
        }
        else if(sLi[i]==']')
        {
            if(i1==i2)
                {k2++;
                if(k2>k1)
                    return 0;
                }
        }

    }
    if((k1==k2) && (i1==i2))
        return 1;
    else
        return 0;
}

int ctn(char x)                         //This is to change char input to integers
{
    if(x=='1')
        return 1;
    else if(x=='2')
        return 2;
    else if(x=='3')
        return 3;
    else if(x=='4')
        return 4;
    else if(x=='5')
        return 5;
    else if(x=='6')
        return 6;
    else if(x=='7')
        return 7;
    else if(x=='8')
        return 8;
    else if(x=='9')
        return 9;
    else if(x=='0')
        return 0;
    else if(x=='^')
        return -1;
    else if(x=='*')
        return -2;
    else if(x=='/')
        return -3;
    else if(x=='%')
        return -4;
    else if(x=='+')
        return -5;
    else if(x=='-')
        return -6;
    else if(x=='[')
        return -7;
    else if(x=='(')
        return -7;
    else if(x==']')
        return -8;
    else if(x==')')
        return -8;
    else return -10;
}

int getnum(Queue<int> num,int dec)     //This function gets +2 digit number since like making 1 2 3 into 123.
{
    int tempin=0;
    int tempfin=0;
    for(;dec>=0;dec--)
    {
        tempin=pow(10,dec)*num.QDelete();
        tempfin=tempin+tempfin;
    }
    return tempfin;
}

Queue<int> mat(Queue<int> input)        //This is the function that makes +2 digit numbers numbers from 1 digit numbers.
{
    int uzunluk;
    int temp,temp2;
    int decimal=-1;
    Queue<int> sayi;
    Queue<int> asil;
    uzunluk=input.QLength();
    while(!input.QEmpty())
    {
        temp=input.QDelete();
        if(temp==-7 || temp==-8)
        {
            if(decimal>-1)
            {
            temp2=getnum(sayi,decimal);
            asil.QInsert(temp2);
            sayi.ClearQueue();
            decimal=-1;
            }
            asil.QInsert(temp);
        }
        else if(temp>-1)
        {
            sayi.QInsert(temp);
            decimal++;
        }
        else
        {
            if(decimal>-1)
            {
            temp2=getnum(sayi,decimal);
            asil.QInsert(temp2);
            sayi.ClearQueue();
            decimal=-1;
            }
            asil.QInsert(temp);
        }

    }
if(decimal>-1)
{
temp2=getnum(sayi,decimal);
asil.QInsert(temp2);
sayi.ClearQueue();
decimal=-1;
}
return asil;
}

Queue<int> hust(Queue<int> dizi)        //This is the function that operates as power function. Dynamic memory used here and deleted at the end of all cases.
{
    int dummy1,dummy2,dummy3;
    int n,tempe;
    Queue<int> te;
    Queue<int> dumm;
    Queue<int> gercekson;
    n=dizi.QLength();
    int *p;
    p=new int[n];
    for(int i=0;i<n;i++)
        *(p+i)=dizi.QDelete();

    for(int i=0;i<n;i++)
    {
    dum.push(*(p+i));
        if(*(p+i)==-1)
        {
        dummy1=dum.pop();
        dummy2=dum.pop();
        dummy3=*(p+i+1);
        tempe=pow(dummy2,dummy3);
        dum.push(tempe);
        if((i+2)<n)
        {
            for(int t=i+2;t<n;t++)
            {
                dum.push(*(p+t));
            }
        }
        while(!dum.stackEmpty())
        dumm.QInsert(dum.pop());
        while(!dumm.QEmpty())
        dum.push(dumm.QDelete());
        while(!dum.stackEmpty())
        te.QInsert(dum.pop());

        gercekson=hust(te);
        delete p;
        return gercekson;
        }
    }
while(!dum.stackEmpty())
dumm.QInsert(dum.pop());
while(!dumm.QEmpty())
dum.push(dumm.QDelete());
while(!dum.stackEmpty())
te.QInsert(dum.pop());
delete p;
return te;
}

Queue<int> hcarp(Queue<int> dizi)       //h functions checks the input 1 by  1 and make proper calculations.
{
    int dummy1,dummy2,dummy3;
    int n,tempe;
    Queue<int> te;
    Queue<int> dumm;
    Queue<int> gercekson;
    n=dizi.QLength();
    int *p;
    p=new int[n];
    for(int i=0;i<n;i++)
        *(p+i)=dizi.QDelete();
    for(int i=0;i<n;i++)
    {
    dum.push(*(p+i));
        if(*(p+i)==-2)
        {
        dummy1=dum.pop();
        dummy2=dum.pop();
        dummy3=*(p+i+1);
        tempe=dummy2*dummy3;
        dum.push(tempe);
        if((i+2)<n)
        {
            for(int t=i+2;t<n;t++)
            {
                dum.push(*(p+t));
            }
        }
        while(!dum.stackEmpty())
        dumm.QInsert(dum.pop());
        while(!dumm.QEmpty())
        dum.push(dumm.QDelete());
        while(!dum.stackEmpty())
        te.QInsert(dum.pop());

        gercekson=hcarp(te);
        delete p;
        return gercekson;
        }
    }
while(!dum.stackEmpty())
dumm.QInsert(dum.pop());
while(!dumm.QEmpty())
dum.push(dumm.QDelete());
while(!dum.stackEmpty())
te.QInsert(dum.pop());
delete p;
return te;
}

Queue<int> hbol(Queue<int> dizi)        //hcarp, hbol, hmod etc are similar to hust function. Only difference is the operation.
{
    int dummy1,dummy2,dummy3;
    int n,tempe;
    Queue<int> te;
    Queue<int> dumm;
    Queue<int> gercekson;
    n=dizi.QLength();
    int *p;
    p=new int[n];
    for(int i=0;i<n;i++)
        *(p+i)=dizi.QDelete();

    for(int i=0;i<n;i++)
    {
    dum.push(*(p+i));
        if(*(p+i)==-3)
        {
        dummy1=dum.pop();
        dummy2=dum.pop();
        dummy3=*(p+i+1);
        tempe=dummy2/dummy3;
        dum.push(tempe);
        if((i+2)<n)
        {
            for(int t=i+2;t<n;t++)
            {
                dum.push(*(p+t));
            }
        }
        while(!dum.stackEmpty())
        dumm.QInsert(dum.pop());
        while(!dumm.QEmpty())
        dum.push(dumm.QDelete());
        while(!dum.stackEmpty())
        te.QInsert(dum.pop());

        gercekson=hbol(te);
        delete p;
        return gercekson;
        }
    }
while(!dum.stackEmpty())
dumm.QInsert(dum.pop());
while(!dumm.QEmpty())
dum.push(dumm.QDelete());
while(!dum.stackEmpty())
te.QInsert(dum.pop());
delete p;
return te;
}

Queue<int> hmod(Queue<int> dizi)
{
    int dummy1,dummy2,dummy3;
    int n,tempe;
    Queue<int> te;
    Queue<int> dumm;
    Queue<int> gercekson;
    n=dizi.QLength();
    int *p;
    p=new int[n];
    for(int i=0;i<n;i++)
        *(p+i)=dizi.QDelete();

    for(int i=0;i<n;i++)
    {
    dum.push(*(p+i));
        if(*(p+i)==-4)
        {
        dummy1=dum.pop();
        dummy2=dum.pop();
        dummy3=*(p+i+1);
        tempe=dummy2%dummy3;
        dum.push(tempe);
        if((i+2)<n)
        {
            for(int t=i+2;t<n;t++)
            {
                dum.push(*(p+t));
            }
        }
        while(!dum.stackEmpty())
        dumm.QInsert(dum.pop());
        while(!dumm.QEmpty())
        dum.push(dumm.QDelete());
        while(!dum.stackEmpty())
        te.QInsert(dum.pop());

        gercekson=hmod(te);
        delete p;
        return gercekson;
        }
    }
while(!dum.stackEmpty())
dumm.QInsert(dum.pop());
while(!dumm.QEmpty())
dum.push(dumm.QDelete());
while(!dum.stackEmpty())
te.QInsert(dum.pop());
delete p;
return te;
}

Queue<int> htop(Queue<int> dizi)
{
    int dummy1,dummy2,dummy3;
    int n,tempe;
    Queue<int> te;
    Queue<int> dumm;
    Queue<int> gercekson;
    n=dizi.QLength();
    int *p;
    p=new int[n];
    for(int i=0;i<n;i++)
        *(p+i)=dizi.QDelete();

    for(int i=0;i<n;i++)
    {
    dum.push(*(p+i));
        if(*(p+i)==-5)
        {
        dummy1=dum.pop();
        dummy2=dum.pop();
        dummy3=*(p+i+1);
        tempe=dummy2+dummy3;
        dum.push(tempe);
        if((i+2)<n)
        {
            for(int t=i+2;t<n;t++)
            {
                dum.push(*(p+t));
            }
        }
        while(!dum.stackEmpty())
        dumm.QInsert(dum.pop());
        while(!dumm.QEmpty())
        dum.push(dumm.QDelete());
        while(!dum.stackEmpty())
        te.QInsert(dum.pop());

        gercekson=htop(te);
        delete p;
        return gercekson;
        }
    }
while(!dum.stackEmpty())
dumm.QInsert(dum.pop());
while(!dumm.QEmpty())
dum.push(dumm.QDelete());
while(!dum.stackEmpty())
te.QInsert(dum.pop());
delete p;
return te;
}

Queue<int> hcik(Queue<int> dizi)
{
    int dummy1,dummy2,dummy3;
    int n,tempe;
    Queue<int> te;
    Queue<int> dumm;
    Queue<int> gercekson;
    n=dizi.QLength();
    int *p;
    p=new int[n];
    for(int i=0;i<n;i++)
        *(p+i)=dizi.QDelete();

    for(int i=0;i<n;i++)
    {
    dum.push(*(p+i));
        if(*(p+i)==-6)
        {
        dummy1=dum.pop();
        dummy2=dum.pop();
        dummy3=*(p+i+1);
        tempe=dummy2-dummy3;
        dum.push(tempe);
        if((i+2)<n)
        {
            for(int t=i+2;t<n;t++)
            {
                dum.push(*(p+t));
            }
        }
        while(!dum.stackEmpty())
        dumm.QInsert(dum.pop());
        while(!dumm.QEmpty())
        dum.push(dumm.QDelete());
        while(!dum.stackEmpty())
        te.QInsert(dum.pop());

        gercekson=hcik(te);
        delete p;
        return gercekson;
        }
    }
while(!dum.stackEmpty())
dumm.QInsert(dum.pop());
while(!dumm.QEmpty())
dum.push(dumm.QDelete());
while(!dum.stackEmpty())
te.QInsert(dum.pop());
delete p;
return te;
}

int calculator(Queue<int> girdi)       //This is the function that makes the calculation by using above hust hcar..... functions by the order of power,multiplication,division, mod etc.
{
int sonuc;
int te;
int leng;
leng=girdi.QLength();
    if(leng>1)
    {
        Queue<int> temp;
        temp=hust(girdi);
        temp=hcarp(temp);
        temp=hbol(temp);
        temp=hmod(temp);
        temp=hcik(temp);
        temp=htop(temp);
        sonuc=temp.QDelete();
        return sonuc;
    }
te=girdi.QDelete();
return te;
}

Queue<int> paren(Queue<int> slist)      //This is the main function that uses iterative ways. It calculates the input from the most inner parentheses
{
    string hesapla,temporar;
    string finnal;
    Queue<int> hesap1,hesap2;
    Queue<int> gecici,te;
    Queue<int> damatasi,fina;
    Queue<int> dum1;
    int sonuc;
    int uzunluk,zonuc;
    int tem1,tem2;
    int c=0,r=0,i=0;
    int dummy;
    int el1,el2,l,k,op;
    int leng=slist.QLength();
if(leng!=1)
{
    while(!slist.QEmpty())
    {
        tem1=slist.QDelete();
            if(tem1==-8)
            {
                while(!dum.stackEmpty())
                {
                    tem2=dum.pop();
                    if(tem2==-7)
                    {
                            uzunluk=gecici.QLength();
                            while(!gecici.QEmpty())
                            {
                            dum.push(gecici.QDelete());
                            }
                            for(int b=0;b<uzunluk;b++)
                            {
                            gecici.QInsert(dum.pop());
                            }
                        while(!dum.stackEmpty())
                            dum1.QInsert(dum.pop());
                        while(!dum1.QEmpty())
                            dum.push(dum1.QDelete());
                        while(!dum.stackEmpty())
                            dum1.QInsert(dum.pop());
                        zonuc=calculator(gecici);
                        gecici.ClearQueue();

                        while(!dum1.QEmpty())
                            damatasi.QInsert(dum1.QDelete());

                            damatasi.QInsert(zonuc);

                        while(!slist.QEmpty())
                            damatasi.QInsert(slist.QDelete());


                        fina=paren(damatasi);

                        return fina;
                    }
                gecici.QInsert(tem2);
                }
            }
        dum.push(tem1);
    }
}
return slist;
}




int main()  //This is the main function that has interface functions where user can see what they do.
{
    Queue<int> seri1,seri2,ana,sonuc;
    int control,sonuc1,cont4;
    char cont1,cont2,cont3;
    string input;
    cont1='c';
    cont2='c';
    cont3='c';
    cont4=0;
    cout << "Queue and Stack based calculator" << endl;
    cout << "1-) Enter an expression" << "\n" << "2-) Check the expression" << "\n" << "3-) Calculate" << "\n" << "4-) Reset" << "\n" << "5-) Exit" << endl;

    do{

            cout << "Enter your option" << endl;
            cin >> control;

        if(control==1)
        {
            if(cont2=='p')
            cout <<"Please reset the previous expression first" << endl;
            else
            {
            cout << "Enter an expression" << endl;
            cin >> input;
            cont2='p';
            }
        }

        if(control==2)
        {
            if(cont2=='c')
                cout << "Please enter an expression first" << endl;
            else
            {
                int con;
                con=validity(input);
                if(con==1)
                {
                    cout << "Valid expression!" << endl;
                    cont4=1;
                }
                else
                    cout << "Expression is not valid!" << endl;
            }
        }
        if(control==3)
        {
            if(cont2=='c')
                cout << "Please enter an expression first" << endl;
            else
            {
               if(cont4==1)
               {
                if(cont3=='c')
                {
                int uzun=input.length();
                for(int i=0;i<uzun;i++)
                    seri1.QInsert(ctn(input[i]));
                seri2=mat(seri1);
                while(!seri1.QEmpty())
                    seri1.QDelete();
                ana.QInsert(-7);
                while(!seri2.QEmpty())
                    ana.QInsert(seri2.QDelete());
                ana.QInsert(-8);
                sonuc=paren(ana);
                while(!ana.QEmpty())
                    ana.QDelete();
                sonuc1=sonuc.QDelete();
                cout << sonuc1 << endl;
                cont3='p';
                }
                else
                    cout << sonuc1 << endl;
               }
               else
                cout << "Validate the expression first" << endl;
            }

        }
        if(control==4)
        {
            if(cont2=='c')
                cout << "Please enter an expression first" << endl;
            else
            {
            input.clear();
            cont2='c';
            cont3='c';
            cont4=0;
            cout << "Reset is successful!" << endl;
            }
        }

    }
    while(control!=5);
    return 0;
}
