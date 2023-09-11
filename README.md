# QRify
QRify User Guide
v 1.0

Download script: https://github.com/zzokalj/QRify 

Table of Contents:

1. Introduction
1.1 Overview
1.2 Features
2. Prerequisites
2.1 Python Installation
2.2 Required Python Libraries
2.3 CSV File Preparation
2.4 Installing QRify
3. Using QRify
3.1 Running QRify
3.2 Choosing the Language
3.3 Path to CSV File
3.4 Generating QR Codes
3.5 Multiple Languages
3.6 End of QRify
4. Tips and Troubleshooting
4.1 Tips for Using QRify
4.2 Troubleshooting Common Issues
4.3 Getting Help
5. Conclusion and Additional Resources
5.1 Summary
5.2 Additional Resources
6. Legal Information
6.1 Copyright
6.2 Trademarks
6.3 Open-Source Libraries
6.4 Data Privacy
6.5 Terms of Use

1. Introduction

Welcome to the QRify User Guide! 

QRify is a versatile Python script designed to generate QR codes from CSV data, making it easier to create QR code-based contact cards. 
Whether you want to quickly generate QR codes for multiple contacts or need an efficient way to manage your contact information, QRify can simplify the process.

1.1 Overview

QRify is a user-friendly tool that streamlines the creation of QR codes. It's especially helpful for businesses, organizations, or individuals who want to distribute contact information efficiently. With QRify, you can generate QR codes that contain contact details such as names, titles, phone numbers, email addresses, and more.

1.2 Features

QRify offers several key features to enhance your QR code generation experience:

Language Selection: QRify supports both Croatian and English languages, allowing you to generate QR codes with contact data in your preferred language.

CSV Data Import: Easily import contact data from CSV (Comma-Separated Values) files. CSV files provide a structured format for storing contact information.

QR Code Generation: QRify generates QR codes with embedded contact details, making it convenient to share contact information digitally.

Overwrite Existing QR Codes: QRify overwrites existing QR codes in the output folder, ensuring that you always have up-to-date contact information.

User-Friendly Interface: QRify provides a straightforward command-line interface, making it accessible to users with varying levels of technical expertise.

Cross-Platform Compatibility: QRify is compatible with Windows, macOS, and Linux operating systems, making it versatile for users across different platforms.

Whether you're a professional looking to create QR code-based business cards or an organization seeking an efficient way to manage contact information, QRify simplifies the process and helps you stay organized.

In the following chapters, we'll walk you through the installation, usage, and troubleshooting of QRify, ensuring you can make the most of this powerful tool.
2. Prerequisites

In this chapter, we'll cover the prerequisites you need to meet to use QRify effectively. QRify is a Python script designed to generate QR codes from CSV files containing contact information. Before you begin using QRify, make sure you have the following requirements in place.

2.1 Python Installation

QRify is a Python script, so you need to have Python installed on your computer. If you haven't already installed Python, follow these steps:

For Windows:

Visit the official Python website at Python Downloads.
Download the latest version of Python for Windows.
Run the installer and follow the installation instructions.
Make sure to check the "Add Python X.X to PATH" option during installation, where X.X represents the Python version.

For macOS:

Open a terminal.
Install Homebrew by running the following command:
bash

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

Install Python using Homebrew:

brew install python


For Linux (Ubuntu/Debian):

Open a terminal.
Run the following commands:
sql

sudo apt update
sudo apt install python3


2.2 Required Python Libraries

QRify relies on specific Python libraries that need to be installed. You can easily install these libraries using the Python package manager, pip.

Open your terminal or command prompt and run the following commands:

bash

pip install qrcode[pil]
pip install pandas

qrcode[pil]: This library is used for generating QR codes.
pandas: This library is used for handling CSV files.

2.3 CSV File Preparation

Before you start using QRify, prepare your CSV file with the necessary columns. The CSV file should contain the following columns: Ime, Prezime, titula, radno mjesto, mail, telefon, mobitel, adresa, web.

Ensure that your CSV file is properly formatted with these columns and filled with the relevant contact information.

2.4 Installing QRify

You'll need to download the QRify script and save it to your computer. Here's how to do it:

Visit the QRify GitHub repository at QRify GitHub Repository.
Click the "Code" button and select "Download ZIP" to download the ZIP file containing the QRify script.
Extract the contents of the ZIP file to a folder of your choice on your computer.


3. Using QRify

In this chapter, we'll walk you through the process of using QRify to generate QR codes from your CSV files. Follow these steps to create QR codes with ease.

3.1 Running QRify

Before you start, make sure you've completed 1. Prerequisites and have the required libraries installed.

To run QRify:

Open a terminal or command prompt on your computer.

Navigate to the folder where you've saved the QRify script using the cd command. 
For example:
bash
cd /path/to/qrify

Run QRify by entering the following command:

For Windows:
python qrify.py


For macOS and Linux:
python3 qrify.py

3.2 Choosing the Language

QRify will prompt you to choose the language: Croatian or English. 
Enter your choice to proceed.

If you choose Croatian, QRify will ask for the path to your Croatian CSV file.
If you choose English, QRify will ask for the path to your English CSV file.

3.3 Path to CSV File

After choosing the language, you'll need to provide the path to your CSV file containing contact information. Make sure your CSV file follows the required format.

3.4 Generating QR Codes

QRify will process the CSV file and generate QR codes for each contact entry. The QR codes will be saved in subfolders named CROATIAN or ENGLISH, within the QRify folder.

3.5 Multiple Languages

Currently there are 2 language options in QRify, Croatian and English. 
After generating QR codes for the chosen language, QRify will ask if you'd like to generate QR codes for the other language. You can choose Yes or No:

