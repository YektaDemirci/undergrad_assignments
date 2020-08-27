#include <iostream>
#include <string>
#include "Node.h"

using namespace std;

class LinkedList
{
private:
    Node *fro,*currPtr,*prevPtr;
    long int counter;                                //*******counter checks insertion performance

public:
    LinkedList(Node*, Node*, Node*,long int);       //Member functions are created as they are needed. They are not exactly the same as the ones in the lectures.
    void Insert(Node *item);                        //I only defined some that I needed.
    Node *returnFro(void);
    Node *returnCurr(void);
    void CurNext(void);
    void ResetCurr(void);
    void FroNext(void);
    void ResetFront(void);
    long int returnCounter(void);
};

LinkedList::LinkedList(Node* fr=NULL, Node* cur=NULL, Node* prev=NULL,long int cou=0)
{
    fro=fr;
    currPtr=fro;
    counter=cou;
    prev=NULL;
}

void LinkedList::Insert(Node *item)     //Basically it checks all possible cases for a priority order. Test checks if the linked list has more than 2 elements.
{                                       //This is the part where linked list is created actually.
    currPtr=fro;
    prevPtr=currPtr;
    int test=0;

    if(fro==NULL)
        fro=item;
    else
    {
        while(item->prior>=currPtr->prior && currPtr->next !=NULL)
        {
            counter++;
            prevPtr=currPtr;
            currPtr=currPtr->next;
            test++;
        }
        if(test!=0)
        {
            if(currPtr->prior<item->prior)
            {
                currPtr->next=item;
            }
            else
            {
                item->next=currPtr;
                prevPtr->next=item;
                prevPtr=prevPtr->next;
            }
        }
        else
        {
            if(item->prior<currPtr->prior)
            {
                item->next=currPtr;
                fro=item;
            }
            else
            {
                item->next=currPtr->next;
                currPtr->next=item;
            }
        }
    }
}
Node *LinkedList::returnFro(void)   //Some member functions for some small steps. They are quite clear so no need to explain.
{
    return fro;
}

Node *LinkedList::returnCurr(void)
{
    return currPtr;
}

void LinkedList::CurNext(void)
{
    if(currPtr->next==NULL)
        currPtr=NULL;
    else
        currPtr=currPtr->next;
}


void LinkedList::ResetCurr(void)
{
    currPtr=fro;
}

void LinkedList::FroNext(void)
{
    if(fro->next==0 || fro->next==NULL)
        fro=NULL;
    else
    fro=fro->next;
}

void LinkedList::ResetFront(void)
{
    fro=NULL;
}

long int LinkedList::returnCounter(void)
{
    return counter;
}

