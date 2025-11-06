#include <iostream>
using namespace std;

#define SIZE 5   // Maximum size of the queue

class CircularQueue {
private:
    int arr[SIZE];
    int front, rear;

public:
    CircularQueue() {
        front = -1;
        rear = -1;
    }

    // a. Insertion (Enqueue)
    void enqueue(int value) {
        if ((front == 0 && rear == SIZE - 1) || (rear == (front - 1 + SIZE) % SIZE)) {
            cout << "Queue Overflow! Cannot insert " << value << endl;
            return;
        }
        else if (front == -1) {  // Empty queue
            front = rear = 0;
        }
        else if (rear == SIZE - 1 && front != 0) {  // Wrap around
            rear = 0;
        }
        else {
            rear++;
        }

        arr[rear] = value;
        cout << value << " inserted into the queue.\n";
    }

    // b. Deletion (Dequeue)
    void dequeue() {
        if (front == -1) {
            cout << "Queue Underflow! No elements to delete.\n";
            return;
        }

        cout << "Deleted element: " << arr[front] << endl;

        if (front == rear) {  // Only one element
            front = rear = -1;
        }
        else if (front == SIZE - 1) {
            front = 0;
        }
        else {
            front++;
        }
    }

    // c. Display
    void display() {
        if (front == -1) {
            cout << "Queue is Empty!\n";
            return;
        }

        cout << "Circular Queue Elements: ";
        if (rear >= front) {
            for (int i = front; i <= rear; i++)
                cout << arr[i] << " ";
        }
        else {
            for (int i = front; i < SIZE; i++)
                cout << arr[i] << " ";
            for (int i = 0; i <= rear; i++)
                cout << arr[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    CircularQueue q;
    int choice, value;

    do {
        cout << "\n===== CIRCULAR QUEUE MENU =====";
        cout << "\n1. Enqueue (Insert)";
        cout << "\n2. Dequeue (Delete)";
        cout << "\n3. Display";
        cout << "\n0. Exit";
        cout << "\nEnter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter value to insert: ";
            cin >> value;
            q.enqueue(value);
            break;
        case 2:
            q.dequeue();
            break;
        case 3:
            q.display();
            break;
        case 0:
            cout << "Exiting program...\n";
            break;
        default:
            cout << "Invalid choice! Try again.\n";
        }
    } while (choice != 0);

    return 0;
}




// Experiment: Circular Queue using Array
// COs: CO1, CO2
// Aim
// Implement a Circular Queue using a fixed-size array and perform the following operations:
// 1. Insertion (Enqueue)
// 2. Deletion (Dequeue)
// 3. Display
// Objectives
// ● Understand the concept of circular queue and its advantages over linear queue.
// ● Implement enqueue, dequeue, and display operations using arrays.
// ● Handle overflow (queue full) and underflow (queue empty) conditions.
// ● Apply circular indexing to efficiently use array memory.
// Theory
// Queue
// ● A queue is a linear data structure which follows FIFO (First In First Out) principle.
// ● Front points to the first element, Rear points to the last element.
// Linear Queue Limitation
// ● Fixed array size leads to wastage of memory after some deletions because front moves forward and
// empty spaces at the beginning cannot be reused.
// Circular Queue
// ● A Circular Queue overcomes this limitation.
// ● Last position is connected to the first position, forming a circle.
// Front and Rear are updated using modulo operation:
// rear = (rear + 1) % size
// front = (front + 1) % size
// Advantages of Circular Queue
// ● Efficient memory utilization.
// ● No need to shift elements after deletion.
// ● Useful in CPU scheduling, buffering, traffic control systems.


// Operations
// 1. Enqueue (Insertion)
// ○ If queue is full → Overflow.
// ○ Else → Increment rear (mod size) and insert element.
// 2. Dequeue (Deletion)
// ○ If queue is empty → Underflow.
// ○ Else → Remove element at front and increment front (mod size).
// 3. Display
// ○ Traverse from front to rear using circular indexing.
// Algorithm
// Enqueue(x)
// if ( (rear+1) % size == front ) then
//  print "Queue Full"
// else
//  rear = (rear+1) % size
//  queue[rear] = x
//  if (front == -1) front = 0
// Dequeue()
// if (front == -1) then
//  print "Queue Empty"
// else
//  element = queue[front]
//  if (front == rear) // only one element
//  front = rear = -1
//  else
//  front = (front+1) % size
// Display()
// if (front == -1) print "Queue Empty"
// else
//  i = front
//  do
//  print queue[i]
//  i = (i+1) % size
//  while i != (rear+1) % size
// Observation / Result
// ● Circular Queue efficiently reuses array space after deletions.
// ● Overflow occurs when queue is full (rear+1 == front).
// ● Underflow occurs when queue is empty (front == -1).


// Conclusion
// ● Implemented circular queue using array successfully.
// ● Enqueue, Dequeue, and Display operations are working correctly.
// ● Circular indexing avoids wastage of array memory.
// ● Useful for buffering, CPU scheduling, and real-time systems.


// program / code 
// Experiment:Implement Circular Queue using Array. Perform following operations on it.
// a. Insertion (Enqueue)
// b. Deletion (Dequeue)
// c. Display
// #include <iostream>
// using namespace std;
// #define SIZE 5 // Fixed size of circular queue
// class CircularQueue
// {
// private:
//  int queue[SIZE];
//  int front, rear;
// public:
//  CircularQueue()
//  {
//  front = rear = -1;
//  }
//  bool isFull()
//  {
//  return ( (rear + 1) % SIZE == front );
//  }
//  bool isEmpty()
//  {
//  return (front == -1);
//  }
//  void enqueue(int value)
//  {
//  if (isFull())
//  {
//  cout << "Queue Overflow! Cannot insert " << value << endl;
//  return;
//  }
//  rear = (rear + 1) % SIZE;
//  queue[rear] = value;
//  if (front == -1) front = rear;
//  cout << "Inserted: " << value << endl;
//  }
//  void dequeue()
//  {
//  if (isEmpty())
//  {
//  cout << "Queue Underflow! Nothing to delete." << endl;
//  return;
//  }

// NAVSAHYADRI EDUCATION SOCIETY’S, GROUP OF INSTITUTIONS
//  Savitribai Phule Pune University
// Second Year of Artificial Intelligence and Machine Learning (2024 Course)
// Course Code: PCC-204-AIM Course Name: Data Structures & Algorithms Lab
// 5 Asst.Prof.Salunkhe A.A
//  int deleted = queue[front];
//  if (front == rear)
//  { // Only one element
//  front = rear = -1;
//  }
//  else
//  {
//  front = (front + 1) % SIZE;
//  }
//  cout << "Deleted: " << deleted << endl;
//  }
//  void display()
//  {
//  if (isEmpty())
//  {
//  cout << "Queue is empty!" << endl;
//  return;
//  }
//  cout << "Queue elements: ";
//  int i = front;
//  while (true)
//  {
//  cout << queue[i] << " ";
//  if (i == rear) break;
//  i = (i + 1) % SIZE;
//  }
//  cout << endl;
//  }
// };
// int main()
//  {
//  CircularQueue cq;
//  int choice, value;
//  do
//  {
//  cout << "\n--- Circular Queue Menu ---\n";
//  cout << "1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\n";
//  cout << "Enter your choice: ";
//  cin >> choice;
//  switch(choice)
//  {
//  case 1:
//  cout << "Enter value to insert: ";
//  cin >> value;
//  cq.enqueue(value);
//  break;
//  case 2:
//  cq.dequeue();
//  break;

// NAVSAHYADRI EDUCATION SOCIETY’S, GROUP OF INSTITUTIONS
//  Savitribai Phule Pune University
// Second Year of Artificial Intelligence and Machine Learning (2024 Course)
// Course Code: PCC-204-AIM Course Name: Data Structures & Algorithms Lab
// 6 Asst.Prof.Salunkhe A.A
//  case 3:
//  cq.display();
//  break;
//  case 4:
//  cout << "Exiting...\n";
//  break;
//  default:
//  cout << "Invalid choice! Try again.\n";
//  }
//  } while(choice != 4);
//  return 0;
// }
// Output
// --- Circular Queue Menu ---
// 1. Enqueue
// 2. Dequeue
// 3. Display
// 4. Exit
// Enter your choice: 1
// Enter value to insert: 10
// Inserted: 10
// Enter your choice: 1
// Enter value to insert: 20
// Inserted: 20
// Enter your choice: 1
// Enter value to insert: 30
// Inserted: 30
// Enter your choice: 3
// Queue elements: 10 20 30
// Enter your choice: 2
// Deleted: 10
// Enter your choice: 3
// Queue elements: 20 30
// Enter your choice: 1
// Enter value to insert: 40
// Inserted: 40
// Enter your choice: 1
// Enter value to insert: 50
// Inserted: 50
// Enter your choice: 1
// Enter value to insert: 60
// Queue Overflow! Cannot insert 60
// Enter your choice: 3
// Queue elements: 20 30 40 50