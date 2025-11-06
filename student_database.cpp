#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

struct Student {
    int id;
    char name[50];
    float cgpa;
};

// Function Prototypes
void addStudent(Student *&students, int &count);
void displayStudents(Student *students, int count);
int linearSearch(Student *students, int count, int id);
int binarySearch(Student *students, int count, int id);
void bubbleSortByName(Student *students, int count);
void selectionSortByCGPA(Student *students, int count, bool ascending);
void analyzeSearchPerformance(Student *students, int count);

int main() {
    Student *students = NULL;
    int count = 0, choice, id;

    do {
        cout << "\n====== STUDENT DATABASE MENU ======";
        cout << "\n1. Add Student";
        cout << "\n2. Display All Students";
        cout << "\n3. Linear Search by ID";
        cout << "\n4. Sort by Name (Alphabetically - Bubble Sort)";
        cout << "\n5. Sort by CGPA (Selection Sort)";
        cout << "\n6. Binary Search by ID (After Sorting by ID)";
        cout << "\n7. Analyze Search Performance";
        cout << "\n0. Exit";
        cout << "\nEnter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            addStudent(students, count);
            break;
        case 2:
            displayStudents(students, count);
            break;
        case 3:
            cout << "Enter Student ID to Search: ";
            cin >> id;
            {
                int pos = linearSearch(students, count, id);
                if (pos != -1)
                    cout << "Found: " << students[pos].name << " (CGPA: " << students[pos].cgpa << ")\n";
                else
                    cout << "Student not found!\n";
            }
            break;
        case 4:
            bubbleSortByName(students, count);
            cout << "Students sorted alphabetically by name.\n";
            break;
        case 5:
            {
                int order;
                cout << "1. Ascending\n2. Descending\nChoose order: ";
                cin >> order;
                selectionSortByCGPA(students, count, order == 1);
                cout << "Students sorted by CGPA.\n";
            }
            break;
        case 6:
            cout << "Enter Student ID to search (Binary Search): ";
            cin >> id;
            {
                int pos = binarySearch(students, count, id);
                if (pos != -1)
                    cout << "Found: " << students[pos].name << " (CGPA: " << students[pos].cgpa << ")\n";
                else
                    cout << "Student not found!\n";
            }
            break;
        case 7:
            analyzeSearchPerformance(students, count);
            break;
        case 0:
            cout << "Exiting program...\n";
            break;
        default:
            cout << "Invalid choice!\n";
        }
    } while (choice != 0);

    free(students);
    return 0;
}

// ---------------- Function Definitions ----------------

// 1. Add student with dynamic memory using realloc()
void addStudent(Student *&students, int &count) {
    students = (Student *)realloc(students, (count + 1) * sizeof(Student));
    if (!students) {
        cout << "Memory allocation failed!\n";
        return;
    }

    cout << "Enter Student ID: ";
    cin >> students[count].id;
    cout << "Enter Student Name: ";
    cin.ignore();
    cin.getline(students[count].name, 50);
    cout << "Enter CGPA: ";
    cin >> students[count].cgpa;

    count++;
    cout << "Student added successfully!\n";
}

// 2. Display student list
void displayStudents(Student *students, int count) {
    if (count == 0) {
        cout << "No student records available.\n";
        return;
    }

    cout << "\n===== Student Records =====\n";
    for (int i = 0; i < count; i++) {
        cout << "ID: " << students[i].id
             << "\tName: " << students[i].name
             << "\tCGPA: " << students[i].cgpa << endl;
    }
}

// 3. Linear Search
int linearSearch(Student *students, int count, int id) {
    for (int i = 0; i < count; i++) {
        if (students[i].id == id)
            return i;
    }
    return -1;
}

