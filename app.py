from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

tasks = []
tid = 1

def add_task(title, deadline):
    global tid
    t = {'id': tid, 'title': title, 'deadline': deadline, 'status': 'Pendiente'}
    tasks.append(t)
    tid += 1
    return t

def complete_task(task_id):
    for t in tasks:
        if t['id'] == task_id:
            t['status'] = 'Completada'
            return True
    return False

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    deadline = request.form['deadline']
    add_task(title, deadline)
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    complete_task(task_id)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
