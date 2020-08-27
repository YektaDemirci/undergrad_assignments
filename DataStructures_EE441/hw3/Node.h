#include <iostream>
#include <string>

using namespace std;

class Node
{
public :
Node *next;
int ID,arrtime,runtime,prior;       //Very basic node class. I didn't define ID, arrtime, runtime,priority as private members. I could have and created some more member functions to get them
Node(int, int, int, int, Node*);    //But for the sake of simplicity I haven't. I used private ones in the linkedlist class to show I know how to use them. Also in the hw it is not defined to
Node *NextNode(void);               //create which element private or public so I made them all public here.
void Show(void);

};

Node::Node(int IT=0, int arr=0, int run=0, int pri=0, Node* ptrNext=NULL)
{
    ID=IT;
    arrtime=arr;
    runtime=run;
    prior=pri;
    next=NULL;
}

Node *Node::NextNode(void)
{
    return next;
}

void Node::Show(void)
{
    cout << ID << " " << arrtime << " " << runtime << " " << prior <<  endl;
}
