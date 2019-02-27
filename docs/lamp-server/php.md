# PHP programming language

PHP is a popular programming language to write scripts that are executed on a server. PHP enables programs to generate dynamic webpages. PHP is mostly used together with HTML to enhance the generation of HTML code.

PHP is free and open source. Anyone can download it and start using it. This is one of the main reasons of its popularity. It is by far the most popular server-side programming language for web sites and applications.

PHP is popular because it can run on almost any operating system. It is compatible with the most of the HTTP servers and supports a wide range of databases out of the box.

## Syntax

PHP can be placed anywhere inside `.php` documents. `.php` documents are actually HTML documents that have the ability to be enriched with PHP code. PHP code is marked by the use of _tags_. PHP scripts start with `<?php` and end with `?>`.

```php
<?php
  // PHP code goes here
?>
```

An example of PHP mixed with HTML is shown below.

```php
<!DOCTYPE html>
<html>
  <body>
    <h1>My first PHP page</h1>
    <?php
      echo "Hello World!";
    ?>
  </body>
</html>
```

In PHP variables always start with the `$` character. This makes them easy to spot. Variables in PHP can contain many types.

* integer
* double
* boolean
* string
* array
* object
* null

Text can be send set in the generated document by using the `echo` statement. Any text that is passed to the `echo` statement will be shown in the result that will be send back to the browser that made the request. For example if we have this php document:

```php
<p>
    <?php echo "Hello World"; ?>
</p>
```

Then the browser will receive

```html
<p>
    Hello World
</p>
```

PHP is a programming language that supports all the important programming language features such as 

* Object oriented principles: classes, interfaces, polymorphism inheritance
* Conditionals: `if`, `else`, `elseif`, `switch`,...
* Loops: `for`, `foreach`, `while`, `do while`

Another powerful language feature that PHP implements are _associative arrays_. This means that in PHP arrays can have indexes that are not numbers, but any other kind of type. This makes some structures really easy to implement in PHP.

Some examples:

`for` loop

```php
for ($i = 1; $i <= 10; $i++) {
    echo $i;
}
```

`foreach` loop with an associative array

```php
$fruits = [
    'banana' => 'yellow',
    'apple' => 'green',
    'orange' => 'orange',
];

foreach($fruits as $fruit => $color) {
  echo "A $fruit has the color $color";
}
```

classes

```php
class Student {
    // constructor
    public function __construct($first_name, $last_name) {
        $this->first_name = $first_name;
        $this->last_name = $last_name;
    }

    public function say_name() {
        echo "My name is " . $this->first_name . " " . $this->last_name . ".\n";
    }
}

$alex = new Student("Alex", "Jones");
$alex->say_name();
```

## Installation

Installing PHP on Linux is easy with the apt package manager. Just run the following command to install PHP 7 on the Raspberry Pi.

```shell
sudo apt install php libapache2-mod-php -y
```

Note that the command above actually installs two software packages.

* `php`: This is the PHP language interpreter. This is what we need to be able to process and execute any PHP code.
* `libapache2-mod-php`: This is the Apache module that will link both Apache and the PHP runtime. If Apache encounters any PHP file it can give it to the PHP runtime before returning a result.

## Testing it out

To test if the installation is successful and if Apache is able to process PHP code, a `.php` file can be created which calls the `phpinfo()` function.

```shell
cd /var/www/html
sudo nano index.php
```

Insert the following code inside the `index.php` file.

```php
<?php
phpinfo();
```

If you now surf to [http://localhost](http://localhost) (or the IP address), you should see alot of information about the PHP and Apache installation. This will confirm that PHP and Apache are configured correctly.

![PHPinfo](./img/phpinfo.jpg)

### Hello world

Now that there is confirmation that the setup is installed and configured well, lets create a _Hello World_ application. The application will pass a String type to the browser containing the text `"Hello World"`.

```shell
cd /var/www/html
sudo nano index.php
```

Now replace the previous code with the code below:

```php
<?php
echo "Hello World";
```

When surfing to the page now, it should show only the string `Hello World`.

![Hello World in PHP](./img/php-hello-world.png)