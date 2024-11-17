# MedPrime Technologies Programming Assignments

This repository contains a series of assignments completed for MedPrime Technologies. Each assignment focuses on different parts of Python programming, helping to improve problem-solving skills and understanding of the language.

### Tasks:
1. **Assignment 1**: Renaming Files Sequentially
2. **Assignment 2**: Zipping a Folder
3. **Assignment 3**: Creating a Collage from 4 Images

---

## Table of Contents
- [Getting Started](#getting-started)
- [Assignment 1: Renaming Files Sequentially](#assignment-1-renaming-files-sequentially)
- [Assignment 2: Zipping a Folder](#assignment-2-zipping-a-folder)
- [Assignment 3: Creating a Collage from 4 Images](#assignment-3-creating-a-collage-from-4-images)
- [Prerequisites](#prerequisites)
- [Usage Instructions](#usage-instructions)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Getting Started

Follow these steps to run the scripts:

1. **Clone the repository** to your machine.
2. **Make sure Python 3.x** is installed.
3. **Install any required libraries** (see prerequisites).
4. **Run the scripts** as per the instructions for each assignment.

---

## Assignment 1: Renaming Files Sequentially

This is a Python script that renames all the files in a specified folder sequentially, while preserving the original file extensions. The program will only rename regular files and ignore directories or non-file items such as symbolic links or hidden files.

### Steps to Run the Program:

1. **Clone or Download the Script**:
   - If you haven't done so already, download or clone this repository to your local machine.

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the folder where the script is located.
   - Run the Python script using the following command:
     ```bash
     cd Assignment1
     python main.py
     ```

3. **Input the Folder Path**:
   - When prompted, enter the path to the folder where you want to rename the files.

### Example:

```bash
Please enter the path to the folder: /path/to/your/folder
Renaming files...
File 'image1.jpg' renamed to '1.jpg'
File 'document.txt' renamed to '2.txt'
File 'report.pdf' renamed to '3.pdf'
File 'notes.docx' renamed to '4.docx'
File 'music.mp3' renamed to '5.mp3'
Renaming completed.
```


## Assignment 2: Zipping a Folder

This is a Python script that zips a specified folder, including all of its subfolders and files. It creates a compressed `.zip` file of the folder and preserves the folder structure within the zip.

### Requirements

- Python 3.x
- `os` module (Standard Python Library)
- `zipfile` module (Standard Python Library)


### Steps to Run the Program:

1. **Clone or Download the Script**:
   - If you haven't done so already, download or clone this repository to your local machine.

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the folder where the script is located.
   - Run the Python script using the following command:
     ```bash
	 cd Assignment2
     python main.py
     ```

3. **Input the Folder Path**:
   - When prompted, enter the path to the folder you want to zip.

### Example:

```bash
Please enter the path to the folder: /path/to/your/folder
Creating zip file...
Successfully created zip file: /path/to/your/folder.zip
```

## Assignment 3: Creating a Collage from 4 Images

This program creates a 2x2 collage from four input images and saves the output in a specified format.

### How to Run
1. Install the Pillow library:
   `pip install pillow`
2. Run the program:
    ```bash
	 cd Assignment3
     python main.py
     ```
3. Follow the prompts to specify image paths and output format.

### Input
- Four image file paths.
- Desired output format (`jpg`, `png`, etc.).

### Output
- A collage saved as `collage.<format>`.

### Error Handling
- Handles invalid paths and unsupported file formats gracefully.





### Clone the Repository:
```bash
git clone https://github.com/Krushnajadhav9697/MedprimeAssignment.git
cd MedprimeAssignment
```



---

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository, make your changes, and submit a pull request.

---

## License

This project is licensed under the **MIT License**.

---

## Contact

If you have any questions, feel free to reach out:
- **Email**: [krushnajadhav9697@gmail.com](mailto:your-email@example.com)
- **GitHub**: [krushnajadhav9697](https://github.com/yourusername)

---
