
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
