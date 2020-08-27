#include <iostream>
#include <string>

using namespace std;

template <class P>                  //Stack class is straightforward. It is designed like we did in class.
class Stack
{
private:
P sList[80];
int top;

public:
Stack(void);
void push(P);
P pop(void);
void clearStack(void);
P peek(void);
int stackLength(void);
int stackEmpty(void);
};

template <class P>
Stack<P>::Stack(void)
{
    top=-1;
}

template <class P>
void Stack<P>::push(P el)
{
    top++;
    sList[top]=el;
}

template <class P>
P Stack<P>::pop(void)
{
    if(top==-1)
    {
        cout <<"Stack is empty 12";

    }
    else
    {
        P temp;
        temp=sList[top];
        top--;
        return temp;
    }
}

template <class P>
void Stack<P>::clearStack(void)
{
    top=-1;
}

template <class P>
P Stack<P>::peek(void)
{
    if(top==-1)
        cout << "Stack is empty";
    else
    return sList[top];
}

template <class P>
int Stack<P>::stackLength(void)
{
    int temp;
    temp=top+1;
return temp;
}


template <class P>
int Stack<P>::stackEmpty(void)
{
    if(top==-1)
        return 1;
    else return 0;
}
