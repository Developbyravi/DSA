#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// Node structure for Stack
struct Node {
    char data;
    Node* next;
};

// Stack class using Linked List
class Stack {
private:
    Node* top;
public:
    Stack() { top = NULL; }

    void push(char x) {
        Node* temp = new Node;
        if (!temp) {
            cout << "Stack Overflow\n";
            return;
        }
        temp->data = x;
        temp->next = top;
        top = temp;
    }

    char pop() {
        if (isEmpty()) {
            cout << "Stack Underflow\n";
            return '\0';
        }
        Node* temp = top;
        char popped = temp->data;
        top = top->next;
        delete temp;
        return popped;
    }

    char peek() {
        if (!isEmpty())
            return top->data;
        else
            return '\0';
    }

    bool isEmpty() {
        return top == NULL;
    }
};

// Function to check if character is operator
bool isOperator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/' || c == '^');
}

// Function to return precedence of operators
int precedence(char c) {
    if (c == '^')
        return 3;
    else if (c == '*' || c == '/')
        return 2;
    else if (c == '+' || c == '-')
        return 1;
    else
        return -1;
}

// Function to convert Infix → Postfix
string infixToPostfix(string infix) {
    Stack s;
    string postfix = "";

    for (char c : infix) {
        if (isalnum(c)) {
            postfix += c; // Operand → directly add to result
        }
        else if (c == '(') {
            s.push(c);
        }
        else if (c == ')') {
            while (!s.isEmpty() && s.peek() != '(') {
                postfix += s.pop();
            }
            s.pop(); // Remove '('
        }
        else if (isOperator(c)) {
            while (!s.isEmpty() && precedence(s.peek()) >= precedence(c)) {
                postfix += s.pop();
            }
            s.push(c);
        }
    }

    // Pop remaining operators
    while (!s.isEmpty()) {
        postfix += s.pop();
    }

    return postfix;
}

// Function to reverse a string and swap ( ) for prefix conversion
string reverseInfix(string exp) {
    reverse(exp.begin(), exp.end());
    for (int i = 0; i < exp.size(); i++) {
        if (exp[i] == '(')
            exp[i] = ')';
        else if (exp[i] == ')')
            exp[i] = '(';
    }
    return exp;
}

// Function to convert Infix → Prefix
string infixToPrefix(string infix) {
    string reversedInfix = reverseInfix(infix);
    string postfix = infixToPostfix(reversedInfix);
    reverse(postfix.begin(), postfix.end());
    return postfix;
}

// Main Function
int main() {
    string infix;
    cout << "Enter Infix Expression: ";
    cin >> infix;

    string postfix = infixToPostfix(infix);
    string prefix = infixToPrefix(infix);

    cout << "\nInfix Expression: " << infix;
    cout << "\nPostfix Expression: " << postfix;
    cout << "\nPrefix Expression: " << prefix << endl;

    return 0;
}



// Experiment No 2: Stack as ADT (Singly Linked List) and Expression Conversion (Infix → Postfix, Infix
// → Prefix)
// COs: CO1, CO2
// Aim
// Implement Stack as an Abstract Data Type (ADT) using a singly linked list and use this ADT to convert
// infix expressions to postfix and prefix forms.

// Objectives
// 1. Implement stack operations (push, pop, peek, isEmpty) using a singly linked list.
// 2. Use the stack ADT to convert infix expressions to postfix and prefix.
// 3. Understand operator precedence and associativity and how stack helps in expression conversion.
// 4. Validate correctness with sample expressions.

// Problem Statement
// Implement stack as an abstract data type using singly linked list and use this ADT for conversion of infix
// expression to postfix, prefix

// Theory
// Stack (Abstract Data Type)
// ● A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
// ● The element inserted last is the first to be removed.
// ● Example: a stack of plates – the plate placed last is removed first.
// ● Stack ADT operations:
// 1. push(x): Insert element x at the top.
// 2. pop(): Remove and return the top element.
// 3. peek()/top(): Return the top element without removing it.
// 4. isEmpty(): Check if stack is empty.
// Linked List Implementation of Stack
// ● A singly linked list is used to dynamically allocate stack memory.
// ● Each node contains:
// ○ data (element stored),
// ○ next (pointer to the next node).
// ● The head pointer acts as the stack’s top.
// ● Advantages over array implementation:
// No fixed size (dynamic).
// ○ Efficient use of memory.
// No stack overflow unless memory is full.

