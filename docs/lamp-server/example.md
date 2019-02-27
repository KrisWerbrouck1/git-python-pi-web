# Todo app example

Todo application

## Database

```sql
CREATE DATABASE todo;
USE todo;
CREATE TABLE tasks (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(32) NOT NULL,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## Todo class

```php
<?php

class Todo
{
  public function __construct()
  {
    $this->pdo = new PDO("mysql:host=localhost;dbname=todo", "root", "");
  }

  public function getTasks()
  {
    $stm = $this->pdo->query("SELECT * FROM tasks");
    return $stm->fetchAll(PDO::FETCH_OBJ);
  }

  public function addTask($title)
  {
    $query = "INSERT INTO tasks (title, state) VALUES (?, false);";
    $this->pdo->prepare($query)->execute([$title]);
  }

  public function removeTask($id)
  {
    $query = "DELETE FROM tasks WHERE id = ?;";
    $this->pdo->prepare($query)->execute([$id]);
  }
}
```

## PHP document

```php
<?php

require_once('todo.php');

$todo = new Todo();

if(isset($_POST['newtask'])) {
  $todo->addTask($_POST['newtask']);
}

if(isset($_POST['delete'])) {
  $todo->removeTask($_POST['delete']);
}

// fetch all task in the database
$tasks = $todo->getTasks();

?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <title>Todo app</title>
</head>
<body>
  <div class="container">
    <h1>Todo</h1>

    <h2>Add a new task</h2>
    <form action="index.php" method="post">
      <input type="text" name="newtask">
      <button type="submit" class="btn">Add</button>
    </form>

    <h2>Task list</h2>
    <form action="index.php" method="post">
      <ul class="collection">
        <?php foreach ($tasks as $task) { ?>
            <li class="collection-item">
              <?php echo $task->title; ?>
              <button type="submit"
                class="btn-floating btn-small waves-effect waves-light red secondary-content"
                name="delete" value="<?php echo $task->id ?>">
                <i class="material-icons">close</i>
              </button>
            </li>
        <?php } ?>
      </ul>
    </form>
  </div>
</body>
</html>
```