If you choose Yes, QRify will proceed to generate QR codes for the other language.
If you choose No, QRify will display the end message and close the program.

3.6 End of QRify

Once you've generated QR codes for both languages (if desired), QRify will display the end message: "Thank you for using QRify! Buy Zeno a coffee. ;)" and then close the program.

Congratulations! You've successfully used QRify to generate QR codes from your CSV files.

In the next chapter, we'll provide additional tips and troubleshooting guidance for common issues you might encounter while using QRify.


4. Tips and Troubleshooting

In this chapter, we'll provide some helpful tips for using QRify effectively and offer solutions to common issues that users may encounter.

4.1 Tips for Using QRify

Here are some tips to ensure a smooth experience with QRify:

CSV File Format: Ensure that your CSV file adheres to the format specified in Chapter 1. Proper formatting of the CSV file is essential for QRify to work correctly.

Unicode Characters: If your CSV file contains special characters like č, ć, š, ž, or others, make sure that the file is saved in UTF-8 encoding. If you encounter issues with special characters, consider replacing them with their non-accented counterparts to avoid encoding problems.

File Paths: Double-check that you provide the correct path to your CSV file when prompted. Any mistakes in the file path will result in an error.

Running the Script: When running QRify, ensure that you are in the correct directory where the script is located. You should see the script file, qrify.py, in the directory.

4.2 Troubleshooting Common Issues

Here are some common issues users might face and how to resolve them:

CSV File Not Found: If you receive an error message stating that the CSV file was not found, verify that you've entered the correct file path. Check for any typos or incorrect characters in the path.

Encoding Errors: If you encounter encoding errors, ensure that your CSV file is saved in UTF-8 encoding. You can do this when saving the file in programs like Microsoft Excel or Google Sheets.

Empty CSV File: If your CSV file is empty or contains no data, QRify will not generate any QR codes. Make sure your CSV file has valid contact information.

Missing Required Libraries: If you haven't installed the required libraries mentioned in Section 2.2, you may encounter errors. Follow the installation instructions in that chapter to ensure all dependencies are met.

CSV File Errors: If you receive errors when loading your CSV file, double-check the file path to ensure it's correct. Ensure the file is saved in the correct encoding (UTF-8) and follows the required format.

Special Characters: If you have special characters in your data (e.g., č, ć, š, ž) and they are not displaying correctly in the generated QR codes, consider replacing them with their closest ASCII counterparts (e.g., "č" with "c"). This can be done directly in your CSV file.

Folder and File Permissions: Ensure you have the necessary permissions to create folders and files in the directory where QRify is located. Administrative privileges might be required.

Disk Space: Check that you have sufficient disk space on your computer to generate and save QR code images. Large CSV files with many entries can result in substantial image files.

4.3 Getting Help

If you encounter issues that are not covered in this guide or need further assistance, you can seek help from the following sources:

Online Communities: Join online forums or communities related to Python programming or QR code generation. Experienced users may offer solutions to your specific problems.

Contact the Developer: You can reach out to the developer, Zeno Žokalj, for support or assistance by emailing zeno.zokalj@gmail.com
.


5. Conclusion and Additional Resources

In this final chapter of the QRify User Guide, we'll summarize what you've learned and provide you with additional resources to help you make the most of QRify.

5.1 Summary

In this guide, you've learned how to use QRify, a Python script developed by Zeno Žokalj, to generate QR codes from contact data stored in a CSV file. QRify is a versatile tool that simplifies the process of creating QR codes for your business cards, contacts, or any other use case.

Here's a brief summary of what you've covered:

Prerequisites: You've learned about the software and libraries required to run QRify successfully.

Installation: We provided step-by-step instructions on how to install the necessary software and libraries.

Usage: You've seen how to run QRify, select a language (Croatian or English), and provide the path to your CSV file. QRify then generates QR codes for your contact data.

Tips and Troubleshooting: This chapter offered tips for successful QR code generation and solutions to common issues.

Feedback and Support: You've been encouraged to provide feedback to the developer and seek support for any problems you encounter.

5.2 Additional Resources

As you continue to use QRify and explore the world of QR codes, consider these additional resources:

Python Documentation: If you're new to Python or want to deepen your knowledge, visit the official Python documentation at www.Python.org. 

Pandas Documentation: For more information on using the Pandas library for data manipulation, check out the Pandas documentation.

QR Code Information: To learn more about QR codes, how they work, and potential use cases, visit www.QRCode.com.


6. Legal Information
6.1 Copyright

QRify, including all associated files and documentation, is Copyright © 2023 by Zeno Žokalj. All rights are reserved. This software and its accompanying materials are provided "as is" without warranty of any kind, express or implied. In no event shall the copyright owner or contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.
6.2 Trademarks

Any product names, logos, brands, and other trademarks or registered trademarks used in this guide are the property of their respective holders. Their use is for identification purposes only and does not imply any endorsement or affiliation with QRify.
6.3 Open-Source Libraries

QRify may include third-party open-source libraries or modules. These libraries are used in compliance with their respective licenses and terms. For information on specific open-source components used in QRify, please refer to the documentation or readme files provided with the software.
6.4 Data Privacy

QRify generates QR codes that can contain contact information. Users are responsible for ensuring that the contact information they generate and distribute complies with applicable data protection and privacy laws. Be mindful of sharing sensitive personal information and obtain proper consent when handling contact details.
6.5 Terms of Use

By using QRify, you agree to abide by the terms and conditions outlined in this document. Please ensure that you comply with all relevant local, state, and national laws and regulations when using QRify.

If you have any questions or concerns regarding QRify's legal aspects, please contact Zeno Žokalj at zeno.zokalj@email.com.

