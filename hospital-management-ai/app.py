from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Local file paths
file_path_patients = 'patients_data.csv'  # Adjust path if necessary
file_path_doctors = 'doctors_data.csv'    # Adjust path if necessary

def fetch_local_data(file_path):

    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error fetching {file_path}: {e}")
        return None

@app.route('/')
def index():
    print("index route accessed")
    try:
        # Fetch both CSV files from local storage
        df_patients = fetch_local_data(file_path_patients)
        df_doctors = fetch_local_data(file_path_doctors)

        if df_patients is not None and df_doctors is not None:
            # Convert both DataFrames to HTML tables
            patients_table_html = df_patients.to_html(classes='table table-striped', index=False)
            doctors_table_html = df_doctors.to_html(classes='table table-striped', index=False)

            # Pass both tables to the template
            return render_template('index.html', patients_table=patients_table_html, doctors_table=doctors_table_html)
        else:
            return "Error loading data from local files."

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Run on port 80 for HTTP access