// Expression Conversion and Notations
// Mathematical expressions can be written in three different notations:
// 1. Infix: Operator is between operands.
// Example: a + b
// Human readable, but requires parentheses and precedence rules.
// 2. Postfix (Reverse Polish Notation): Operator comes after operands.
// Example: a b +
// ○ No parentheses needed.
// ○ Easy for computers to evaluate using a stack.
// 3. Prefix (Polish Notation): Operator comes before operands.
// Example: + a b
// ○ No parentheses required.
// Why Use Stack for Conversion?
// ● Infix is easy for humans but difficult for machines to evaluate directly.
// ● Postfix and Prefix eliminate ambiguity since they do not need parentheses.
// ● Stack is ideal for conversion because of its LIFO nature:
// ○ Operators are pushed until operands or precedence conditions are met.
// ○ Parentheses are handled naturally by push/pop operations.
//  Operator Precedence and Associativity
// ● Precedence determines which operator is evaluated first.
// ● Associativity decides order when operators have equal precedence.
// Operator Precedence Associativity
// ^ Highest Right-to-left
// * / Medium Left-to-right
// + - Lowest Left-to-right
// Infix → Postfix Conversion
// ● Scan infix expression from left to right.
// ● Operands are output immediately.
// ● Operators are pushed on the stack according to precedence rules.


// ● When ) is encountered, pop until matching ( is found.
// ● At the end, pop remaining operators.
// Infix → Prefix Conversion
// ● Reverse the infix string and swap ( with ).
// ● Apply the Infix → Postfix algorithm.
// ● Reverse the result → gives prefix.
// Advantages of Stack-based Conversion
// ● Eliminates ambiguity of infix expressions.
// ● Allows direct evaluation of postfix/prefix using stack.
// ● Efficient and systematic approach.
// Algorithm (High-level)
// InfixToPostfix(infix):
// 1. Initialize empty stack S and empty result.
// 2. For each character ch in infix:
// ○ If ch is operand → append to result.
// ○ Else if ch is '(' → push on S.
// ○ Else if ch is ')' → pop from S to result until '(' encountered; pop '('.
// ○ Else (operator):
// ■ While S not empty and top of S is operator and (precedence(top) > precedence(ch) or
// (precedence(top) == precedence(ch) and ch is left-associative)) → pop top to result.
// ■ Push ch on S.
// 3. After scanning, pop remaining operators from S to result.
// 4. Return result.
// InfixToPrefix(infix):
// 1. Reverse infix string.
// 2. Swap '(' with ')' in reversed string.
// 3. temp = InfixToPostfix(modified-reversed-infix).
// 4. Reverse temp → prefix.
// Observation / Result
// ● Stack ADT using linked list works correctly for conversion tasks.
// ● Postfix and prefix forms generated using stack operations — demonstrating the utility of stack
// (LIFO) for expression parsing and operator management.
// Conclusion
// ● Implemented Stack ADT using singly linked list and applied it for infix-to-postfix and infix-to-prefix
// conversions.


// ● Students will understand how stack supports expression evaluation and parsing, and the importance
// of operator precedence and associativity.
// Viva Questions
// 1. What is Stack ADT? List basic operations.
// 2. Explain how stack helps in converting infix to postfix.
// 3. Why is ^ (exponent) treated as right-associative? How does that affect conversion?
// 4. How does the algorithm handle parentheses?
// 5. Show the step-by-step stack content for expression a+b*c.
// 6. Difference between postfix and prefix notations.
// 7. Why is linked list implementation of stack useful compared to array-based stack?
// 8. How would you modify the code to handle multi-digit numbers and spaces?



// program / code 
// Name of Student:
// Roll No:
// Branch:
// Class:
// Experiment: Implement stack as an abstract data type using singly linked list and use this ADT for
// conversion of infix expression to postfix, prefix
// #include <iostream>
// #include <string>
// #include <cctype> // isalnum
// using namespace std;
// // Node for singly linked list (stack)
// struct Node
// {
//  char data;
//  Node* next;
//  Node(char d) : data(d), next(nullptr) {}
// };
// // Stack ADT implemented using singly linked list
// class Stack
// {
// private:
//  Node* topNode;
// public:
//  Stack() : topNode(nullptr)
//  {

//  }
//  ~Stack()
//  {
//  while (!isEmpty()) pop();
//  }
//  void push(char ch)
//  {
//  Node* newNode = new Node(ch);
//  newNode->next = topNode;
//  topNode = newNode;
//  }
//  char pop()
//  {
//  if (isEmpty()) return '\0'; // caller should check isEmpty before pop ideally
//  Node* temp = topNode;
//  char val = temp->data;
//  topNode = topNode->next;
//  delete temp;
//  return val;
//  }
//  char peek() const
//  {
//  if (isEmpty()) return '\0';


