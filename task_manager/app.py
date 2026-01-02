from flask import Flask, request, redirect, render_template

app = Flask(__name__)

def load_data():
    try:
        with open('tasks.json', 'r') as f:
            import json
            return json.load(f).get('tasks')
    except FileNotFoundError:
        print(f"file tasks.json not found, creating a new one")
        try:
            with open('tasks.json', 'w') as f:
                import json
                json.dump({'tasks': []}, f)
                return []
        except Exception as e:
            print(f"Error creating new file tasks.json: {e}")
    
tasks = load_data()
next_id = len(tasks) + 1
print(f"Next ID: {next_id}")

def add_task(title, description):   
    global next_id
    task = {
        'id': next_id,
        'title': title,
        'description': description,
        'completed': False
    }
    tasks.append(task)
    save_data()
    next_id += 1

def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_data()
            return True
    return False

def save_data():
    try:
        with open('tasks.json', 'w') as f:
            import json
            json.dump({'tasks': tasks}, f)
            return True
    except Exception as e:
            print(f"Error saving data: {e}")
            return False
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

@app.route('/')
def index():
    #return "Hello, New World!"
    sorted_tasks = sorted(tasks, key=lambda x: x['completed'], reverse=True)
    return render_template('index.html', tasks=sorted_tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['text_task']
    description = request.form['description_task']
    add_task(title, description)
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete(task_id):
    if complete_task(task_id):
        return redirect('/') # Redirect to the index page   
    else:
        return "Task not found", 404 # Return a 404 error if the task is not found
    
if __name__ == "__main__":
    app.run(debug=True)