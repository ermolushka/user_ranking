import os
import sqlite3
import logging
from flask import Flask, jsonify, request, render_template
from werkzeug.utils import secure_filename
from utils import rank_users

logging.basicConfig(
    format="%(asctime)s %(name)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level="DEBUG",
)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd() + '/uploads/'


@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        # Checking for file type, we work just with txt

        if file and file.filename.endswith(".txt"):

            filename = secure_filename(file.filename)

            # Check if the filename is already in our database, if yes we don't save it's name
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT file_name FROM people WHERE file_name = ?", (filename,))
            data = cursor.fetchall()
            if len(data) == 0:

                # Save file locally and insert it;'s name to database
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                app.logger.debug("File uploaded")
                cursor.execute("INSERT INTO people (file_name) VALUES(?)", (filename,))
                app.logger.debug("Filename saved to db")
                conn.close()

                # Return list of user_ids and names in json format
                return jsonify(rank_users(app.config['UPLOAD_FOLDER'] + filename))
    return render_template('file_upload.html')


if __name__ == '__main__':
    app.run()

