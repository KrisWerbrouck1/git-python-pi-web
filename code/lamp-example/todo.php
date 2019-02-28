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
    $query = "INSERT INTO tasks (title) VALUES (?);";
    $this->pdo->prepare($query)->execute([$title]);
  }

  public function removeTask($id)
  {
    $query = "DELETE FROM tasks WHERE id = ?;";
    $this->pdo->prepare($query)->execute([$id]);
  }
}