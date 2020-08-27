#include <iostream>
#include <fstream>
#include <stdlib.h>
#include "LinkedList.h"



using namespace std;

int main()
{


ifstream processesFile;
processesFile.open ("processes.txt");

//Check error
if(processesFile.fail())
{
    cerr << "Error Opening File" << endl;
    exit(1);
}

int numProcesses;
processesFile >> numProcesses;
Node *liste;
liste=new Node[numProcesses];

int processID, arrivalTime, runTime, priority;

for(int i=0; i<numProcesses; ++i)
{
processesFile >> processID >> arrivalTime >> runTime >> priority;
liste[i] = Node(processID, arrivalTime, runTime, priority);
}
processesFile.close();

LinkedList deneme;
int id=0,idc=0;
int i=0,cont=0;
long int counter=0;

    while(idc<numProcesses)                             //Basic loop it runs till all ID's are printed
    {
        if(i<numProcesses && liste[i].arrtime==counter) //It checks if the arrival time has came for a node to be inserted to the linked list
        {
        deneme.Insert(liste+i);
        i++;
        }

        else if(cont>0)                                 //It is the case when CPU is busy. cont is the runtime value for each case.
        {
            counter++;
            cont--;
            if(cont==0)                                 //If the work is done then ID is printed
            {
                cout << idc <<" ID "<< id << endl;
                idc++;                                  //************ idc checks searching performance
            }
            else
                continue;
        }

        else                                            //If cont is 0 then it means cpu is not busy. So a new task is given from the head of the linked list
        {
            Node temp(deneme.returnFro()->ID, deneme.returnFro()->arrtime, deneme.returnFro()->runtime, deneme.returnFro()->prior);
            id=temp.ID;
            cont=temp.runtime;
            deneme.FroNext();
            counter++;
            cont--;
            if(cont==0)                                  //It controls if the runtime is 1 for work. This part is used otherwise tasks with 1 runtime are missed.
            {
                cout << idc <<" ID "<< id << endl;
                idc++;
            }
            else
                idc=idc+0;                              //It is a dummy line just ignore it. I don't like leaving unmatched if so I added a dummy else line.
        }

    }
cout << "Number of nodes visited for searching " << idc << endl;
cout << "Number of nodes visited for insertation " << deneme.returnCounter();

}
