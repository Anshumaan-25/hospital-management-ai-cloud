# Hospital Management Using AI and Cloud
## Overview
This project implements a **Hospital Management System** using **AI** and **cloud-based storage** to manage and analyze hospital data. The system stores and displays key data about **patients** and **doctors**. Additionally, it incorporates **Anomaly Detection** using the **Isolation Forest** algorithm to detect unusual patterns in the data (such as high salaries for doctors or abnormal visit counts for patients).

The project is built using **Python**, **Flask**, and various libraries such as **Pandas**, **Scikit-learn**, and **Bootstrap** for the web interface. It also fetches data from **CSV files** and presents the results in a **tabular format** on a web page.
## Features
- **Hospital Data Management**: Stores and displays data about patients and doctors.
- **Anomaly Detection**: Detects anomalies in hospital data using the **Isolation Forest** algorithm.
- **Web Interface**: Displays the data and anomalies through a clean and responsive web interface.
- **Cloud Integration**: The system is set up to support cloud storage solutions (e.g., AWS S3), though it currently uses local CSV files.

## Technologies Used
- **Python**: Programming language used for backend processing and anomaly detection.
- **Flask**: Web framework used to build the web interface.
- **Pandas**: Used to manipulate and display data from CSV files.
- **Scikit-learn**: Machine learning library used to implement the **Isolation Forest** algorithm.
- **Bootstrap**: Front-end framework used to style the web page and tables.
- **HTML/CSS**: Used for the structure and design of the web interface.

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hospital-management-ai.git
   cd hospital-management-ai

pip install -r requirements.txt

python app2.py


Explanation:
- The `1.`, `2.`, etc., create an ordered (numbered) list.
- The code snippets inside triple backticks (```) are formatted as code blocks.
- You should replace `your-username` in the clone URL with your actual GitHub username once the project is uploaded.

---

### Step 7: Usage Instructions

Add instructions on how users can use your app.

```markdown
## Usage
- Open the application in your web browser by going to `http://127.0.0.1:5000/`.
- The web page will display:
  - **Patients Data** (in a table format)
  - **Doctors Data** (in a table format)
  - **Detected Anomalies** (if any, displayed in a separate table)
  
The application fetches data from CSV files, processes it to detect anomalies, and then displays the data and anomalies on the web page.

## Anomaly Detection Logic
The system uses the **Isolation Forest** algorithm from **Scikit-learn** to detect anomalies. Anomalies are defined as data points that significantly deviate from the normal distribution of the data. The system checks for anomalies in the following columns:

- **Patients Data**:
  - `age`
  - `visit count`

- **Doctors Data**:
  - `annual salary`
  - `department`

The anomalies are flagged and displayed separately in a table on the web page.

## Contributing
Feel free to fork this repository and contribute to the project! If you find any bugs, have suggestions for improvements, or want to add new features, please create an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