// 4. Binary Search (Assumes sorted by ID)
int binarySearch(Student *students, int count, int id) {
    int low = 0, high = count - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (students[mid].id == id)
            return mid;
        else if (students[mid].id < id)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

// 5. Bubble Sort by Name
void bubbleSortByName(Student *students, int count) {
    for (int i = 0; i < count - 1; i++) {
        for (int j = 0; j < count - i - 1; j++) {
            if (strcmp(students[j].name, students[j + 1].name) > 0) {
                Student temp = students[j];
                students[j] = students[j + 1];
                students[j + 1] = temp;
            }
        }
    }
}

// 6. Selection Sort by CGPA
void selectionSortByCGPA(Student *students, int count, bool ascending) {
    for (int i = 0; i < count - 1; i++) {
        int target = i;
        for (int j = i + 1; j < count; j++) {
            if (ascending ? (students[j].cgpa < students[target].cgpa)
                          : (students[j].cgpa > students[target].cgpa))
                target = j;
        }
        if (target != i) {
            Student temp = students[i];
            students[i] = students[target];
            students[target] = temp;
        }
    }
}

// 7. Analyze performance (Simple comparison)
void analyzeSearchPerformance(Student *students, int count) {
    if (count == 0) {
        cout << "Add students first!\n";
        return;
    }

    int id;
    cout << "Enter ID to search for performance analysis: ";
    cin >> id;

    cout << "\n-- Linear Search (Unsorted) --\n";
    int pos1 = linearSearch(students, count, id);
    if (pos1 != -1)
        cout << "Found: " << students[pos1].name << "\n";
    else
        cout << "Not found.\n";

    cout << "\n-- Sorting by ID before Binary Search --\n";
    // Sort by ID (Simple Bubble Sort)
    for (int i = 0; i < count - 1; i++) {
        for (int j = 0; j < count - i - 1; j++) {
            if (students[j].id > students[j + 1].id) {
                Student temp = students[j];
                students[j] = students[j + 1];
                students[j + 1] = temp;
            }
        }
    }

    int pos2 = binarySearch(students, count, id);
    cout << "\n-- Binary Search (Sorted) --\n";
    if (pos2 != -1)
        cout << "Found: " << students[pos2].name << "\n";
    else
        cout << "Not found.\n";
}


// Experiment No. 1 – Searching and Sorting


// Title
// Design a program to maintain a student database and perform Searching and Sorting operations
// Objectives
// 1. To understand the concept of dynamic memory allocation in C++
// 2. To implement Linear Search and Binary Search.
// 3. To implement Sorting algorithms (Bubble, Selection, Insertion).
// 4. To analyze performance of searching before and after sorting.
// Problem Statement
// Design a program to maintain a student database that performs the following tasks:
// 1. Add and store student details (ID, Name, CGPA) using dynamically allocated memory.
// 2. Expand the student list using realloc() as new entries are added.
// 3. Implement Linear Search and Binary Search to find student records by ID.
// 4. Implement at least two sorting algorithms (Bubble Sort, Selection Sort, or Insertion Sort) to sort
// student records by:
// ○ Name (Alphabetically)
// ○ CGPA (Ascending/Descending)
// 5. Analyze and compare the performance of search operations before and after sorting.
// Theory
// Dynamic Memory Allocation:
// In C programming, the amount of memory required by a program is not always known at compile time. For
// example, when dealing with arrays or linked lists, the size may depend on user input or runtime conditions.
// Dynamic Memory Allocation (DMA) allows programs to allocate and free memory at runtime from the

// heap segment of memory.This provides flexibility in building efficient programs such as databases, stacks,
// queues, linked lists, and trees.
// Functions Used in DMA (stdlib.h)
// 1. malloc() – Memory Allocation
// ○ Allocates a block of memory of given size (in bytes).
// ○ Memory is uninitialized (contains garbage values).
// ★ Syntax:
// ptr = (cast_type*) malloc(size_in_bytes);
// ★ Example:
// int *arr = (int*) malloc(5 * sizeof(int));
// 2. calloc() – Contiguous Allocation
// ○ Allocates multiple blocks of memory, initializes them to zero.
// ○ Useful for arrays.
// ★ Syntax:
// ptr = (cast_type*) calloc(num_elements, size_of_each_element);
// ★ Example:
// int *arr = (int*) calloc(5, sizeof(int)); // array of 5 ints initialized to 0
// 3. realloc() – Reallocation
// ○ Expands or shrinks previously allocated memory block.
// ○ Old data is preserved, new memory is added if expanded.
// ★ Syntax:
// ptr = (cast_type*) realloc(ptr, new_size_in_bytes);
// ★ Example:
// arr = (int*) realloc(arr, 10 * sizeof(int)); // expand array to 10 ints
// 4. free() – Memory Deallocation
// ○ Releases previously allocated memory back to the heap.
// ○ Prevents memory leak.
// ★ Syntax:
// free(ptr);
// Memory Allocation Flow (Heap Segment)
// ● malloc() / calloc() → Allocates memory from heap.
// ● realloc() → Resizes allocated block.
// ● free() → Frees memory.
// Advantages of DMA
// ● Efficient use of memory.
// ● Flexibility in handling varying data sizes.
// ● Required for advanced data structures (linked lists, trees, graphs).
// ● Prevents wastage of memory compared to static allocation.
// Applications in Lab
// ● Student Database Program: Expands records using realloc().
// ● Dynamic Arrays: Handles unknown size input from users.


// ● Linked Lists, Trees, Graphs: Nodes created dynamically using malloc().
// ★ Linear Search: Sequentially checks each element until the target is found. Time Complexity: O(n).
// Binary Search
// Binary Search is an efficient searching algorithm that works on the principle of divide and conquer.
// Unlike Linear Search, which checks each element sequentially, Binary Search repeatedly divides the sorted
// array into halves until the required element is found (or search space becomes empty).It is applicable only
// when the array/list is sorted.
// Working Principle
// 1. Start with the middle element of the sorted array.
// 2. If the middle element matches the key → search is successful.
// 3. If the key is smaller than the middle element → repeat search in the left half.
// 4. If the key is larger than the middle element → repeat search in the right half.
// 5. Continue until the element is found or the subarray size becomes zero.
// Algrithm (Binary Search – Iterative)
// BinarySearch(arr, n, key)
// . low = 0, high = n-1
// while low <= high do
// mid = (low + high) / 2
// if arr[mid] == key then
//  return mid // element found
//  else if arr[mid] < key then
//  low = mid + 1
//  else
//  high = mid - 1
// .end while
// . return -1 // element not found
// Example
// Array (sorted): [10, 20, 30, 40, 50, 60]
// Key = 40
// ● Step 1: low=0, high=5 → mid=2 → arr[2]=30 → 40 > 30 → search right half
// ● Step 2: low=3, high=5 → mid=4 → arr[4]=50 → 40 < 50 → search left half
// ● Step 3: low=3, high=3 → mid=3 → arr[3]=40 → Found at index 3
// Time Complexity
// ● Best Case → O(1) (element found at mid)
// ● Worst Case → O(log n) (divide by 2 each step)
// ● Space Complexity → O(1) for iterative, O(log n) for recursive
// Advantages
// ● Faster than linear search for large datasets.

// ● Works efficiently on sorted data structures.
// Disadvantages
// ● Requires data to be sorted.
// ● Not suitable for linked lists (no random access).
// Applications in Industry
// ● Searching in databases.
// ● Searching in dictionaries or phonebooks.
// ● Used in compiler symbol tables.
// ● Core logic in many divide and conquer algorithms.
// ★ Bubble Sort: Bubble Sort is the simplest comparison-based sorting algorithm. It repeatedly
// compares adjacent elements in the array and swaps them if they are in the wrong order. This process
// continues until the array is sorted.
//  Working Principle
// ● Compare each pair of adjacent elements.
// ● Swap them if they are in the wrong order.
// ● Repeat the process for all passes until no swaps are needed.
// Algorithm (Bubble Sort)
// BubbleSort(arr, n)
// 1. for i = 0 to n-1 do
// 2. for j = 0 to n-i-2 do
// 3. if arr[j] > arr[j+1] then
// 4. swap(arr[j], arr[j+1])
// 5. end for
// 6. end for
// Example
// Array: [5, 3, 8, 4, 2]
// ● Pass 1: [3, 5, 4, 2, 8]
// ● Pass 2: [3, 4, 2, 5, 8]
// ● Pass 3: [3, 2, 4, 5, 8]
// ● Pass 4: [2, 3, 4, 5, 8] → Sorted
// Time Complexity
// ● Best Case (already sorted): O(n)
// ● Worst Case: O(n²)
// ● Space Complexity: O(1) (in-place sorting)


// Advantages
// ● Very simple to implement.
// ● Useful for teaching basic sorting concepts.
// Disadvantages
// ● Inefficient for large datasets.
// ● Requires many passes even if nearly sorted.
// Applications
// ● Small datasets.
// ● Educational purpose (understanding sorting).
// ● Used when simplicity is more important than efficiency.
// ★ Selection Sort: Selection Sort is a simple comparison-based sorting algorithm. It works by
// repeatedly finding the smallest (or largest) element from the unsorted part of the array and placing it
// at the correct position.
//  Working Principle
// ★ Divide the array into sorted and unsorted parts.
// ★ Select the minimum element from the unsorted part.
// ★ Swap it with the first element of the unsorted part.
// ★ Repeat until the array is fully sorted.
// Algorithm (Selection Sort)
// SelectionSort(arr, n)
// for i = 0 to n-1 do
//  min_index = i
//  for j = i+1 to n-1 do
// . if arr[j] < arr[min_index] then
//  min_index = j
//  end for
//  swap(arr[i], arr[min_index])
//  end for
// Example
// Array: [64, 25, 12, 22, 11]
// ● Pass 1: Minimum = 11 → [11, 25, 12, 22, 64]
// ● Pass 2: Minimum = 12 → [11, 12, 25, 22, 64]
// ● Pass 3: Minimum = 22 → [11, 12, 22, 25, 64]
// ● Pass 4: Minimum = 25 → [11, 12, 22, 25, 64] → Sorted
// Time Complexity
// ● Best Case: O(n²)
// ● Worst Case: O(n²)
// ● Space Complexity: O(1) (in-place sorting)


// Advantages
// ● Easy to implement.
// ● Performs fewer swaps compared to Bubble Sort.
// Disadvantages
// ● Still inefficient for large datasets (O(n²)).
// ● Not adaptive (does not get faster if partially sorted).
// Applications
// ● Useful for small arrays.
// ● Situations where memory writes are costly, since it performs fewer swaps.
// Insertion Sort:
// Insertion Sort is a simple sorting algorithm that builds the sorted array one element at a time. It works like
// arranging playing cards in hand – each new card (element) is inserted into its correct position among the
// previously sorted cards.
// Working Principle
// ● Consider the first element as sorted.
// ● Pick the next element (key).
// ● Compare it with elements in the sorted part and shift larger elements to the right.
// ● Insert the key into its correct position.
// ● Repeat until the whole array is sorted.
// InsertionSort(arr, n)
// for i = 1 to n-1 do
// key = arr[i]
// j = i - 1
// while j >= 0 and arr[j] > key do
// arr[j+1] = arr[j]
// j = j - 1
// end while
// arr[j+1] = key
// end for
// Example
// Array: [5, 3, 4, 1, 2]
// ● Pass 1: Insert 3 → [3, 5, 4, 1, 2]
// ● Pass 2: Insert 4 → [3, 4, 5, 1, 2]
// ● Pass 3: Insert 1 → [1, 3, 4, 5, 2]
// ● Pass 4: Insert 2 → [1, 2, 3, 4, 5] → Sorted


// Algorithm (Steps)
// 1. Start the program.
// 2. Define a structure Student with fields: ID, Name, CGPA.
// 3. Dynamically allocate memory for student list using malloc().
// 4. Insert student details.
// 5. If more students are added, use realloc() to expand memory.
// 6. Implement functions for:
// Display student records
// Linear Search by ID
// Binary Search by ID
// Bubble Sort (by Name, CGPA)
// Selection Sort (by Name, CGPA)
// 7. Compare search performance before and after sorting.
// 8. Display results.
// 9. End program.
// Observation Table
// Operation Before Sorting (Time
// Complexity)
// After Sorting (Time
// Complexity)
// Linear Search O(n) O(n) (no change)
// Binary Search Not Possible O(log n)
// Bubble Sort (CGPA) O(n²) –
// Selection Sort (Name) O(n²) –
// Result / Conclusion
// ● Successfully implemented a dynamic student database using malloc() and realloc().
// ● Performed Linear and Binary Search for finding records.
// ● Applied Bubble Sort (CGPA) and Selection Sort (Name).
// ● Concluded that Binary Search is efficient (O(log n)), but requires data to be sorted.
// Outcome
// Students will be able to:
// ● Implement searching and sorting algorithms in C++.
// ● Use dynamic memory allocation in real-world problems.
// ● Analyze time complexity and efficiency of algorithms.


// Experiment 1 – Searching & Sorting (program code) 
// #include <iostream>
// #include <cstring> // for strcmp
// #include <cstdlib> // for malloc, realloc, free
// using namespace std;
// struct Student
// {
//  int id;
//  char name[50];
//  float cgpa;
// };
// // Function to display students
// void display(Student* students, int n)
// {
//  cout << "\nID\tName\tCGPA\n";
//  for (int i = 0; i < n; i++) {
//  cout << students[i].id << "\t" << students[i].name << "\t" << students[i].cgpa << endl;
//  }
// }
// // Linear Search
// int linearSearch(Student* students, int n, int key)
// {
//  for (int i = 0; i < n; i++)
//  {
//  if (students[i].id == key)
//  return i;
//  }
//  return -1;
// }
// // Binary Search (requires sorted IDs)
// int binarySearch(Student* students, int n, int key)
// {
//  int low = 0, high = n - 1, mid;
//  while (low <= high) {
//  mid = (low + high) / 2;
//  if (students[mid].id == key)
//  return mid;
//  else if (students[mid].id < key)
//  low = mid + 1;
//  else
//  high = mid - 1;
//  }
//  return -1;
// }
// // Bubble Sort by CGPA
// void bubbleSortByCGPA(Student* students, int n, bool ascending = true)
// {
//  for (int i = 0; i < n - 1; i++)
// {
//  for (int j = 0; j < n - i - 1; j++)
// {
//  if ((ascending && students[j].cgpa > students[j + 1].cgpa) ||
//  (!ascending && students[j].cgpa < students[j + 1].cgpa))
// {
//  Student temp = students[j];
//  students[j] = students[j + 1];
//  students[j + 1] = temp;
//  }
//  }
//  }
// }
// // Selection Sort by Name
// void selectionSortByName(Student* students, int n)
// {
//  for (int i = 0; i < n - 1; i++)
//  {
//  int min = i;
//  for (int j = i + 1; j < n; j++)
//  {
//  if (strcmp(students[j].name, students[min].name) < 0)
//  min = j;
//  }
//  Student temp = students[i];
//  students[i] = students[min];
//  students[min] = temp;
//  }
// }
// int main()
// {
//  int n, choice, key, pos;
//  Student* students;
//  cout << "Enter initial number of students: ";
//  cin >> n;
//  // Dynamic allocation
//  students = (Student*)malloc(n * sizeof(Student));
//  for (int i = 0; i < n; i++)
//  {
//  cout << "\nEnter ID, Name, CGPA for student " << i + 1 << ": ";
//  cin >> students[i].id >> students[i].name >> students[i].cgpa;
//  }
//  // Menu-driven program
//  do
//  {
//  cout << "\n\n--- Student Database Menu ---";
//  cout << "\n1. Display Students";
//  cout << "\n2. Add New Student (realloc)";
//  cout << "\n3. Linear Search by ID";
//  cout << "\n4. Binary Search by ID (requires sorted IDs)";
//  cout << "\n5. Sort by CGPA (Bubble Sort)";
//  cout << "\n6. Sort by Name (Selection Sort)";
//  cout << "\n7. Exit";
//  cout << "\nEnter choice: ";
//  cin >> choice;
//  switch (choice)
//  {
//  case 1:
//  display(students, n);
//  break;
//  case 2:
//  {
//  int addCount;
//  cout << "How many new students do you want to add? ";
//  cin >> addCount;
//  // Reallocate memory
//  students = (Student*)realloc(students, (n + addCount) * sizeof(Student));
//  for (int i = n; i < n + addCount; i++)
//  {
//  cout << "\nEnter ID, Name, CGPA for student " << i + 1 << ": ";
//  cin >> students[i].id >> students[i].name >> students[i].cgpa;
//  }
//  n += addCount;
//  cout << "\nStudents added successfully!\n";
//  break;
//  }
//  case 3:
//  cout << "Enter student ID to search (Linear): ";
//  cin >> key;
//  pos = linearSearch(students, n, key);
//  if (pos != -1)
//  cout << "Found at position " << pos + 1 << " (Linear)\n";
//  else
//  cout << "Not Found (Linear)\n";
//  break;
//  case 4:
//  cout << "Enter student ID to search (Binary): ";
//  cin >> key;
//  pos = binarySearch(students, n, key);
//  if (pos != -1)
//  cout << "Found at position " << pos + 1 << " (Binary)\n";
//  else
//  cout << "Not Found (Binary)\n";
//  break;
//  case 5:
//  bubbleSortByCGPA(students, n, true);
//  cout << "\nStudents Sorted by CGPA (Ascending):";
//  display(students, n);
//  break;
//  case 6:
//  selectionSortByName(students, n);
//  cout << "\nStudents Sorted by Name (Alphabetical):";
//  display(students, n);
//  break;
//  case 7:
//  cout << "Exiting program...\n";
//  break;
//  default:
//  cout << "Invalid choice! Try again.\n";
//  }
//  } while (choice != 7);
//  free(students);
//  return 0;
// }
// OUTPUT
// Enter initial number of students: 2
// Enter ID, Name, CGPA for student 1: 101 Amit 8.5
// Enter ID, Name, CGPA for student 2: 102 Neha 9.1
// --- Student Database Menu ---
// 1. Display Students
// 2. Add New Student (realloc)
// 3. Linear Search by ID
// 4. Binary Search by ID
// 5. Sort by CGPA
// 6. Sort by Name
// 7. Exit
// Enter choice: 1
// ID Name CGPA
// 101 Amit 8.5
// 102 Neha 9.1