//  return topNode->data;
//  }
//  bool isEmpty() const
//  {
//  return topNode == nullptr;
//  }
// };
// // Utility: precedence of operators
// int precedence(char op)
// {
//  switch (op)
//  {
//  case '^': return 3;
//  case '*':
//  case '/': return 2;
//  case '+':
//  case '-': return 1;
//  default: return -1;
//  }
// }
// // Utility: is operator
// bool isOperator(char ch)
// {
//  return ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '^';
// }
// // Convert infix (string) to postfix (string)
// // Assumes operands are single characters (letters/digits). If multi-digit tokens needed,
// // tokenization logic must be added.
// string infixToPostfix(const string& infix)
// {
//  Stack st;
//  string output;
//  for (size_t i = 0; i < infix.length(); ++i)
// {
//  char ch = infix[i];
//  if (isspace(ch)) continue; // ignore spaces
//  // If operand, add to output
//  if (isalnum(ch))
//  {
//  output.push_back(ch);
//  }
//  // If '(', push to stack
//  else if (ch == '(')
//  {
//  st.push(ch);
//  }
//  // If ')', pop until '('
//  else if (ch == ')')
//  {


//  while (!st.isEmpty() && st.peek() != '(') {
//  output.push_back(st.pop());
//  }
//  if (!st.isEmpty() && st.peek() == '(') st.pop(); // pop '('
//  }
//  // If operator
//  else if (isOperator(ch))
//  {
//  // while top of stack has same or higher precedence
//  while (!st.isEmpty() && isOperator(st.peek()))
//  {
//  char topOp = st.peek();
//  int pTop = precedence(topOp);
//  int pCh = precedence(ch);
//  // '^' is right-associative
//  if ( (pTop > pCh) || (pTop == pCh && ch != '^') )
//  {
//  output.push_back(st.pop());
//  }
//  else
//  {
//  break;
//  }
//  }
//  st.push(ch);
//  }
//  // any other char ignored
//  }
//  // Pop remaining operators
//  while (!st.isEmpty())
//  {
//  if (st.peek() == '(' || st.peek() == ')')
//  {
//  st.pop();
//  continue;
//  }
//  output.push_back(st.pop());
//  }
//  return output;
// }
// // Convert infix to prefix using reverse method
// string infixToPrefix(const string& infix)
//  {
//  // 1. Reverse infix and swap '(' with ')'
//  string rev;
//  for (int i = (int)infix.length() - 1; i >= 0; --i)


//  {
//  char ch = infix[i];
//  if (ch == '(') rev.push_back(')');
//  else if (ch == ')') rev.push_back('(');
//  else rev.push_back(ch);
//  }
//  // 2. Convert reversed to postfix
//  string post = infixToPostfix(rev);
//  // 3. Reverse postfix -> prefix
//  string prefix;
//  for (int i = (int)post.length() - 1; i >= 0; --i) prefix.push_back(post[i]);
//  return prefix;
// }
// // Helper to show explanation
// void showMenu()
// {
//  cout << "\n--- Expression Conversion using Stack (Linked List ADT) ---\n";
//  cout << "1. Convert Infix to Postfix\n";
//  cout << "2. Convert Infix to Prefix\n";
//  cout << "3. Exit\n";
//  cout << "Enter choice: ";
// }
// int main()
// {
//  int choice;
//  string infix;
//  cout << "Stack ADT using Singly Linked List (Infix -> Postfix/Prefix)\n";
//  do
//  {
//  showMenu();
//  cin >> choice;
//  cin.ignore(); // flush newline
//  switch (choice)
//  {
//  case 1:
//  cout << "Enter infix expression (use single-letter/digit operands, e.g., a+b*(c-d)):\n";
//  getline(cin, infix);
//  {
//  string postfix = infixToPostfix(infix);
//  cout << "Postfix: " << postfix << "\n";
//  }
//  break;
//  case 2:
//  cout << "Enter infix expression (use single-letter/digit operands, e.g., a+b*(c-d)):\n";
//  getline(cin, infix);
//  {
//  string prefix = infixToPrefix(infix);
//  cout << "Prefix: " << prefix << "\n";
//  }


//  break;
//  case 3:
//  cout << "Exiting...\n";
//  break;
//  default:
//  cout << "Invalid option. Try again.\n";
//  }
//  } while (choice != 3);
//  return 0;
// }
// Sample Runs
// 1. Example 1:
// Input (infix): a+b*c
// Postfix: abc*+
// Prefix: +a*bc
// 2. Example 2:
// Input: (a+b)*(c-d)
// Postfix: ab+cd-*
// Prefix: *+ab-cd
// 3. Example 3:
// Input: a^b^c
// Postfix: abc^^ // because ^ is right-associative it becomes a (b c ^) ^ -> abc^^
// Prefix: ^a^bc