# Incremental Backup System

<!---[comment]: <>(![Incremental Backup System](https://github.com/your-username/incremental-backup-system/assets/your-image.png)) --->
![Python 3.10](https://img.shields.io/badge/Python-3.10-blue) ![Maintenance](https://img.shields.io/badge/Maintained-Yes-brightgreen) ![License](https://img.shields.io/badge/License-MIT-red) ![Code Size](https://img.shields.io/github/languages/code-size/ddhruv-iot/incremental-backup-system?style=flat&label=Code%20Size&color=yellow)




## About Project

Welcome to our **Incremental Backup System**! This Python application is designed to create incremental backups from a source directory to a destination directory, such as a pendrive, ensuring that only modified files are copied. It saves time and storage space by avoiding unnecessary data duplication. This project is based on Python 3.10 and is perfect for anyone looking to maintain an efficient and automated backup system.

## Tools and Technologies Used:

### Python Libraries used:
- os, for directory and file operations
- shutil, for file copying
- datetime, for handling file modification times

### OS Used:
- Windows (This code was developed and tested on a Windows environment, but it can be adapted for other platforms)

## How It Works:

The Incremental Backup System works by analyzing the source directory and the destination directory (e.g., pendrive) and copying only the files that have been modified since the last backup. Here's how it operates:

1. **Data Initialization:** The system initializes and maintains a record of the modification times of files in the source directory using a dictionary.

2. **File Comparison:** For each file in the source directory, the system checks whether it exists in the destination directory and if it does, it compares the modification time with the stored time. If the file is new or has been modified, it is copied to the destination directory.

3. **File Copying:** Files that need to be updated are copied from the source directory to the destination directory using the `shutil.copy2` function, which preserves file metadata.

4. **Summary:** After the backup process is complete, the system provides a summary of the total number of files modified and copied.


## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.10 or higher is installed on your system.

## Usage:

To use this incremental backup system, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/incremental-backup-system.git
   ```

2. Open the `backup.py` file and set the `source_dir` and `pendrive_dir` variables to point to your source and destination directories.

3. Run the backup system:

   ```bash
   python backup.py
   ```

The system will create incremental backups, ensuring that only modified files are copied, making it an efficient solution for your backup needs.

## Contributing

If you would like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them.
4. Commit your changes with clear and concise commit messages.
5. Push your branch to your fork.
6. Create a pull request to the main repository's `main` branch.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Thank you

Thank you for considering our Incremental Backup System. We hope this tool helps you maintain a well-organized and efficient backup strategy. If you have any suggestions or feedback, please feel free to reach out. Your input is greatly appreciated!
