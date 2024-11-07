# Poll Creation and Management Web App

## Project Description

The **Poll Creation and Management Web App** is a full-stack web application that allows users to create polls, define multiple choices for each poll, vote on polls, and delete polls. The app is built using **Python (Flask)** for the backend, **SQL** (SQLite for simplicity) for the database, and **HTML, CSS** for the frontend. Users can add as many choices as needed for each poll and are also able to vote and delete polls once they have been created.

## Technologies Used

- **Backend**: Python (Flask framework)
- **Database**: SQLite
- **Frontend**: HTML, CSS (via Flask)
- **Additional Tools**: Jinja templates for dynamic content rendering

## Features

1. **Create Polls**: 
   - Users can create a poll with a title and description.
   - The number of choices can be dynamically adjusted, allowing users to add as many choices as required.
   - The poll form is user-friendly, and choice fields are easily added or removed.

2. **Vote on Polls**:
   - Users can vote on available polls, with the system ensuring only one vote per user per poll.
   - Real-time display of voting results (optional for future enhancements).

3. **View Polls**:
   - Users can see a list of all created polls with options to vote on them or delete them.

4. **Delete Polls**:
   - Users have the ability to delete polls they have created.

5. **Responsive Design**:
   - The app is mobile-friendly and adjusts automatically for different screen sizes.

6. **Styling**:
   - The app has a clean, minimalistic design with clear typography and well-organized content.

## Setup

1. Clone this repository:
    ```bash
    git clone https://github.com/fardeenfarrukh/Poll-Creation-and-Management-App.git
    cd Poll-Creation-and-Management-App
    ```

2. Install dependencies (ensure you have Python 3.6+):
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask app:
    ```bash
    python app.py
    ```

4. Open your browser and navigate to `http://127.0.0.1:5000/` to see the app in action.

## Database Schema

- **Polls Table**:
  - `id` (INTEGER, Primary Key)
  - `title` (TEXT)
  - `description` (TEXT)

- **Choices Table**:
  - `id` (INTEGER, Primary Key)
  - `poll_id` (INTEGER, Foreign Key)
  - `choice_text` (TEXT)
  
- **Votes Table**:
  - `id` (INTEGER, Primary Key)
  - `poll_id` (INTEGER, Foreign Key)
  - `choice_id` (INTEGER, Foreign Key)
  - `user_ip` (TEXT)

## Deliverables

1. **Backend**:
   - A Flask app with routes for creating, viewing, voting, and deleting polls.
   - A database schema for polls and choices (SQLite).
   - Proper handling of user input validation for poll creation and voting.

2. **Frontend**:
   - HTML templates using Jinja to dynamically generate content.
   - A clean, responsive UI with well-organized forms, buttons, and elements.
   - An interactive poll creation form allowing dynamic addition of choices.

3. **Database**:
   - An SQLite database with tables for:
     - `Polls`: Store poll details (title, description).
     - `Choices`: Store choices for each poll.
     - `Votes`: Track votes for each poll choice.

4. **Functionality**:
   - Fully functional CRUD operations for polls and choices.
   - Voting system ensuring each user can vote once per poll.
   - Poll deletion functionality, limited to the poll creator.

5. **Documentation**:
   - A brief README file explaining the setup, usage, and functionalities of the application.

## Testing

- **Unit Testing**:
   - Test poll creation, choice addition, and deletion features.
   - Test the voting system to ensure users can only vote once per poll.
  
- **Integration Testing**:
   - Ensure the system functions as expected when interacting with both the database and frontend (e.g., creating a poll, voting, etc.).

- **User Acceptance Testing (UAT)**:
   - Test the app with real users to ensure ease of use, and make any UI/UX improvements based on feedback.

## Future Enhancements (Optional)

1. **Real-time Voting Results**: Display voting results dynamically once a user votes.
2. **Authentication**: Implement user authentication (login/signup) for better management of poll ownership and voting rights.
3. **Deployment**: Deploy the app on cloud platforms such as Heroku or PythonAnywhere for access from anywhere.
4. **Advanced Styling**: Enhance UI with animations, transitions, and additional custom styles.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask for web framework
- SQLite for database
- Jinja for dynamic templating
- Bootstrap for responsive layout (optional for future improvements)

---

Feel free to update the **Repository URL** and **License section** based on your actual setup. This README file provides a detailed overview, setup instructions, and features to guide you through the development and use of the project.
