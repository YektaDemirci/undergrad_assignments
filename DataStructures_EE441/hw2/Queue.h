#include <iostream>
#include <string>

using namespace std;

template <class T>                  //Queue class is straightforward. It is designed like we did in class.
class Queue
{

private:
int fro, rea, coun;
char op;
T qList[80] ;

public:
Queue(void);
void QOpera(char);
void QInsert(T);
T QDelete(void);
void ClearQueue(void);
T QFront(void);
int QLength(void);
int QEmpty(void);
};

template <class T>
Queue<T>::Queue(void)
{

    op='\0';
    fro=0;
    rea=0;
    coun=0;
}

template <class T>
void Queue<T>::QOpera(char o)
{
    op=o;
}

template <class T>
void Queue<T>::QInsert(T el)
{
    qList[rea]=el;
    coun++;
    rea++;
}

template <class T>
T Queue<T>::QDelete(void)
{
    if(coun==0)
    {
        cout << "Queue is empty1";
    }
    else
    {
        T temp;
        temp=qList[fro];
        coun--;
        fro++;
        return temp;
    }
}

template <class T>
void Queue<T>::ClearQueue(void)
{
    fro=0;
    rea=0;
    coun=0;
}

template <class T>
T Queue<T>::QFront(void)
{
    if(coun==0)
    {
        cout << "Queue is empty2";
    }
    else
        return qList[fro];
}

template <class T>
int Queue<T>::QLength(void)
{
    if(coun==0)
    {
        cout << "Queue is empty3";
    }
    else
        return coun;
}

template <class T>
int Queue<T>::QEmpty(void)
{
    if(coun==0)
        return 1;
    else
        return 0;
}
