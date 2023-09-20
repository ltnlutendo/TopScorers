# Top Scorers
A short coding challenge

## Assumptions made
1. Input text/csv "Score" column has only numbers, error handling wasn't implemented for this case.
2. The text/csv file has delimeter ','. This can be improved in the future for user to choose delimeter but wasn't part of this challenge
3. There are no empty "cells", this assumption is similar to 1.
4. If there is data in the file, there will always be a top scorer, even if there is one person.
   
### Introduction

This Python script is designed to determine the top scorer from a CSV file or text file containing data about individuals and their scores. The script reads the input data, parses it into dictionaries, identifies the top scorer(s), sorts them alphabetically by name, and displays their names along with their scores.

### Design Choices

1. **Modular Design**: The code is structured into several functions to promote modularity and readability. Each function has a specific responsibility, making the code easier to understand and maintain.

2. **Error Handling**: Robust error handling has been implemented throughout the code. It ensures that the script gracefully handles various exceptional situations, such as empty input, malformed data, or inconsistent columns in the CSV file. Detailed error messages are provided to assist users in identifying issues.

3. **Input Flexibility**: The script reads data from standard input, which means it can accept input from both files and manual input through the command line. This design choice enhances the versatility of the script.

4. **Data Parsing**: The `parse_csv` function processes CSV data, checking for a minimum of one header and one data row. It ensures data consistency by verifying that the number of columns in each row matches the number of headers.

5. **Top Scorer Identification**: The `find_top_scorers` function identifies the top scorers by extracting and comparing scores from the parsed data. It allows for multiple top scorers if they have the same highest score.

6. **Sorting**: To present the top scorers alphabetically, the `sort_data_alphabetically` function sorts the data based on the individuals' first and second names.

7. **Display**: The `display_person_info` function is responsible for displaying each top scorer's name. Additionally, the script displays the top scorer's score after listing their names.

8. **Main Function**: The `main` function orchestrates the execution of the script. It reads the input, processes the data, identifies the top scorers, sorts and displays their information, and terminates the script gracefully.

9. **Versioning**: The script includes a version number (Version: 2) and an author's name and date to provide context for maintenance and collaboration.

### How to Use

1. Run the script in a terminal.
2. Provide the CSV data through standard input (e.g., by piping a CSV file or manually entering data).
3. The script will identify the top scorers, sort them alphabetically, and display their names and scores.

### Example

```bash
$ cat TestData.csv | python TopScorers.py
```

### Conclusion

This Python script is designed with a focus on readability, maintainability, and robust error handling. It allows for flexible input methods and provides clear feedback to the user. The modular structure ensures that future updates and enhancements can be made with ease while maintaining code quality.

---
