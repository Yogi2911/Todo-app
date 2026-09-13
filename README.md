# Full-Stack Todo App

A minimal full-stack Python web app:
- **Backend:** Flask (REST API)
- **Database:** SQLite (auto-created on first run)
- **Frontend:** HTML/CSS/JavaScript (served by Flask, talks to the API via `fetch`)

## Project structure
```
fullstack-todo-app/
├── app.py              # Flask app + REST API + SQLite
├── requirements.txt
├── templates/
│   └── index.html      # Main page
└── static/
    ├── style.css
    └── script.js
```

## Setup & Run

1. (Recommended) create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open your browser at:
   ```
   http://127.0.0.1:5000
   ```

That's it — add, check off, and delete todos. Data persists in `todos.db` (created automatically next to `app.py`).

## API endpoints

| Method | Route              | Description          |
|--------|---------------------|-----------------------|
| GET    | `/api/todos`         | List all todos        |
| POST   | `/api/todos`         | Create a todo (`{"task": "..."}`) |
| PATCH  | `/api/todos/<id>`     | Update a todo (`{"task": "...", "done": true}`) |
| DELETE | `/api/todos/<id>`     | Delete a todo         |

## Git and GitHub Workflow

This project follows a structured Git and GitHub workflow for feature development, code review, conflict resolution, and releases.

### Branch Structure

The repository uses the following branches:

* `main` - Stable production-ready code
* `develop` - Integration branch for completed features
* `feature/login` - Login functionality
* `feature/user-profile` - User profile functionality
* `fix/login-error` - Bug fixes

### Creating a Feature Branch

New features are developed using separate feature branches.

```bash
git checkout develop
git pull origin develop
git checkout -b feature/<feature-name>
```

### Making Changes

After making changes:

```bash
git status
git add .
git commit -m "feat: describe the feature"
```

### Pushing a Feature Branch

```bash
git push -u origin feature/<feature-name>
```

### Pull Request Workflow

Feature branches are merged into `develop` through Pull Requests.

The workflow is:

```text
Feature Branch
      |
      v
Pull Request
      |
      v
Code Review
      |
      v
Approval
      |
      v
develop
```

Pull Requests require code review before merging.

### Merge Conflict Resolution

When conflicts occur, the latest `develop` branch is incorporated into the feature branch.

```bash
git checkout feature/<feature-name>
git fetch origin
git rebase origin/develop
```

If a conflict occurs:

1. Open the conflicted file.
2. Review the conflicting changes.
3. Keep the required changes from both branches.
4. Remove Git conflict markers.
5. Test the application.
6. Stage the resolved file.

```bash
git add <file>
git rebase --continue
```

After a successful rebase, the feature branch can be pushed using:

```bash
git push --force-with-lease origin feature/<feature-name>
```

### Branch Protection

The `main` and `develop` branches are protected.

Direct pushes are restricted.

Changes must be submitted through Pull Requests.

At least one code review approval is required before merging.

### Bug Tracking

Bugs are tracked using GitHub Issues.

A bug fix is developed in a dedicated branch and submitted through a Pull Request.

The Pull Request references the corresponding issue using:

```text
Closes #<issue-number>
```

### Release Workflow

After the application reaches a stable state, a version tag is created.

Example:

```bash
git checkout main
git pull origin main
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

A GitHub Release is then created using the `v1.0.0` tag with release notes describing the changes.

### Complete Workflow

The complete development workflow is:

```text
develop
   |
   +---- feature/login
   |          |
   |          v
   |      Pull Request
   |          |
   |      Code Review
   |          |
   |          v
   +------ develop
              |
   +---- feature/user-profile
   |          |
   |          v
   |      Pull Request
   |          |
   |      Code Review
   |          |
   |          v
   +------ develop
              |
              v
          Pull Request
              |
          Code Review
              |
              v
             main
              |
              v
           v1.0.0
              |
              v
       GitHub Release
```

### Useful Git Commands

Check current branch:

```bash
git branch
```

Check repository status:

```bash
git status
```

View commit history:

```bash
git log --oneline --graph --all
```

Update a branch:

```bash
git pull origin <branch-name>
```

Push changes:

```bash
git push origin <branch-name>
```

Create a branch:

```bash
git checkout -b <branch-name>
```

Switch branches:

```bash
git checkout <branch-name>
```
