# Project Themis-Solare

A simple Flask application for uploading, processing, and downloading CSV files. The main functionality is to allow users to upload a CSV file, process it by removing duplicates, and provide a downloadable version of the updated file.

## Main Functionality

- Upload CSV files via a web interface.
- Process the CSV to remove duplicate entries.
- Provide a download link for the processed file.

## Technologies Used

- **Flask** for backend routing and request handling.
- **Pandas** for data processing.
- **HTML/CSS** for frontend design.

## To-Do

- [x] Set up Flask application structure.
- [x] Create an upload form in `index.html` to receive CSV files.
- [x] Implement file upload handling in Flask.
- [x] Process CSV files to remove duplicates using Pandas.
- [x] Generate a download link for the processed file.
- [ ] Add error handling for invalid file types.
- [ ] Improve UI/UX for better user experience.
- [ ] Add progress indicators during file upload and processing.
- [ ] Write unit tests for CSV processing functions.
- [ ] Enhance security for file uploads (e.g., file size limits, sanitizing file names).
- [ ] Document the codebase with comments and function docstrings.

## Project Structure

```
project-root/
│
├── main.py                 # Main entry point for running the Flask server
├── config.py               # Configuration settings for the Flask app
├── app/
│   ├── __init__.py         # Initializes the app package
│   ├── routes.py           # Routes for handling requests
│   └── utils.py            # Utility functions for processing CSV files
│
├── uploads/                # Folder for storing uploaded and processed CSV files
├── templates/
│   └── index.html          # Main HTML page for file upload
├── static/
│   └── style.css           # CSS for styling the frontend
└── requirements.txt        # List of dependencies
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This provides a clear list of what’s been done and what remains to be done, making it easy to track progress and contributions.