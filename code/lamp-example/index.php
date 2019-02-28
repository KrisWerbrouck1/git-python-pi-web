<?php

require_once('todo.php');
$todo = new Todo();

if(isset($_POST['newtask'])) {
  $todo->addTask($_POST['newtask']);
}

if(isset($_POST['delete'])) {
  $todo->removeTask($_POST['delete']);
}

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
              <?php echo $task->title ?> 
              <button type="submit" style="margin: 0px;" class="btn-floating btn-small waves-effect waves-light red secondary-content" name="delete" value="<?php echo $task->id ?>">
                <i class="material-icons">close</i>
              </button>
            </li>
        <?php } ?>
      </ul>
    </form>
  </div>
</body>
</html>