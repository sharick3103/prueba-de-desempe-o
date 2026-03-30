# Student Management System

A robust console-based application developed in **Python** to manage student records through CRUD (Create, Read, Update, and Delete) operations.

---

## 🚀 How to Run

1.  **Requirements**: Ensure you have [Python 3.x](https://www.python.org) installed on your system.
2.  **File Setup**: Make sure both `main.py` and `functions.py` are located in the same directory.
3.  **Execution**: Open your terminal or command prompt in the project folder and run:
    ```bash
    python main.py
    ```

---

## 🛠️ Included Features

-   **Register Student**: Capture essential data including ID, name, age, course, and status (Active/Inactive).
-   **Consult List**: Display a formatted list of all currently registered students.
-   **Update Information**: Modify the name and course of any existing student using their unique ID.
-   **Delete Records**: Permanently remove a student from the system's database.
-   **Input Validation**: Integrated error handling (`try-except`) to prevent crashes when non-numeric values are entered in ID or age fields.

---

## 📝 Usage Examples

### **Example 1: Registering a New Student**
**User Input:**
- Identification: `1020`
- Name: `John Doe`
- Age: `21`
- Course: `Computer Science`
- Status: `Active`

**System Output:**
```text
========================================
 student : John Doe 
 ID : 1020 
 age : 21 
 course : Computer Science 
 status : Active 
========================================
